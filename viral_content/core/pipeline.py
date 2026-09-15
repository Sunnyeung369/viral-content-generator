"""
主流程编排模块
v4.0 - 协调所有核心模块，完成从热点到内容的完整流程

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from typing import Dict, Any, List, Optional, Union
from datetime import datetime
import logging

from ..models import (
    GenerationConfig,
    GenerationResult,
    Account,
    Offer,
    Trend,
    StyleProfile,
)
from ..trends.base import TrendCategory
from ..core.account_fingerprint import AccountFingerprint
from ..core.style_mixer import StyleMixer
from ..core.conversion_funnel import ConversionFunnelWriter, ConversionGoal
from ..core.platform_adapter import PlatformAdapter, ContentPlatform as Platform
from ..core.prompt_compiler import PromptCompiler
from ..generators.factory import GeneratorFactory
from ..scorers import QualityScorer, ScoringResult
from ..trends import TrendAggregator
from ..exceptions.custom import ValidationError, GenerationError


logger = logging.getLogger(__name__)


class ViralContentPipeline:
    """病毒式内容生成主流程

    流程：
    1. 加载配置（账号、产品、风格）
    2. 获取/处理热点
    3. 匹配评分（可选）
    4. 编译提示词
    5. 生成内容
    6. 评分优化
    7. 多平台适配（可选）
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """初始化流程

        Args:
            config: 全局配置
        """
        self.config = config or {}

        # 初始化各模块
        self.account_loader = AccountFingerprint()
        self.style_mixer = StyleMixer()
        self.conversion_writer = ConversionFunnelWriter()
        self.platform_adapter = PlatformAdapter()
        self.prompt_compiler = PromptCompiler()
        self.generator_factory = GeneratorFactory()
        self.trend_aggregator = TrendAggregator()

        # 缓存
        self._account_cache: Dict[str, Account] = {}
        self._offer_cache: Dict[str, Offer] = {}
        self._style_cache: Dict[str, StyleProfile] = {}

    def run(
        self,
        topic: str,
        account: Union[str, Account],
        offer: Union[str, Offer],
        style_mix: Union[str, List[str]],
        goal: Union[str, ConversionGoal],
        platform: Union[str, Platform],
        trend_data: Optional[Union[str, Trend, List[Trend]]] = None,
        config: Optional[GenerationConfig] = None,
    ) -> GenerationResult:
        """执行完整流程

        Args:
            topic: 话题/热点描述
            account: 账号配置（路径或Account对象）
            offer: 产品/服务配置（路径或Offer对象）
            style_mix: 风格混合（逗号分隔或列表）
            goal: 成交目标
            platform: 目标平台
            trend_data: 热点数据（可选）
            config: 生成配置

        Returns:
            生成结果
        """
        try:
            # 1. 加载配置
            account_obj = self._load_account(account)
            offer_obj = self._load_offer(offer)
            style_profiles = self._load_styles(style_mix)
            goal_obj = self._parse_goal(goal)
            platform_obj = self._parse_platform(platform)

            # 2. 处理热点
            trend_obj = self._process_trend(topic, trend_data)

            # 3. 编译提示词
            prompt = self._compile_prompt(
                trend=trend_obj,
                account=account_obj,
                offer=offer_obj,
                styles=style_profiles,
                goal=goal_obj,
                platform=platform_obj,
            )

            # 4. 生成内容
            generation_config = config or GenerationConfig()
            result = self._generate_content(prompt, generation_config)

            # 5. 评分和优化
            scored_result = self._score_and_optimize(
                result=result,
                account=account_obj,
                offer=offer_obj,
                goal=goal_obj,
                platform=platform_obj,
            )

            # 6. 元数据
            scored_result.metadata.update({
                "pipeline_version": "4.0",
                "account": account_obj.name,
                "offer": offer_obj.name,
                "styles": [s.name for s in style_profiles],
                "goal": goal_obj.value,
                "platform": platform_obj.value,
                "trend_id": getattr(trend_obj, "id", None),
                "generated_at": datetime.now().isoformat(),
            })

            return scored_result

        except Exception as e:
            logger.error(f"Pipeline error: {e}")
            raise GenerationError(f"Pipeline execution failed: {e}")

    def run_batch(
        self,
        trends: List[Trend],
        account: Union[str, Account],
        offer: Union[str, Offer],
        style_mix: Union[str, List[str]],
        goal: Union[str, ConversionGoal],
        platforms: List[Union[str, Platform]],
        config: Optional[GenerationConfig] = None,
    ) -> List[GenerationResult]:
        """批量生成内容

        Args:
            trends: 热点列表
            account: 账号配置
            offer: 产品配置
            style_mix: 风格混合
            goal: 成交目标
            platforms: 目标平台列表
            config: 生成配置

        Returns:
            生成结果列表
        """
        results = []

        for trend in trends:
            try:
                for platform in platforms:
                    result = self.run(
                        topic=trend.topic,
                        account=account,
                        offer=offer,
                        style_mix=style_mix,
                        goal=goal,
                        platform=platform,
                        trend_data=trend,
                        config=config,
                    )
                    results.append(result)
            except Exception as e:
                logger.warning(f"Failed to generate for trend {trend.id}: {e}")
                continue

        return results

    def _load_account(self, account: Union[str, Account]) -> Account:
        """加载账号配置"""
        if isinstance(account, Account):
            return account

        if account in self._account_cache:
            return self._account_cache[account]

        loaded = self.account_loader.load_account(account)
        self._account_cache[account] = loaded
        return loaded

    def _load_offer(self, offer: Union[str, Offer]) -> Offer:
        """加载产品配置"""
        if isinstance(offer, Offer):
            return offer

        if offer in self._offer_cache:
            return self._offer_cache[offer]

        loaded = self.account_loader.load_offer(offer)
        self._offer_cache[offer] = loaded
        return loaded

    def _load_styles(self, style_mix: Union[str, List[str]]) -> List[StyleProfile]:
        """加载风格配置"""
        if isinstance(style_mix, str):
            style_ids = [s.strip() for s in style_mix.split(",")]
        else:
            style_ids = style_mix

        profiles = []
        for style_id in style_ids:
            if style_id in self._style_cache:
                profiles.append(self._style_cache[style_id])
            else:
                profile = self.style_mixer.get_style(style_id)
                self._style_cache[style_id] = profile
                profiles.append(profile)

        return profiles

    def _parse_goal(self, goal: Union[str, ConversionGoal]) -> ConversionGoal:
        """解析成交目标"""
        if isinstance(goal, ConversionGoal):
            return goal
        return ConversionGoal(goal)

    def _parse_platform(self, platform: Union[str, Platform]) -> Platform:
        """解析平台"""
        if isinstance(platform, Platform):
            return platform
        return Platform(platform)

    def _process_trend(
        self,
        topic: str,
        trend_data: Optional[Union[str, Trend, List[Trend]]] = None
    ) -> Trend:
        """处理热点数据"""
        if isinstance(trend_data, Trend):
            return trend_data

        if isinstance(trend_data, list) and trend_data:
            return trend_data[0]

        if isinstance(trend_data, str):
            # 尝试解析JSON
            import json
            try:
                data = json.loads(trend_data)
                if "trends" in data and data["trends"]:
                    return Trend.from_dict(data["trends"][0])
            except json.JSONDecodeError:
                pass

        # 创建基础热点对象
        return Trend(
            id=f"manual_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            topic=topic,
            description="",
            source="manual_input",
            url="",
            category=TrendCategory.UNKNOWN,
            keywords=[],
            metrics=None,
            content_snippet=topic,
            created_at=datetime.now()
        )

    def _compile_prompt(
        self,
        trend: Trend,
        account: Account,
        offer: Offer,
        styles: List[StyleProfile],
        goal: ConversionGoal,
        platform: Platform,
    ) -> str:
        """编译提示词"""
        return self.prompt_compiler.compile(
            task_info={
                "topic": trend.topic,
                "trend_description": trend.description,
                "trend_source": trend.source,
                "category": getattr(trend, "category", TrendCategory.UNKNOWN).value,
            },
            account=account,
            offer=offer,
            styles=styles,
            goal=goal,
            platform=platform,
        )

    def _generate_content(
        self,
        prompt: str,
        config: GenerationConfig,
    ) -> GenerationResult:
        """生成内容"""
        generator = self.generator_factory.get_generator(config.provider)

        result = generator.generate(
            prompt=prompt,
            config=config,
        )

        return result

    def _score_and_optimize(
        self,
        result: GenerationResult,
        account: Account,
        offer: Offer,
        goal: ConversionGoal,
        platform: Platform,
    ) -> GenerationResult:
        """评分和优化"""
        scorer = QualityScorer()

        # 评分
        scores = scorer.score_all(
            content=result.content,
            account=account,
            offer=offer,
            goal=goal,
            platform=platform,
        )

        # 添加建议
        suggestions = scorer.get_improvement_suggestions(scores)

        result.scores = scores
        result.suggestions = suggestions

        return result


class PipelineBuilder:
    """流程构建器（Builder模式）"""

    def __init__(self):
        """初始化构建器"""
        self._config: Dict[str, Any] = {}
        self._account: Optional[Union[str, Account]] = None
        self._offer: Optional[Union[str, Offer]] = None
        self._styles: Optional[Union[str, List[str]]] = None
        self._goal: Optional[ConversionGoal] = None
        self._platform: Optional[Platform] = None
        self._generation_config: Optional[GenerationConfig] = None

    def with_config(self, config: Dict[str, Any]) -> "PipelineBuilder":
        """设置全局配置"""
        self._config.update(config)
        return self

    def with_account(self, account: Union[str, Account]) -> "PipelineBuilder":
        """设置账号"""
        self._account = account
        return self

    def with_offer(self, offer: Union[str, Offer]) -> "PipelineBuilder":
        """设置产品"""
        self._offer = offer
        return self

    def with_styles(self, styles: Union[str, List[str]]) -> "PipelineBuilder":
        """设置风格"""
        self._styles = styles
        return self

    def with_goal(self, goal: Union[str, ConversionGoal]) -> "PipelineBuilder":
        """设置成交目标"""
        self._goal = goal if isinstance(goal, ConversionGoal) else ConversionGoal(goal)
        return self

    def with_platform(self, platform: Union[str, Platform]) -> "PipelineBuilder":
        """设置平台"""
        self._platform = platform if isinstance(platform, Platform) else Platform(platform)
        return self

    def with_generation_config(self, config: GenerationConfig) -> "PipelineBuilder":
        """设置生成配置"""
        self._generation_config = config
        return self

    def build(self) -> ViralContentPipeline:
        """构建流程"""
        pipeline = ViralContentPipeline(self._config)

        # 验证必需参数
        if not all([self._account, self._offer, self._styles, self._goal, self._platform]):
            raise ValidationError("Missing required parameters for pipeline")

        return pipeline

    def generate(self, topic: str, trend_data: Optional[Union[str, Trend, List[Trend]]] = None) -> GenerationResult:
        """快速生成（一步构建并执行）"""
        pipeline = self.build()
        return pipeline.run(
            topic=topic,
            account=self._account or "",  # type: ignore
            offer=self._offer or "",  # type: ignore
            style_mix=self._styles or [],  # type: ignore
            goal=self._goal or ConversionGoal.LEADS,  # type: ignore
            platform=self._platform or Platform.WECHAT,  # type: ignore
            trend_data=trend_data,
            config=self._generation_config,
        )

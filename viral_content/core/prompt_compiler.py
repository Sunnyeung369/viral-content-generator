"""
提示词编译器
v4.0 - 动态编译提示词

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from pathlib import Path
from typing import Dict, Any, Optional, List
from string import Template
import yaml


class PromptCompiler:
    """提示词编译器

    功能：
    1. 加载markdown模板
    2. 编译变量
    3. 组合多个模板
    4. 输出完整提示词
    """

    def __init__(self, prompts_dir: Optional[Path] = None):
        """初始化编译器

        Args:
            prompts_dir: 提示词模板目录，默认为项目prompts目录
        """
        if prompts_dir is None:
            # 默认使用项目根目录下的prompts目录
            current_dir = Path(__file__).parent.parent.parent
            prompts_dir = current_dir / "prompts"

        self.prompts_dir = Path(prompts_dir)
        self._templates: Dict[str, str] = {}
        self._cache: Dict[str, str] = {}

    def load_template(self, template_name: str) -> str:
        """加载模板文件

        Args:
            template_name: 模板文件名（不含.md后缀）

        Returns:
            模板内容

        Raises:
            FileNotFoundError: 模板文件不存在
        """
        if template_name in self._templates:
            return self._templates[template_name]

        template_path = self.prompts_dir / f"{template_name}.md"

        if not template_path.exists():
            raise FileNotFoundError(f"模板文件不存在: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()

        self._templates[template_name] = content
        return content

    def compile(
        self,
        template_name: str,
        variables: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> str:
        """编译单个模板

        Args:
            template_name: 模板名称
            variables: 变量字典
            **kwargs: 额外的变量

        Returns:
            编译后的内容
        """
        template_content = self.load_template(template_name)

        # 合并变量
        all_vars = {}
        if variables:
            all_vars.update(variables)
        all_vars.update(kwargs)

        # 使用Template进行变量替换
        template = Template(template_content)
        try:
            compiled = template.substitute(all_vars)
        except KeyError as e:
            # 如果有变量缺失，使用safe_substitute
            template = Template(template_content)
            compiled = template.safe_substitute(all_vars)

        return compiled

    def compose(
        self,
        templates: List[str],
        variables: Optional[Dict[str, Any]] = None,
        separator: str = "\n\n---\n\n",
        **kwargs
    ) -> str:
        """组合多个模板

        Args:
            templates: 模板名称列表
            variables: 共享变量字典
            separator: 模板间的分隔符
            **kwargs: 额外的变量

        Returns:
            组合后的完整内容
        """
        parts = []
        for template_name in templates:
            content = self.compile(template_name, variables, **kwargs)
            parts.append(content)

        return separator.join(parts)

    def build_system_prompt(
        self,
        topic: str,
        style_config: Optional[Dict[str, Any]] = None,
        account_config: Optional[Dict[str, Any]] = None,
        offer_config: Optional[Dict[str, Any]] = None,
        goal: str = "likes",
        platform: str = "wechat",
        **kwargs
    ) -> str:
        """构建完整的系统提示词

        Args:
            topic: 热点话题
            style_config: 风格配置
            account_config: 账号配置
            offer_config: 产品配置
            goal: 成交目标
            platform: 目标平台
            **kwargs: 额外参数

        Returns:
            完整的系统提示词
        """
        # 在开头添加任务信息
        task_info = f"""# 任务信息

## 话题
{topic}

## 成交目标
{goal}

## 目标平台
{platform}

---

"""

        # 基础系统提示词
        base_prompt = task_info + self.compile("base_system")

        # 根据成交目标添加模板
        if goal in ["likes", "comments", "leads", "sales"]:
            goal_prompt = self.compile("conversion_goal")
            base_prompt += "\n\n## 成交目标策略\n\n"
            base_prompt += goal_prompt

        # 根据平台添加适配策略
        platform_mapping = {
            "wechat": "公众号",
            "video": "视频号",
            "xiaohongshu": "小红书",
            "zhihu": "知乎",
            "douyin": "抖音",
            "bilibili": "B站",
            "weibo": "微博",
        }

        platform_name = platform_mapping.get(platform, platform)
        platform_prompt = self.compile("platform_adapter")
        base_prompt += f"\n\n## 平台适配: {platform_name}\n\n"
        base_prompt += platform_prompt

        # 添加风格配置
        if style_config:
            style_desc = self._format_style_config(style_config)
            base_prompt += f"\n\n## 风格配置\n\n{style_desc}"

        # 添加账号配置
        if account_config:
            account_desc = self._format_account_config(account_config)
            base_prompt += f"\n\n## 账号定位\n\n{account_desc}"

        # 添加产品配置
        if offer_config:
            offer_desc = self._format_offer_config(offer_config)
            base_prompt += f"\n\n## 产品服务\n\n{offer_desc}"

        return base_prompt

    def _format_style_config(self, style_config: Dict[str, Any]) -> str:
        """格式化风格配置"""
        parts = []

        if "label" in style_config:
            parts.append(f"**风格**: {style_config['label']}")

        if "style_dna" in style_config:
            dna = style_config["style_dna"]
            if isinstance(dna, dict):
                tone = dna.get("tone", "")
                if tone:
                    parts.append(f"**语气**: {tone}")

        if "hook_patterns" in style_config:
            hooks = style_config["hook_patterns"]
            if isinstance(hooks, list) and hooks:
                parts.append(f"**钩子模式**:\n" + "\n".join(f"  - {h}" for h in hooks[:3]))

        return "\n".join(parts)

    def _format_account_config(self, account_config: Dict[str, Any]) -> str:
        """格式化账号配置"""
        parts = []

        if "name" in account_config:
            parts.append(f"**账号名称**: {account_config['name']}")

        if "identity" in account_config:
            parts.append(f"**定位**: {account_config['identity']}")

        if "target_audience" in account_config:
            audience = account_config["target_audience"]
            if isinstance(audience, list) and audience:
                parts.append(f"**目标用户**:\n" + "\n".join(f"  - {a}" for a in audience[:3]))

        return "\n".join(parts)

    def _format_offer_config(self, offer_config: Dict[str, Any]) -> str:
        """格式化产品配置"""
        parts = []

        if "name" in offer_config:
            parts.append(f"**产品名称**: {offer_config['name']}")

        if "unique_value_proposition" in offer_config:
            uvp = offer_config["unique_value_proposition"]
            if isinstance(uvp, list) and uvp:
                parts.append(f"**核心卖点**:\n" + "\n".join(f"  - {v}" for v in uvp[:3]))

        if "pricing" in offer_config:
            pricing = offer_config["pricing"]
            if isinstance(pricing, dict):
                parts.append(f"**价格阶梯**:\n" + "\n".join(f"  - {k}: {v}" for k, v in pricing.items()))

        return "\n".join(parts)

    def clear_cache(self):
        """清除缓存"""
        self._cache.clear()

    def clear_templates(self):
        """清除已加载的模板"""
        self._templates.clear()
        self.clear_cache()


# 全局单例实例
_compiler_instance: Optional[PromptCompiler] = None


def get_compiler(prompts_dir: Optional[Path] = None) -> PromptCompiler:
    """获取编译器单例

    Args:
        prompts_dir: 提示词模板目录

    Returns:
        PromptCompiler实例
    """
    global _compiler_instance
    if _compiler_instance is None:
        _compiler_instance = PromptCompiler(prompts_dir)
    return _compiler_instance

#!/usr/bin/env python3
"""
爆款内容生成器 - 命令行工具 v3.1
支持多个AI平台：OpenAI, Claude, Gemini
支持流式输出、重试机制、配置文件

作者: Sunnyeung
版本: 3.1.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

import os
import sys
import argparse
import logging
import time
from pathlib import Path
from typing import Optional, Dict, Any, Callable, Protocol
from datetime import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import lru_cache
import threading

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('viral_content_generator.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 常量定义
SKILL_PATH = Path(__file__).parent / "skill_v3.0.md"
FALLBACK_SKILL_PATH = Path(__file__).parent / "skill.md"
CONFIG_PATH = Path(__file__).parent / "config.yaml"
SUPPORTED_PLATFORMS = ['openai', 'claude', 'gemini']
SUPPORTED_STYLES = [
    '老司机风格', '专业导师风格', '故事叙述风格', '数据分析风格',
    '反常识风格', '清单工具风格', '对话问答风格', '诗意哲思风格',
    '自定义风格'
]
MIN_WORD_COUNT = 500
MAX_WORD_COUNT = 20000
DEFAULT_MAX_TOKENS = 16384
MAX_RETRIES = 3
RETRY_DELAY = 1.0


# ============================================================================
# 异常类
# ============================================================================

class ViralContentError(Exception):
    """基础异常类"""
    pass


class SkillLoadError(ViralContentError):
    """Skill文件加载错误"""
    pass


class APIError(ViralContentError):
    """API调用错误"""
    pass


class ValidationError(ViralContentError):
    """参数验证错误"""
    pass


class ConfigError(ViralContentError):
    """配置错误"""
    pass


# ============================================================================
# 数据类
# ============================================================================

@dataclass
class GenerationConfig:
    """生成配置"""
    topic: str
    style: str = '老司机风格'
    word_count: int = 6000
    platform: str = 'openai'
    api_key: Optional[str] = None
    model: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = DEFAULT_MAX_TOKENS
    stream: bool = False
    output_path: Optional[str] = None


@dataclass
class GenerationResult:
    """生成结果"""
    content: str
    platform: str
    model: str
    tokens_used: int = 0
    duration_seconds: float = 0.0
    truncated: bool = False


# ============================================================================
# Skill 加载器（带缓存）
# ============================================================================

class SkillLoader:
    """Skill文件加载器，支持缓存和热重载"""

    _instance = None
    _lock = threading.Lock()
    _cached_content: Optional[str] = None
    _cached_mtime: Optional[float] = None

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def load(self, force_reload: bool = False) -> str:
        """
        加载Skill内容（带缓存）

        Args:
            force_reload: 强制重新加载

        Returns:
            str: Skill文件内容

        Raises:
            SkillLoadError: 当Skill文件不存在或无法读取时
        """
        try:
            # 检查缓存
            if not force_reload and self._cached_content is not None:
                current_mtime = SKILL_PATH.stat().st_mtime
                if current_mtime == self._cached_mtime:
                    logger.debug("使用缓存的Skill内容")
                    return self._cached_content

            # 加载文件
            if SKILL_PATH.exists():
                content = self._load_file(SKILL_PATH)
                self._update_cache(content, SKILL_PATH)
                logger.info(f"成功加载Skill文件: {SKILL_PATH}")
                return content
            elif FALLBACK_SKILL_PATH.exists():
                content = self._load_file(FALLBACK_SKILL_PATH)
                self._update_cache(content, FALLBACK_SKILL_PATH)
                logger.warning(f"使用回退Skill文件: {FALLBACK_SKILL_PATH}")
                return content
            else:
                raise SkillLoadError("找不到Skill文件")

        except SkillLoadError:
            raise
        except Exception as e:
            logger.error(f"加载Skill文件失败: {e}")
            raise SkillLoadError(f"加载Skill文件失败: {e}")

    def _load_file(self, path: Path) -> str:
        """加载单个文件"""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def _update_cache(self, content: str, path: Path) -> None:
        """更新缓存"""
        self._cached_content = content
        self._cached_mtime = path.stat().st_mtime

    def clear_cache(self) -> None:
        """清除缓存"""
        self._cached_content = None
        self._cached_mtime = None


# 全局Skill加载器实例
skill_loader = SkillLoader()


def load_skill(force_reload: bool = False) -> str:
    """便捷函数：加载Skill内容"""
    return skill_loader.load(force_reload)


# ============================================================================
# 抽象生成器基类
# ============================================================================

class ContentGenerator(ABC):
    """内容生成器抽象基类"""

    # 平台默认模型
    DEFAULT_MODEL: str = ""
    # 平台名称
    PLATFORM_NAME: str = ""

    def __init__(self, config: GenerationConfig):
        self.config = config
        self.skill_content = load_skill()
        self._client = None
        self._setup_client()

    @abstractmethod
    def _setup_client(self) -> None:
        """设置API客户端"""
        pass

    @abstractmethod
    def _generate_internal(self, prompt: str) -> GenerationResult:
        """内部生成方法"""
        pass

    @property
    def model(self) -> str:
        """获取使用的模型名称"""
        return self.config.model or self.DEFAULT_MODEL

    def build_prompt(self) -> str:
        """构建提示词"""
        return f"""请用{self.config.style}风格，写一篇关于"{self.config.topic}"的文章，目标字数：{self.config.word_count}字。

要求：
1. 严格按照Skill中的方法论创作
2. 应用用户决策4次判断模型
3. 确保内容质量达到HKR评分标准
4. 字数控制在{self.config.word_count}字左右（误差±10%）
5. 前句建立相关性，前20行建立信任
6. 完整内容提供真价值，结尾展示利用价值

请直接输出文章内容，不需要额外的解释或说明。"""

    def generate(self) -> GenerationResult:
        """
        生成内容（带重试机制）

        Returns:
            GenerationResult: 生成结果

        Raises:
            APIError: 当API调用失败时
        """
        last_error = None
        prompt = self.build_prompt()

        for attempt in range(MAX_RETRIES):
            try:
                logger.info(f"调用 {self.PLATFORM_NAME} API (尝试 {attempt + 1}/{MAX_RETRIES})...")

                start_time = time.time()
                result = self._generate_internal(prompt)
                result.duration_seconds = time.time() - start_time

                logger.info(
                    f"{self.PLATFORM_NAME} API调用成功，"
                    f"生成内容长度: {len(result.content)}字，"
                    f"耗时: {result.duration_seconds:.2f}秒"
                )

                return result

            except Exception as e:
                last_error = e
                if attempt < MAX_RETRIES - 1:
                    wait_time = RETRY_DELAY * (2 ** attempt)  # 指数退避
                    logger.warning(f"API调用失败，{wait_time}秒后重试: {e}")
                    time.sleep(wait_time)
                else:
                    logger.error(f"API调用失败，已达最大重试次数: {e}")

        raise APIError(f"{self.PLATFORM_NAME} API调用失败: {last_error}")


# ============================================================================
# 具体平台生成器
# ============================================================================

class OpenAIGenerator(ContentGenerator):
    """OpenAI GPT生成器"""

    PLATFORM_NAME = "OpenAI"
    DEFAULT_MODEL = "gpt-4o"

    def _setup_client(self) -> None:
        try:
            from openai import OpenAI
            self._client = OpenAI(api_key=self.config.api_key)
        except ImportError:
            raise APIError("未安装openai库，请运行: pip install openai")

    def _generate_internal(self, prompt: str) -> GenerationResult:
        try:
            if self.config.stream:
                return self._generate_stream(prompt)

            response = self._client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.skill_content},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )

            content = response.choices[0].message.content or ""
            tokens_used = response.usage.total_tokens if response.usage else 0

            return GenerationResult(
                content=content,
                platform="openai",
                model=self.model,
                tokens_used=tokens_used,
                truncated=not response.choices[0].finish_reason == "stop"
            )

        except Exception as e:
            raise APIError(f"OpenAI API调用失败: {e}")

    def _generate_stream(self, prompt: str) -> GenerationResult:
        """流式生成"""
        print("\n[流式生成中...]\n")

        response = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.skill_content},
                {"role": "user", "content": prompt}
            ],
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            stream=True
        )

        content = ""
        tokens_used = 0

        for chunk in response:
            if chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                content += text
                print(text, end='', flush=True)

            if chunk.usage:
                tokens_used = chunk.usage.total_tokens

        print()  # 换行

        return GenerationResult(
            content=content,
            platform="openai",
            model=self.model,
            tokens_used=tokens_used
        )


class ClaudeGenerator(ContentGenerator):
    """Claude生成器"""

    PLATFORM_NAME = "Claude"
    DEFAULT_MODEL = "claude-sonnet-4-20250514"

    def _setup_client(self) -> None:
        try:
            import anthropic
            self._client = anthropic.Anthropic(api_key=self.config.api_key)
        except ImportError:
            raise APIError("未安装anthropic库，请运行: pip install anthropic")

    def _generate_internal(self, prompt: str) -> GenerationResult:
        try:
            if self.config.stream:
                return self._generate_stream(prompt)

            message = self._client.messages.create(
                model=self.model,
                max_tokens=self.config.max_tokens,
                system=self.skill_content,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            content = message.content[0].text
            tokens_used = message.usage.input_tokens + message.usage.output_tokens

            return GenerationResult(
                content=content,
                platform="claude",
                model=self.model,
                tokens_used=tokens_used
            )

        except Exception as e:
            raise APIError(f"Claude API调用失败: {e}")

    def _generate_stream(self, prompt: str) -> GenerationResult:
        """流式生成"""
        print("\n[流式生成中...]\n")

        with self._client.messages.stream(
            model=self.model,
            max_tokens=self.config.max_tokens,
            system=self.skill_content,
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            content = ""
            for text in stream.text_stream:
                content += text
                print(text, end='', flush=True)

        print()  # 换行

        message = stream.get_final_message()
        tokens_used = message.usage.input_tokens + message.usage.output_tokens

        return GenerationResult(
            content=content,
            platform="claude",
            model=self.model,
            tokens_used=tokens_used
        )


class GeminiGenerator(ContentGenerator):
    """Gemini生成器"""

    PLATFORM_NAME = "Gemini"
    DEFAULT_MODEL = "gemini-2.0-flash-exp"

    def _setup_client(self) -> None:
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.config.api_key)
            self._genai = genai
            self._model_client = genai.GenerativeModel(
                model_name=self.model,
                system_instruction=self.skill_content
            )
        except ImportError:
            raise APIError("未安装google-generativeai库，请运行: pip install google-generativeai")

    def _generate_internal(self, prompt: str) -> GenerationResult:
        try:
            response = self._model_client.generate_content(prompt)
            content = response.text

            # Gemini 不返回token使用情况，估算
            tokens_used = len(content) // 2  # 粗略估算

            return GenerationResult(
                content=content,
                platform="gemini",
                model=self.model,
                tokens_used=tokens_used
            )

        except Exception as e:
            raise APIError(f"Gemini API调用失败: {e}")


# ============================================================================
# 生成器工厂
# ============================================================================

GENERATOR_MAP: Dict[str, type[ContentGenerator]] = {
    'openai': OpenAIGenerator,
    'claude': ClaudeGenerator,
    'gemini': GeminiGenerator,
}


def create_generator(config: GenerationConfig) -> ContentGenerator:
    """
    创建生成器实例

    Args:
        config: 生成配置

    Returns:
        ContentGenerator: 生成器实例

    Raises:
        ValidationError: 当平台不支持时
    """
    generator_class = GENERATOR_MAP.get(config.platform)
    if generator_class is None:
        raise ValidationError(
            f"不支持的平台: {config.platform}，"
            f"支持的平台: {list(GENERATOR_MAP.keys())}"
        )
    return generator_class(config)


# ============================================================================
# 参数验证
# ============================================================================

def validate_parameters(
    topic: str,
    style: str,
    word_count: int,
    platform: str
) -> None:
    """
    验证输入参数

    Args:
        topic: 文章主题
        style: 写作风格
        word_count: 目标字数
        platform: AI平台

    Raises:
        ValidationError: 当参数无效时
    """
    # 验证主题
    if not topic or len(topic.strip()) == 0:
        raise ValidationError("主题不能为空")
    if len(topic) > 200:
        raise ValidationError("主题长度不能超过200字符")

    # 验证风格
    if style not in SUPPORTED_STYLES:
        logger.warning(f"使用自定义风格: {style}")

    # 验证字数
    if not isinstance(word_count, int):
        raise ValidationError("字数必须是整数")
    if word_count < MIN_WORD_COUNT:
        raise ValidationError(f"字数不能少于{MIN_WORD_COUNT}")
    if word_count > MAX_WORD_COUNT:
        raise ValidationError(f"字数不能超过{MAX_WORD_COUNT}")

    # 验证平台
    if platform not in SUPPORTED_PLATFORMS:
        raise ValidationError(f"不支持的平台: {platform}，支持的平台: {SUPPORTED_PLATFORMS}")

    logger.info(
        f"参数验证通过: topic={topic[:20]}..., "
        f"style={style}, words={word_count}, platform={platform}"
    )


# ============================================================================
# 内容保存
# ============================================================================

def save_output(
    content: str,
    output_path: Optional[str] = None,
    topic: str = "article"
) -> str:
    """
    保存生成的内容

    Args:
        content: 生成的内容
        output_path: 输出文件路径（可选）
        topic: 文章主题（用于自动命名）

    Returns:
        str: 保存的文件路径
    """
    try:
        if output_path:
            file_path = Path(output_path)
        else:
            # 自动生成文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_'))[:30]
            filename = f"{safe_topic}_{timestamp}.md"
            file_path = Path(filename)

        # 确保目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # 添加元数据头部
        metadata = f"""---
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
工具: 爆款内容生成器 v3.1
---

"""
        full_content = metadata + content

        # 保存文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        logger.info(f"内容已保存到: {file_path.absolute()}")
        return str(file_path.absolute())

    except Exception as e:
        logger.error(f"保存文件失败: {e}")
        raise


# ============================================================================
# 配置文件支持
# ============================================================================

def load_config() -> Dict[str, Any]:
    """
    加载配置文件

    Returns:
        Dict: 配置字典
    """
    if not CONFIG_PATH.exists():
        return {}

    try:
        import yaml
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f) or {}
        logger.info(f"已加载配置文件: {CONFIG_PATH}")
        return config
    except ImportError:
        logger.warning("未安装pyyaml，跳过配置文件加载")
        return {}
    except Exception as e:
        logger.warning(f"加载配置文件失败: {e}")
        return {}


# ============================================================================
# 主函数
# ============================================================================

def main() -> int:
    """
    主函数

    Returns:
        int: 退出码（0表示成功，非0表示失败）
    """
    parser = argparse.ArgumentParser(
        description='爆款内容生成器 - 命令行工具 v3.1',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本使用
  %(prog)s "AI工具使用技巧"

  # 指定风格和字数
  %(prog)s "AI工具使用技巧" --style 老司机风格 --words 6000

  # 使用Claude平台
  %(prog)s "AI工具使用技巧" --platform claude

  # 流式输出（实时显示生成过程）
  %(prog)s "AI工具使用技巧" --stream

  # 使用自定义模型
  %(prog)s "AI工具使用技巧" --platform claude --model claude-3-5-sonnet-20241022

  # 保存到指定文件
  %(prog)s "AI工具使用技巧" -o article.md

  # 完整示例
  %(prog)s "AI工具使用技巧" \\
    --style 老司机风格 \\
    --words 6000 \\
    --platform claude \\
    --stream \\
    --output article.md

支持的风格:
  """ + "\n  ".join(SUPPORTED_STYLES) + """

环境变量:
  OPENAI_API_KEY      - OpenAI API密钥
  ANTHROPIC_API_KEY   - Anthropic API密钥
  GOOGLE_API_KEY      - Google API密钥

配置文件:
  config.yaml - 在项目目录下创建配置文件，可设置默认值
        """
    )

    parser.add_argument(
        'topic',
        help='文章主题'
    )
    parser.add_argument(
        '--style',
        default='老司机风格',
        choices=SUPPORTED_STYLES,
        help='写作风格（默认: 老司机风格）'
    )
    parser.add_argument(
        '--words',
        type=int,
        default=6000,
        help=f'目标字数（默认: 6000，范围: {MIN_WORD_COUNT}-{MAX_WORD_COUNT}）'
    )
    parser.add_argument(
        '--platform',
        default='openai',
        choices=SUPPORTED_PLATFORMS,
        help='AI平台（默认: openai）'
    )
    parser.add_argument(
        '--model',
        help='指定模型（覆盖默认模型）'
    )
    parser.add_argument(
        '--api-key',
        help='API Key（或设置对应的环境变量）'
    )
    parser.add_argument(
        '--output', '-o',
        help='输出文件路径（不指定则自动生成）'
    )
    parser.add_argument(
        '--stream', '-s',
        action='store_true',
        help='启用流式输出（实时显示生成过程）'
    )
    parser.add_argument(
        '--max-tokens',
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help=f'最大token数（默认: {DEFAULT_MAX_TOKENS}）'
    )
    parser.add_argument(
        '--temperature', '-t',
        type=float,
        default=0.7,
        help='温度参数（0.0-1.0，默认: 0.7）'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 3.1.0'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='显示详细日志'
    )

    args = parser.parse_args()

    # 设置日志级别
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    try:
        # 加载配置文件
        config_file = load_config()
        # 命令行参数优先级高于配置文件
        api_key = args.api_key or config_file.get(f'{args.platform}_api_key')

        logger.info("=" * 60)
        logger.info("爆款内容生成器 v3.1 启动")
        logger.info("=" * 60)

        # 验证参数
        validate_parameters(args.topic, args.style, args.words, args.platform)

        # 获取API Key
        if not api_key:
            env_var_map = {
                'openai': 'OPENAI_API_KEY',
                'claude': 'ANTHROPIC_API_KEY',
                'gemini': 'GOOGLE_API_KEY'
            }
            env_var = env_var_map[args.platform]
            api_key = os.getenv(env_var)

            if not api_key:
                error_msg = f"错误：请提供API Key或设置环境变量 {env_var}"
                logger.error(error_msg)
                print(f"\n{error_msg}\n", file=sys.stderr)
                return 1

        # 创建生成配置
        config = GenerationConfig(
            topic=args.topic,
            style=args.style,
            word_count=args.words,
            platform=args.platform,
            api_key=api_key,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            stream=args.stream,
            output_path=args.output
        )

        # 创建生成器
        generator = create_generator(config)

        # 生成内容
        if not args.stream:
            print(f"\n正在使用 {args.platform} ({generator.model}) 生成内容...")
            print(f"主题：{args.topic}")
            print(f"风格：{args.style}")
            print(f"字数：{args.words}")
            print("-" * 60)

        result = generator.generate()

        # 保存内容
        output_path = save_output(result.content, args.output, args.topic)

        # 输出结果
        print("\n" + "=" * 60)
        print("✅ 生成成功！")
        print("=" * 60)
        print(f"文件路径: {output_path}")
        print(f"内容长度: {len(result.content)}字")
        if result.tokens_used > 0:
            print(f"Token使用: {result.tokens_used}")
        print(f"耗时: {result.duration_seconds:.2f}秒")
        if result.truncated:
            print("⚠️  内容可能被截断，尝试增加 --max-tokens 参数")
        print("=" * 60)

        # 如果没有指定输出文件，也打印内容预览
        if not args.output and not args.stream:
            print("\n内容预览：")
            print("-" * 60)
            preview = result.content[:500] + "..." if len(result.content) > 500 else result.content
            print(preview)
            print("-" * 60)

        logger.info("任务完成")
        return 0

    except ValidationError as e:
        logger.error(f"参数验证失败: {e}")
        print(f"\n❌ 参数错误: {e}\n", file=sys.stderr)
        return 1

    except SkillLoadError as e:
        logger.error(f"Skill加载失败: {e}")
        print(f"\n❌ Skill加载失败: {e}\n", file=sys.stderr)
        return 1

    except APIError as e:
        logger.error(f"API调用失败: {e}")
        print(f"\n❌ API调用失败: {e}\n", file=sys.stderr)
        return 1

    except KeyboardInterrupt:
        logger.warning("用户中断")
        print("\n\n⚠️  用户中断操作\n", file=sys.stderr)
        return 130

    except Exception as e:
        logger.exception(f"未预期的错误: {e}")
        print(f"\n❌ 发生错误: {e}\n", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())

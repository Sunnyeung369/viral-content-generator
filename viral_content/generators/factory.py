"""
生成器工厂

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from typing import Dict, Type, Optional

from viral_content.generators.base import ContentGenerator
from viral_content.generators.openai import OpenAIGenerator
from viral_content.generators.claude import ClaudeGenerator
from viral_content.generators.gemini import GeminiGenerator
from viral_content.models.generation import GenerationConfig
from viral_content.exceptions.custom import ValidationError


# 生成器映射表
GENERATOR_MAP: Dict[str, Type[ContentGenerator]] = {
    'openai': OpenAIGenerator,
    'claude': ClaudeGenerator,
    'gemini': GeminiGenerator,
}


def create_generator(
    platform: str = 'claude',
    api_key: Optional[str] = None,
    model: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 8192,
    config: Optional[GenerationConfig] = None,
    **kwargs
) -> ContentGenerator:
    """
    创建生成器实例（简化版）

    Args:
        platform: AI平台（openai/claude/gemini）
        api_key: API密钥
        model: 模型名称
        temperature: 温度参数
        max_tokens: 最大token数
        config: 完整配置对象（可选）
        **kwargs: 其他参数

    Returns:
        ContentGenerator: 生成器实例

    Raises:
        ValidationError: 当平台不支持时
    """
    if config is None:
        # 从参数创建配置
        config = GenerationConfig(
            topic="",  # 将在使用时设置
            platform=platform,
            api_key=api_key,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )

    generator_class = GENERATOR_MAP.get(config.platform)
    if generator_class is None:
        raise ValidationError(
            f"不支持的平台: {config.platform}，"
            f"支持的平台: {list(GENERATOR_MAP.keys())}"
        )
    return generator_class(config)


# 保留原始函数以向后兼容
def create_generator_from_config(config: GenerationConfig) -> ContentGenerator:
    """
    从配置对象创建生成器实例

    Args:
        config: 生成配置

    Returns:
        ContentGenerator: 生成器实例

    Raises:
        ValidationError: 当平台不支持时
    """
    return create_generator(config=config)


def register_generator(platform: str, generator_class: Type[ContentGenerator]) -> None:
    """
    注册新的生成器

    Args:
        platform: 平台名称
        generator_class: 生成器类
    """
    GENERATOR_MAP[platform] = generator_class

"""
Viral Content Generator v4.0
热点风格成交引擎

作者: Sunnyeung
版本: 4.0.1
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

__version__ = "4.0.1"
__author__ = "Sunnyeung"

# 核心模块
# 配置
from .config import Settings, get_settings
from .core import (
    AccountFingerprint,
    ConversionFunnel,
    ConversionGoal,
    PipelineBuilder,
    PlatformAdapter,
    PromptCompiler,
    StyleMixer,
    ViralContentPipeline,
)
from .core.platform_adapter import ContentPlatform as Platform

# 数据模型
from .models import (
    Account,
    GenerationConfig,
    GenerationResult,
    Offer,
    StyleProfile,
    Trend,
)

# 工具
from .utils import FileHandler, Validator, YamlFileLoader

__all__ = [
    # 版本
    "__version__",
    "__author__",
    # 核心流程
    "ViralContentPipeline",
    "PipelineBuilder",
    # 核心模块
    "PromptCompiler",
    "AccountFingerprint",
    "StyleMixer",
    "ConversionFunnel",
    "PlatformAdapter",
    "ConversionGoal",
    # 数据模型
    "GenerationConfig",
    "GenerationResult",
    "Account",
    "Offer",
    "Trend",
    "StyleProfile",
    "Platform",
    # 配置
    "get_settings",
    "Settings",
    # 工具
    "FileHandler",
    "YamlFileLoader",
    "Validator",
]

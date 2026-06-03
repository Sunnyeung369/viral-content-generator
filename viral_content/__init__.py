"""
Viral Content Generator v4.0
热点风格成交引擎

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

__version__ = "4.0.0"
__author__ = "Sunnyeung"

# 核心模块
from .core import (
    ViralContentPipeline,
    PipelineBuilder,
    PromptCompiler,
    AccountFingerprint,
    StyleMixer,
    ConversionFunnel,
    PlatformAdapter,
    ConversionGoal,
)

# 数据模型
from .models import (
    GenerationConfig,
    GenerationResult,
    Account,
    Offer,
    Trend,
    StyleProfile,
    Platform,
)

# 配置
from .config import get_settings, Settings

# 工具
from .utils import FileHandler, YamlFileLoader, Validator

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

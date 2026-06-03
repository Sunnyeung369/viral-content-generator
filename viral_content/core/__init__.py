"""
核心引擎模块
v4.0

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from .prompt_compiler import PromptCompiler, get_compiler
from .account_fingerprint import AccountFingerprint, load_account
from .style_mixer import StyleMixer, get_style_mixer
from .conversion_funnel import (
    ConversionFunnel,
    ConversionGoal,
    ContentStructure,
    create_conversion_funnel,
)
from .platform_adapter import (
    PlatformAdapter,
    ContentPlatform,
    PlatformSpec,
    PlatformPackage,
    get_platform_adapter,
)

__all__ = [
    # Prompt Compiler
    "PromptCompiler",
    "get_compiler",
    # Account Fingerprint
    "AccountFingerprint",
    "load_account",
    # Style Mixer
    "StyleMixer",
    "get_style_mixer",
    # Conversion Funnel
    "ConversionFunnel",
    "ConversionGoal",
    "ContentStructure",
    "create_conversion_funnel",
    # Platform Adapter
    "PlatformAdapter",
    "ContentPlatform",
    "PlatformSpec",
    "PlatformPackage",
    "get_platform_adapter",
]

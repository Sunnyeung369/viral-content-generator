"""
核心引擎模块
v4.0

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from .account_fingerprint import AccountFingerprint, load_account
from .conversion_funnel import (
    ContentStructure,
    ConversionFunnel,
    ConversionGoal,
    create_conversion_funnel,
)
from .pipeline import PipelineBuilder, ViralContentPipeline
from .platform_adapter import (
    ContentPlatform,
    PlatformAdapter,
    PlatformPackage,
    PlatformSpec,
    get_platform_adapter,
)
from .prompt_compiler import PromptCompiler, get_compiler
from .style_mixer import StyleMixer, get_style_mixer

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
    # Pipeline
    "ViralContentPipeline",
    "PipelineBuilder",
]

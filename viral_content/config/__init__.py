"""
配置模块
v4.0
"""

from .constants import (
    # 风格分类
    STYLE_CATEGORIES,
    # 平台规格
    PLATFORM_SPECS,
    # 成交目标类型
    CONVERSION_GOALS,
    # 内容类型
    CONTENT_TYPES,
)
from .settings import Settings, get_settings, reload_settings

__all__ = [
    # Constants
    "STYLE_CATEGORIES",
    "PLATFORM_SPECS",
    "CONVERSION_GOALS",
    "CONTENT_TYPES",
    # Settings
    "Settings",
    "get_settings",
    "reload_settings",
]

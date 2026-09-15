"""
配置模块
v4.0
"""

from .constants import (
    # 成交目标类型
    CONVERSION_GOALS,
    # 风格分类
    STYLE_CATEGORIES,
)
from .settings import Settings, get_settings, reload_settings

__all__ = [
    # Constants
    "STYLE_CATEGORIES",
    "CONVERSION_GOALS",
    # Settings
    "Settings",
    "get_settings",
    "reload_settings",
]

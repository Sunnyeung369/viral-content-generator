"""
配置模块
v4.0
"""

from .constants import (
    # 风格分类
    STYLE_CATEGORIES,
    # 成交目标类型
    CONVERSION_GOALS,
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

"""
热点来源模块
v4.0
"""

from .douyin import DouyinTrendSource
from .google_trends import GoogleTrendsSource
from .tiktok import TikTokTrendSource
from .xiaohongshu import XiaohongshuTrendSource

__all__ = [
    "DouyinTrendSource",
    "GoogleTrendsSource",
    "TikTokTrendSource",
    "XiaohongshuTrendSource",
]

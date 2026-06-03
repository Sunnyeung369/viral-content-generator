"""
数据模型模块

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from .generation import (
    GenerationConfig,
    GenerationResult,
    GenerationRequest,
    GenerationOutput
)
from .account import Account, AccountFingerprint
from .offer import Offer, OfferConfig
from .style import Style, StyleDNA, StyleMix
from .trend import Trend, TrendItem, TrendMetrics

__all__ = [
    # Generation
    'GenerationConfig',
    'GenerationResult',
    'GenerationRequest',
    'GenerationOutput',
    # Account
    'Account',
    'AccountFingerprint',
    # Offer
    'Offer',
    'OfferConfig',
    # Style
    'Style',
    'StyleDNA',
    'StyleMix',
    # Trend
    'Trend',
    'TrendItem',
    'TrendMetrics',
]

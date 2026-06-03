"""
评分系统模块
v4.0 - 爆款成交评分器

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from .base import BaseScorer, CompositeScorer, ScoreResult, ScoreLevel
from .hook_scorer import HookScorer
from .trust_scorer import TrustScorer
from .value_scorer import ValueScorer
from .interaction_scorer import InteractionScorer
from .conversion_scorer import ConversionScorer
from .compliance_scorer import ComplianceScorer
from .trend_fit_scorer import TrendFitScorer, TrendInfo, AccountInfo

__all__ = [
    # 基类
    "BaseScorer",
    "CompositeScorer",
    "ScoreResult",
    "ScoreLevel",
    # 专项评分器
    "HookScorer",
    "TrustScorer",
    "ValueScorer",
    "InteractionScorer",
    "ConversionScorer",
    "ComplianceScorer",
    # 匹配评分器
    "TrendFitScorer",
    "TrendInfo",
    "AccountInfo",
]

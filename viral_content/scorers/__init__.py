"""
评分系统模块
v4.0 - 爆款成交评分器

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from .base import BaseScorer, CompositeScorer, ScoreResult, ScoreLevel

class QualityScorer:
    """对外兼容的综合质量评分器。"""
    def __init__(self, scorers=None):
        self.scorers = scorers or [HookScorer(), TrustScorer(), ValueScorer(), ComplianceScorer()]
    def score_all(self, content, **context):
        return {s.name: s.score(content, context) for s in self.scorers}
    def get_improvement_suggestions(self, scores):
        return [tip for result in scores.values() for tip in result.suggestions]

ScoringResult = ScoreResult
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
    "QualityScorer",
    "ScoringResult",
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

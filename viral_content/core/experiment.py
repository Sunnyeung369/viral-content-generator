"""Candidate experiments and outcome feedback models."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

@dataclass
class Candidate:
    content: str
    quality_score: float
    passed_gate: bool
    index: int = 0
    metadata: Dict[str, object] = field(default_factory=dict)

@dataclass
class FeedbackRecord:
    candidate_index: int
    platform: str
    published_at: str
    impressions: Optional[int] = None
    views: Optional[int] = None
    comments: Optional[int] = None
    leads: Optional[int] = None
    conversions: Optional[int] = None
    source: str = "manual"

    def to_dict(self) -> Dict[str, object]:
        return {k: v for k, v in self.__dict__.items()}

class CandidateRanker:
    """Explainable ranking with goal-specific weights."""
    DEFAULT_WEIGHTS = {"likes": (0.55, 0.45), "comments": (0.50, 0.50), "leads": (0.40, 0.60), "sales": (0.35, 0.65)}
    PLATFORM_BIAS = {"douyin": 0.15, "xiaohongshu": 0.10, "bilibili": 0.05, "wechat": 0.0, "zhihu": -0.05}
    def __init__(self, goal: str = "leads", platform: str = "wechat", weights: Optional[tuple] = None):
        self.goal = goal
        bias = self.PLATFORM_BIAS.get(platform, 0.0)
        base_quality, base_gate = weights or self.DEFAULT_WEIGHTS.get(goal, (0.5, 0.5))
        self.quality_weight = min(0.8, max(0.2, base_quality + bias))
        self.gate_weight = 1.0 - self.quality_weight
    def describe(self) -> Dict[str, object]:
        return {"goal": self.goal, "quality_weight": self.quality_weight, "gate_weight": self.gate_weight}

    def rank(self, candidates: List[Candidate]) -> List[Candidate]:
        return sorted(candidates, key=lambda c: self.quality_weight * c.quality_score + self.gate_weight * (10.0 if c.passed_gate else 0.0), reverse=True)


@dataclass
class ExperimentSummary:
    platform: str
    sample_size: int
    winner_index: Optional[int]
    metrics: Dict[int, Dict[str, float]]
    reliable: bool
    note: str

def summarize_feedback(records: List[FeedbackRecord], min_samples: int = 3) -> ExperimentSummary:
    if not records:
        return ExperimentSummary("unknown", 0, None, {}, False, "暂无发布反馈")
    platform = records[0].platform
    metrics = {}
    for r in records:
        denom = max(r.impressions or r.views or 0, 1)
        metrics[r.candidate_index] = {
            "engagement_rate": ((r.comments or 0) / denom) * 100,
            "lead_rate": ((r.leads or 0) / denom) * 100,
            "conversion_rate": ((r.conversions or 0) / denom) * 100,
        }
    def key(item):
        m=item[1]; return (m["conversion_rate"], m["lead_rate"], m["engagement_rate"])
    winner = max(metrics.items(), key=key)[0] if metrics else None
    reliable = len(records) >= min_samples
    note = "样本量达到最低建议值" if reliable else f"样本量不足，建议至少收集 {min_samples} 条记录"
    return ExperimentSummary(platform, len(records), winner, metrics, reliable, note)

"""Candidate experiments and outcome feedback models."""
import json
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Candidate:
    content: str
    quality_score: float
    passed_gate: bool
    index: int = 0
    metadata: dict[str, object] = field(default_factory=dict)

@dataclass
class FeedbackRecord:
    candidate_index: int
    platform: str
    published_at: str
    impressions: int | None = None
    views: int | None = None
    comments: int | None = None
    leads: int | None = None
    conversions: int | None = None
    source: str = "manual"

    def to_dict(self) -> dict[str, object]:
        return {k: v for k, v in self.__dict__.items()}

class CandidateRanker:
    """Explainable ranking with goal-specific weights."""
    DEFAULT_WEIGHTS: ClassVar[dict[str, tuple[float, float]]] = {"likes": (0.55, 0.45), "comments": (0.50, 0.50), "leads": (0.40, 0.60), "sales": (0.35, 0.65)}
    PLATFORM_BIAS: ClassVar[dict[str, float]] = {"douyin": 0.15, "xiaohongshu": 0.10, "bilibili": 0.05, "wechat": 0.0, "zhihu": -0.05}
    def __init__(self, goal: str = "leads", platform: str = "wechat", weights: tuple | None = None):
        self.goal = goal
        bias = self.PLATFORM_BIAS.get(platform, 0.0)
        base_quality, _ = weights or self.DEFAULT_WEIGHTS.get(goal, (0.5, 0.5))
        self.quality_weight = min(0.8, max(0.2, base_quality + bias))
        self.gate_weight = 1.0 - self.quality_weight
    def describe(self) -> dict[str, object]:
        return {"goal": self.goal, "quality_weight": self.quality_weight, "gate_weight": self.gate_weight}

    def rank(self, candidates: list[Candidate]) -> list[Candidate]:
        return sorted(candidates, key=lambda c: self.quality_weight * c.quality_score + self.gate_weight * (10.0 if c.passed_gate else 0.0), reverse=True)


@dataclass
class ExperimentSummary:
    platform: str
    sample_size: int
    winner_index: int | None
    metrics: dict[int, dict[str, float]]
    reliable: bool
    note: str

def summarize_feedback(records: list[FeedbackRecord], min_samples: int = 3) -> ExperimentSummary:
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


def export_feedback_report(records: list[FeedbackRecord], path: str, min_samples: int = 3) -> ExperimentSummary:
    """Write a portable JSON report and return its summary."""
    summary = summarize_feedback(records, min_samples=min_samples)
    payload = {
        "summary": {"platform": summary.platform, "sample_size": summary.sample_size, "winner_index": summary.winner_index, "metrics": summary.metrics, "reliable": summary.reliable, "note": summary.note},
        "records": [r.to_dict() for r in records],
    }
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    return summary

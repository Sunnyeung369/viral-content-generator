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
    def __init__(self, goal: str = "leads", weights: Optional[tuple] = None):
        self.goal = goal
        self.quality_weight, self.gate_weight = weights or self.DEFAULT_WEIGHTS.get(goal, (0.5, 0.5))
    def rank(self, candidates: List[Candidate]) -> List[Candidate]:
        return sorted(candidates, key=lambda c: self.quality_weight * c.quality_score + self.gate_weight * (10.0 if c.passed_gate else 0.0), reverse=True)

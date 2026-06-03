"""
热点数据模型

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class TrendMetrics:
    """热点指标"""
    heat_score: float = 0.0  # 热度分 (0-100)
    discussion_count: int = 0  # 讨论量
    timestamp: Optional[str] = None
    growth_rate: float = 0.0  # 增长率


@dataclass
class TrendItem:
    """热点条目"""
    id: str = ""
    topic: str = ""
    description: str = ""
    source: str = ""
    url: str = ""
    metrics: TrendMetrics = field(default_factory=TrendMetrics)
    keywords: List[str] = field(default_factory=list)
    category: str = ""

    # 评分结果
    account_fit_score: float = 0.0
    conversion_score: float = 0.0
    risk_score: float = 0.0

    # 推荐角度
    recommended_angle: str = ""
    recommended_platforms: List[str] = field(default_factory=list)

    # 元数据
    metadata: Dict[str, Any] = field(default_factory=dict)


# 简化别名
Trend = TrendItem

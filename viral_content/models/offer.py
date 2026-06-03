"""
产品服务数据模型

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


@dataclass
class OfferConfig:
    """产品服务配置"""
    # 基本信息
    name: str = ""
    type: str = "consulting"  # consulting, course, product, service
    category: str = ""

    # 价格阶梯
    pricing: Dict[str, str] = field(default_factory=dict)

    # 核心卖点
    unique_value_proposition: List[str] = field(default_factory=list)

    # 成交门槛
    commitment_required: Dict[str, str] = field(default_factory=dict)

    # 目标客户匹配
    ideal_customer_profile: List[str] = field(default_factory=list)

    # 转化路径
    conversion_path: Dict[str, Any] = field(default_factory=dict)

    # 信任背书
    social_proof: Dict[str, List] = field(default_factory=dict)

    # 元数据
    metadata: Dict[str, Any] = field(default_factory=dict)


# 简化别名
Offer = OfferConfig

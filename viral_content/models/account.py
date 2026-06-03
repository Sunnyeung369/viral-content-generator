"""
账号指纹数据模型

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


@dataclass
class AccountFingerprint:
    """账号指纹配置"""
    # 基本信息
    name: str = ""
    identity: str = ""  # 专业定位（一句话）

    # 目标用户
    target_audience: List[str] = field(default_factory=list)

    # 用户痛点
    pain_points: List[str] = field(default_factory=list)

    # 权威资产
    authority_assets: List[str] = field(default_factory=list)

    # 商业目标
    business_goal: Dict[str, Any] = field(default_factory=dict)

    # 产品阶梯
    offer_ladder: Dict[str, str] = field(default_factory=dict)

    # 语气限制
    tone_constraints: List[str] = field(default_factory=list)

    # 内容限制
    content_constraints: List[str] = field(default_factory=list)

    # 平台偏好
    platform_preferences: Dict[str, List[str]] = field(default_factory=dict)

    # 元数据
    metadata: Dict[str, Any] = field(default_factory=dict)


# 简化别名
Account = AccountFingerprint

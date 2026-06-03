"""
生成配置和结果数据模型

作者: Sunnyeung
版本: 4.0.0
许可: MIT License
GitHub: https://github.com/Sunnyeung369/viral-content-generator
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from pathlib import Path


@dataclass
class GenerationConfig:
    """生成配置（v4.0 扩展版）"""
    # 基础参数（v3.1 兼容）
    topic: str
    style: str = '老司机风格'
    word_count: int = 6000
    platform: str = 'openai'  # AI 平台
    api_key: Optional[str] = None
    model: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 16384
    stream: bool = False
    output_path: Optional[str] = None

    # v4.0 新增参数
    account_path: Optional[str] = None  # 账号配置文件路径
    offer_path: Optional[str] = None  # 产品配置文件路径
    goal: str = 'likes'  # 成交目标: likes, comments, leads, sales, consult
    content_platforms: List[str] = field(default_factory=list)  # 内容输出平台
    style_mix: Optional[str] = None  # 风格混合 (如: "global:tech_explainer,china:business_savage")
    variants: int = 1  # 生成变体数量

    # 热点输入（手动或自动）
    trend_input: Optional[str] = None  # 热点输入（JSON/YAML 字符串）
    trend_file: Optional[str] = None  # 热点文件路径

    # 评分选项
    enable_scoring: bool = False  # 是否启用自动评分
    show_revision_advice: bool = True  # 是否显示修改建议

    # 输出选项
    save_all_variants: bool = False  # 是否保存所有变体
    output_format: str = 'markdown'  # 输出格式: markdown, json, html


@dataclass
class GenerationResult:
    """生成结果（v4.0 扩展版）"""
    content: str
    platform: str  # AI 平台
    model: str
    tokens_used: int = 0
    duration_seconds: float = 0.0
    truncated: bool = False

    # v4.0 新增字段
    variant_index: int = 0  # 变体索引
    content_platform: Optional[str] = None  # 内容输出平台
    goal: Optional[str] = None  # 成交目标

    # 评分结果
    scores: Optional[Dict[str, float]] = None
    revision_advice: Optional[List[str]] = None

    # 元数据
    metadata: Dict[str, Any] = field(default_factory=dict)

    # 保存路径
    saved_path: Optional[str] = None


@dataclass
class GenerationRequest:
    """生成请求（用于 Pipeline）"""
    config: GenerationConfig
    account: Optional['Account'] = None
    offer: Optional['Offer'] = None
    styles: Optional[List['Style']] = None
    trends: Optional[List['Trend']] = None

    # 编译后的提示词
    compiled_prompt: Optional[str] = None


@dataclass
class GenerationOutput:
    """生成输出（多平台/多变体）"""
    request: GenerationRequest
    results: List[GenerationResult]

    # 汇总信息
    total_tokens_used: int = 0
    total_duration: float = 0.0
    average_score: float = 0.0

    # 输出目录
    output_dir: Optional[Path] = None

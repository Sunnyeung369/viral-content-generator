"""Deterministic pre-publish checks for generated content."""
from dataclasses import dataclass
import re
from typing import List

@dataclass
class QualityGateResult:
    passed: bool
    warnings: List[str]

class QualityGate:
    PLACEHOLDER = re.compile(r"\[[^\]]+\]|\{\{[^}]+\}\}|TODO|TBD", re.I)
    OVERCLAIM = re.compile(r"保证(爆款|第一|100%|稳赚)|零风险|绝对有效", re.I)
    def check(self, content: str, *, require_cta: bool = False) -> QualityGateResult:
        warnings=[]
        if not content or len(content.strip()) < 80: warnings.append("内容过短，无法完成有效审核")
        if self.PLACEHOLDER.search(content or ""): warnings.append("仍含占位符或待办标记")
        if self.OVERCLAIM.search(content or ""): warnings.append("包含未经证实的绝对化承诺")
        if require_cta and not re.search(r"评论|私信|了解|领取|咨询|购买|行动", content or ""): warnings.append("缺少清晰的下一步行动")
        return QualityGateResult(not warnings, warnings)

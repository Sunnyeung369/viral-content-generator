"""Create a validated starter style card."""

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new style card template")
    parser.add_argument("id", help="lowercase style identifier, e.g. founder_story")
    parser.add_argument("--label", required=True)
    parser.add_argument("--category", default="custom")
    parser.add_argument("--output", type=Path, default=Path("data/styles"))
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9_]+", args.id):
        parser.error("id 只能包含小写字母、数字和下划线")
    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / f"{args.id}.yaml"
    if path.exists():
        parser.error(f"文件已存在: {path}")
    path.write_text(
        f'''id: {args.id}\nlabel: "{args.label}"\ncategory: "{args.category}"\nstyle_dna:\n  tone: "清晰、具体"\n  sentence_rhythm: "短句为主"\nhook_patterns:\n  - "一个可验证的开头"\nlogic_patterns:\n  - "问题 -> 证据 -> 行动"\nemotion_curve: ["好奇", "理解", "行动"]\navoid:\n  - "绝对化承诺"\nconversion_fit:\n  - "leads"\n''',
        encoding="utf-8",
    )
    print(f"Created {path}. Run scripts/validate_config.py to verify it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Validate a YAML account, offer, or style configuration before generation."""

import argparse
from pathlib import Path
from typing import Any

import yaml


REQUIRED = {
    "account": ("name", "identity"),
    "offer": ("name", "type"),
    "style": ("id", "label", "style_dna"),
}


def validate(path: Path, kind: str) -> list[str]:
    data: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return ["顶层内容必须是 YAML 对象"]
    target = data.get(kind, data)
    if kind == "style" and isinstance(data.get("styles"), list):
        target = data["styles"][0] if data["styles"] else {}
    if not isinstance(target, dict):
        return [f"未找到 {kind} 对象"]
    return [f"缺少字段: {field}" for field in REQUIRED[kind] if field not in target]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate project YAML configuration")
    parser.add_argument("path", type=Path)
    parser.add_argument("--kind", choices=sorted(REQUIRED), required=True)
    args = parser.parse_args()
    errors = validate(args.path, args.kind)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {args.kind} configuration {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

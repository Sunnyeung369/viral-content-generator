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
    targets = data.get("styles", []) if kind == "style" else [target]
    if not isinstance(targets, list):
        targets = [targets]
    errors: list[str] = []
    for index, item in enumerate(targets, start=1):
        if not isinstance(item, dict):
            errors.append(f"第 {index} 项不是对象")
            continue
        errors.extend(
            f"第 {index} 项缺少字段: {field}"
            for field in REQUIRED[kind]
            if field not in item
        )
    return errors


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

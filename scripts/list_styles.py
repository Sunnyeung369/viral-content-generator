"""List available style card IDs from bundled YAML libraries."""

from pathlib import Path

import yaml


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "data" / "styles"
    count = 0
    for path in sorted(root.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        styles = data.get("styles", []) if isinstance(data, dict) else []
        for style in styles:
            if isinstance(style, dict) and style.get("id"):
                print(f"{style['id']}\t{style.get('label', '')}")
                count += 1
    print(f"Total: {count} styles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

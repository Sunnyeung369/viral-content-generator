"""Small consistency checks for documentation examples."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_FILES = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / "examples").glob("*.md"))]


def main() -> int:
    text = "\n".join(path.read_text(encoding="utf-8") for path in TEXT_FILES)
    forbidden = ("--platforms ", "global:tech_explainer", "china:business_savage")
    errors = [token for token in forbidden if token in text]
    if errors:
        print("Outdated documentation tokens:", ", ".join(errors))
        return 1
    required = ("examples/local_demo.py", "CHANGELOG.md", "CITATION.cff")
    missing = [path for path in required if path not in text]
    if missing:
        print("Missing discoverability links:", ", ".join(missing))
        return 1
    print(f"Documentation checks passed ({len(TEXT_FILES)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

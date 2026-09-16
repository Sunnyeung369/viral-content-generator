"""Fail when common API key patterns are present in tracked text files."""

import re
import subprocess


PATTERNS = (re.compile(r"sk-[A-Za-z0-9]{20,}"), re.compile(r"AIza[A-Za-z0-9_-]{20,}"))


def main() -> int:
    files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
    hits = []
    for name in files:
        if name.endswith(('.pyc', '.png', '.jpg', '.gif')):
            continue
        try:
            with open(name, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError):
            continue
        if any(pattern.search(text) for pattern in PATTERNS):
            hits.append(name)
    if hits:
        print("Possible secrets found:", ", ".join(hits))
        return 1
    print("Secret scan passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

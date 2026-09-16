# Viral Content Generator

An experiment-ready workflow for turning one topic into platform-aware content drafts.

**Topic + account fingerprint + style constraints + conversion goal = testable drafts**

## Why fork this project?

- Run a deterministic local demo without an API key: `python examples/local_demo.py`.
- Keep accounts, offers, styles and prompts in editable YAML/Markdown files.
- Generate multiple candidates, apply a deterministic quality gate, and rank them with explainable weights.
- Record real publishing feedback and iterate on one variable at a time.

This project does not promise viral reach or sales. It provides a repeatable workflow for testing content ideas.

## Quick start

```bash
pip install -r requirements.txt
python viral_content_cli.py --topic "AI agent workflow" --goal leads --platform xiaohongshu --variants 3 --score
```

See the [Chinese README](./README.md), [30-second demo](./examples/30-second-demo.md), [case study](./examples/case-study.md), and [v4.1 roadmap](./docs/v4.1-roadmap.md).

## Contributing

Start with [GOOD_FIRST_ISSUE.md](./GOOD_FIRST_ISSUE.md), use the issue and PR templates, and run `python -m pytest -q` before submitting changes.

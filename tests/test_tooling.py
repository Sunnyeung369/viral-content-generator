import subprocess
import sys


def test_list_styles_reports_bundled_cards():
    result = subprocess.run(
        [sys.executable, "scripts/list_styles.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Total: 155 styles" in result.stdout


def test_validate_config_accepts_default_account():
    result = subprocess.run(
        [
            sys.executable,
            "scripts/validate_config.py",
            "data/accounts/default_account.yaml",
            "--kind",
            "account",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "OK: account configuration" in result.stdout

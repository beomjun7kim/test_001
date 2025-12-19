"""Top-level shim delegating to package `test_001`.

This keeps `python main.py` working while the real implementation lives
in `test_001/main.py`.
"""
from test_001.main import _main


if __name__ == "__main__":
    raise SystemExit(_main())

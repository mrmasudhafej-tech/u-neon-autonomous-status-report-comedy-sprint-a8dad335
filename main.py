"""Status Report Comedy Sprint: write one funny status line, exactly as-is.

The line is deliberately deadpan — a tiny crypto claim filed as a
profitable week — and it is written with no trailing newline.
"""

import os
from pathlib import Path

LINE = "Weekly status: I claimed 150 PXIO for 0.0000083 BNB in gas, noted it is worth about two cents, and filed the week as profitable anyway."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "LINE must be 1-200 characters"
    assert LINE.strip(), "LINE must not be only whitespace"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

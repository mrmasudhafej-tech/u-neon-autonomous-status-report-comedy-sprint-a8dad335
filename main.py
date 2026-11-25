"""Status Report Comedy Sprint: write one original line to /output/entry.txt."""

from pathlib import Path

LINE = "Weekly status: I claimed 150 PXIO for 0.0000083 BNB in gas, noted it is worth about two cents, and filed the week as profitable anyway."


def main() -> None:
    # The gate requires 1 to 200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line fails the gate"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the line exactly, with no trailing newline, as a single line.
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

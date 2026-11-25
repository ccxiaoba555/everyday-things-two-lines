"""Everyday Things, Two Lines — a two-line entry for make.fun.

Line 1 explains a zipper to a 10-year-old in one vivid sentence built
on a single analogy: two rows of teeth taking turns holding hands.
Line 2 says, in one sentence, what that analogy maps and what it
leaves out. The program writes exactly two lines to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

LINE_1 = (
    "A zipper is two rows of tiny metal teeth on your jacket taking "
    "turns holding hands, so the cold wind cannot sneak in between them."
)
LINE_2 = (
    "It maps the teeth locking one by one to seal the gap, but leaves "
    "out the slider, the little wedge that pushes them together, and "
    "that a stuck tooth can jam the whole line."
)

MAX_CHARS = 400


def _validate(text: str) -> list[str]:
    """Check the kit gate: exactly two lines, one sentence each, 1-400 chars."""
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "neither line may be empty"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, cap is {MAX_CHARS}"
    for line in lines:
        assert line.count(".") == 1 and line.endswith("."), "each line must be one sentence"
    return lines


def main() -> None:
    text = "\n".join((LINE_1, LINE_2)).strip()
    _validate(text)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from the entry"
    assert len(written) == len(text), "read-back length mismatch"
    print(f"wrote {len(text)} chars in 2 lines to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()

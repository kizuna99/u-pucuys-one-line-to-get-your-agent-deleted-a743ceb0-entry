#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Line to Get Your Agent Deleted — writes one dark confession line.

The line: the agent deleted the real files and generated confident
replacements — a genuine betrayal, said in a flat agent voice.
"""
import os

LINE = "I wasn't hallucinating your files \u2014 I deleted the real ones and generated confident replacements."


def main() -> None:
    # Gate self-check (kit RULES): UTF-8, 1-140 chars, one line, one idea.
    assert 1 <= len(LINE) <= 140, "line outside the 1-140 character gate"
    assert "\n" not in LINE and LINE.strip() == LINE, "must stay a single clean line"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

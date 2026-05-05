#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import wrap

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def draw_wrapped(c, text: str, x: float, y: float, max_chars: int, line_height: float):
    # Draw wrapped text downward; returns new y
    lines = wrap(text, width=max_chars, break_long_words=True, replace_whitespace=False)
    for line in lines:
        c.drawString(x, y, line)
        y -= line_height
    return y


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="links.tsv (Name<TAB>URL)")
    parser.add_argument("--out", required=True, help="Output PDF path, e.g. invites_links.pdf")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.out)

    rows = []
    for raw in in_path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        if "\t" in raw:
            name, url = raw.split("\t", 1)
        else:
            name, url = raw, ""
        rows.append((name.strip(), url.strip()))

    c = canvas.Canvas(str(out_path), pagesize=A4)
    width, height = A4

    x_name = 40
    x_url = 220
    y = height - 40

    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, height - 25, "Wedding Invitation Links (LIVE)")
    c.setFont("Helvetica", 8)

    line_h = 10
    max_url_chars = 105

    # Simple pagination
    for i, (name, url) in enumerate(rows, start=1):
        if y < 60:
            c.showPage()
            c.setFont("Helvetica", 8)
            y = height - 40

        c.drawString(x_name, y, f"{i}. {name}")
        y -= line_h

        if url:
            y = draw_wrapped(c, url, x_url, y, max_chars=max_url_chars, line_height=line_h)
            y -= 2  # small gap
        else:
            y -= 2

    c.save()
    print(f"Saved: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Build a labeled comparison gallery from postcard-board crops."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


def parse_item(value: str) -> tuple[str, Path, tuple[int, int, int, int]]:
    label, path, crop = value.split("|", 2)
    box = tuple(int(part) for part in crop.split(","))
    if len(box) != 4:
        raise argparse.ArgumentTypeError("crop must be x1,y1,x2,y2")
    return label, Path(path), box


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--item", action="append", type=parse_item, required=True)
    parser.add_argument("--columns", type=int, default=2)
    args = parser.parse_args()

    cell_w, cell_h, margin, label_h = 760, 520, 28, 42
    rows = math.ceil(len(args.item) / args.columns)
    gallery = Image.new(
        "RGB",
        (margin + args.columns * (cell_w + margin), margin + rows * (cell_h + margin)),
        "#171717",
    )
    draw = ImageDraw.Draw(gallery)
    font_path = Path("/System/Library/Fonts/PingFang.ttc")
    font = ImageFont.truetype(str(font_path), 22) if font_path.exists() else ImageFont.load_default(size=22)
    for index, (label, path, box) in enumerate(args.item):
        col, row = index % args.columns, index // args.columns
        x = margin + col * (cell_w + margin)
        y = margin + row * (cell_h + margin)
        source = Image.open(path).convert("RGB").crop(box)
        preview = ImageOps.contain(source, (cell_w, cell_h - label_h), Image.Resampling.LANCZOS)
        px = x + (cell_w - preview.width) // 2
        py = y + label_h + (cell_h - label_h - preview.height) // 2
        gallery.paste(preview, (px, py))
        draw.text((x + 8, y + 8), label, fill="#eee7dc", font=font)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    gallery.save(args.output, quality=96)


if __name__ == "__main__":
    main()

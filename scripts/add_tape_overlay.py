#!/usr/bin/env python3
"""Add restrained, repeatable torn-paper tape overlays to a raster board."""

from __future__ import annotations

import argparse
import random
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFilter


def parse_tape(value: str) -> tuple[float, float, int, int, float, str, int]:
    parts = value.split(",")
    if len(parts) != 7:
        raise argparse.ArgumentTypeError(
            "tape must be center_x,center_y,width,height,angle,color,opacity"
        )
    x, y, width, height, angle, color, opacity = parts
    return float(x), float(y), int(width), int(height), float(angle), color, int(opacity)


def make_tape(width: int, height: int, color: str, opacity: int, seed: int) -> Image.Image:
    rng = random.Random(seed)
    pad = max(12, height // 2)
    canvas = Image.new("RGBA", (width + pad * 2, height + pad * 2), (0, 0, 0, 0))
    body = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(body)
    left = pad
    right = pad + width
    top = pad
    bottom = pad + height
    step = max(5, height // 4)
    points = []
    y = top
    while y <= bottom:
        points.append((left + rng.randint(-4, 4), y))
        y += step
    points.extend([(right + rng.randint(-4, 4), y) for y in range(bottom, top - 1, -step)])
    rgb = ImageColor.getrgb(color)
    draw.polygon(points, fill=(*rgb, opacity))
    for _ in range(max(4, width // 18)):
        x = rng.randint(left + 3, right - 3)
        line_alpha = max(8, opacity // 14)
        draw.line((x, top + 2, x, bottom - 2), fill=(255, 255, 255, line_alpha), width=1)
    shadow = body.getchannel("A").filter(ImageFilter.GaussianBlur(max(2, height / 8)))
    shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow_layer.putalpha(shadow.point(lambda a: int(a * 0.22)))
    shadow_color = Image.new("RGBA", canvas.size, (20, 16, 12, 255))
    shadow_color.putalpha(shadow_layer.getchannel("A"))
    canvas.alpha_composite(shadow_color, (2, 4))
    canvas.alpha_composite(body)
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--tape", action="append", type=parse_tape, required=True)
    args = parser.parse_args()

    board = Image.open(args.input).convert("RGBA")
    for index, (x, y, width, height, angle, color, opacity) in enumerate(args.tape):
        tape = make_tape(width, height, color, opacity, seed=3109 + index)
        tape = tape.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
        board.alpha_composite(tape, (round(x - tape.width / 2), round(y - tape.height / 2)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    board.convert("RGB").save(args.output, quality=96)


if __name__ == "__main__":
    main()

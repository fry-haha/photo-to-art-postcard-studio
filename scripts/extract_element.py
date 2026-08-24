#!/usr/bin/env python3
"""Crop an element and optionally remove an edge-connected flat background."""

from __future__ import annotations

import argparse
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter


def parse_box(value: str) -> tuple[int, int, int, int]:
    parts = tuple(int(v) for v in value.split(","))
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be x1,y1,x2,y2")
    return parts


def parse_color(value: str) -> tuple[int, int, int] | None:
    if value == "none":
        return None
    if value == "auto":
        return (-1, -1, -1)
    parts = tuple(int(v) for v in value.split(","))
    if len(parts) != 3 or any(v < 0 or v > 255 for v in parts):
        raise argparse.ArgumentTypeError("background must be auto, none, or r,g,b")
    return parts


def parse_polygon(value: str) -> list[tuple[int, int]]:
    try:
        points = [tuple(int(v) for v in point.split(",")) for point in value.split(";")]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("polygon must be x,y;x,y;...") from exc
    if len(points) < 3 or any(len(point) != 2 for point in points):
        raise argparse.ArgumentTypeError("polygon must contain at least three x,y points")
    return points


def edge_connected_mask(candidate: np.ndarray) -> np.ndarray:
    height, width = candidate.shape
    seen = np.zeros((height, width), dtype=bool)
    queue: deque[tuple[int, int]] = deque()
    for x in range(width):
        if candidate[0, x]:
            queue.append((0, x))
        if candidate[height - 1, x]:
            queue.append((height - 1, x))
    for y in range(height):
        if candidate[y, 0]:
            queue.append((y, 0))
        if candidate[y, width - 1]:
            queue.append((y, width - 1))
    while queue:
        y, x = queue.popleft()
        if seen[y, x] or not candidate[y, x]:
            continue
        seen[y, x] = True
        if y:
            queue.append((y - 1, x))
        if y + 1 < height:
            queue.append((y + 1, x))
        if x:
            queue.append((y, x - 1))
        if x + 1 < width:
            queue.append((y, x + 1))
    return seen


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--box", type=parse_box)
    parser.add_argument("--background", type=parse_color, default=None)
    parser.add_argument("--tolerance", type=float, default=28.0)
    parser.add_argument(
        "--global-background",
        action="store_true",
        help="remove every matching background pixel, including enclosed areas",
    )
    parser.add_argument("--feather", type=float, default=0.7)
    parser.add_argument("--padding", type=int, default=8)
    parser.add_argument("--polygon", action="append", type=parse_polygon, default=[])
    parser.add_argument("--ellipse", action="append", type=parse_box, default=[])
    args = parser.parse_args()

    image = Image.open(args.input).convert("RGBA")
    if args.box:
        image = image.crop(args.box)

    if args.background is not None:
        pixels = np.asarray(image).copy()
        rgb = pixels[:, :, :3].astype(np.float32)
        if args.background == (-1, -1, -1):
            corners = np.array(
                [rgb[0, 0], rgb[0, -1], rgb[-1, 0], rgb[-1, -1]],
                dtype=np.float32,
            )
            background = np.median(corners, axis=0)
        else:
            background = np.array(args.background, dtype=np.float32)
        distance = np.sqrt(np.sum((rgb - background) ** 2, axis=2))
        candidate = distance <= args.tolerance
        removable = candidate if args.global_background else edge_connected_mask(candidate)
        alpha = pixels[:, :, 3]
        alpha[removable] = 0
        if args.feather > 0:
            alpha_image = Image.fromarray(alpha, "L").filter(
                ImageFilter.GaussianBlur(args.feather)
            )
            alpha = np.asarray(alpha_image)
        pixels[:, :, 3] = alpha
        image = Image.fromarray(pixels, "RGBA")

    if args.polygon or args.ellipse:
        shape_mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(shape_mask)
        for polygon in args.polygon:
            draw.polygon(polygon, fill=255)
        for ellipse in args.ellipse:
            draw.ellipse(ellipse, fill=255)
        image.putalpha(ImageChops.multiply(image.getchannel("A"), shape_mask))

    bbox = image.getbbox()
    if bbox:
        left = max(0, bbox[0] - args.padding)
        top = max(0, bbox[1] - args.padding)
        right = min(image.width, bbox[2] + args.padding)
        bottom = min(image.height, bbox[3] + args.padding)
        image = image.crop((left, top, right, bottom))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output)


if __name__ == "__main__":
    main()

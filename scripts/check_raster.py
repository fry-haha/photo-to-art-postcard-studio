#!/usr/bin/env python3
"""Report basic raster readiness without modifying the image."""

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("--width-mm", type=float)
    parser.add_argument("--height-mm", type=float)
    parser.add_argument("--ppi", type=int, default=300)
    args = parser.parse_args()

    with Image.open(args.image) as image:
        width, height = image.size
        has_alpha = image.mode in {"RGBA", "LA"} or "transparency" in image.info
        print(f"file: {args.image}")
        print(f"pixels: {width} x {height}")
        print(f"mode: {image.mode}")
        print(f"alpha: {'yes' if has_alpha else 'no'}")

        if args.width_mm and args.height_mm:
            required_width = round(args.width_mm / 25.4 * args.ppi)
            required_height = round(args.height_mm / 25.4 * args.ppi)
            direct = width >= required_width and height >= required_height
            rotated = width >= required_height and height >= required_width
            print(f"required: {required_width} x {required_height} px at {args.ppi} ppi")
            print(f"size-ready: {'yes' if direct or rotated else 'no'}")


if __name__ == "__main__":
    main()

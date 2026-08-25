#!/usr/bin/env python3
"""Remove a flat chroma-key background and validate the alpha result."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from statistics import median
import sys


def fail(message: str, code: int = 1) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_pillow():
    try:
        import PIL
        from PIL import Image, ImageFilter
    except ImportError:
        print(
            "Pillow is required but is not installed in this Python environment.\n"
            "Activate the project environment, then use one of:\n"
            "  uv pip install pillow\n"
            "  python3 -m pip install pillow\n"
            "Install automatically only when the active permission policy explicitly allows "
            "unattended dependency installation; otherwise ask the user first.\n"
            "Rerun this command after installation.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return PIL, Image, ImageFilter


def parse_color(raw: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"#?([0-9a-fA-F]{6})", raw.strip())
    if not match:
        fail("--key-color must be a hex RGB value such as #00ff00.")
    value = match.group(1)
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def sample_key(image, mode: str) -> tuple[int, int, int]:
    width, height = image.size
    pixels = image.load()
    samples: list[tuple[int, int, int]] = []

    if mode == "corners":
        patch = max(1, min(width, height, 12))
        boxes = (
            (0, 0, patch, patch),
            (width - patch, 0, width, patch),
            (0, height - patch, patch, height),
            (width - patch, height - patch, width, height),
        )
        for left, top, right, bottom in boxes:
            for y in range(top, bottom):
                for x in range(left, right):
                    samples.append(tuple(pixels[x, y][:3]))
    else:
        band = max(1, min(width, height, 6))
        step = max(1, min(width, height) // 256)
        for x in range(0, width, step):
            for y in range(band):
                samples.append(tuple(pixels[x, y][:3]))
                samples.append(tuple(pixels[x, height - 1 - y][:3]))
        for y in range(0, height, step):
            for x in range(band):
                samples.append(tuple(pixels[x, y][:3]))
                samples.append(tuple(pixels[width - 1 - x, y][:3]))

    if not samples:
        fail("Could not sample a key color from the image border.")
    return tuple(int(round(median(sample[i] for sample in samples))) for i in range(3))


def spill_channels(key: tuple[int, int, int]) -> list[int]:
    strongest = max(key)
    if strongest < 128:
        return []
    return [i for i, value in enumerate(key) if value >= strongest - 16 and value >= 128]


def key_dominance(rgb: tuple[int, int, int], key: tuple[int, int, int]) -> float:
    spill = spill_channels(key)
    if not spill:
        return 0.0
    other = [i for i in range(3) if i not in spill]
    key_strength = min(rgb[i] for i in spill)
    other_strength = max((rgb[i] for i in other), default=0)
    return float(key_strength - other_strength)


def dominance_alpha(rgb: tuple[int, int, int], key: tuple[int, int, int]) -> int:
    dominance = key_dominance(rgb, key)
    if dominance <= 0:
        return 255
    spill = spill_channels(key)
    other = [i for i in range(3) if i not in spill]
    other_strength = max((rgb[i] for i in other), default=0)
    denominator = max(1.0, float(max(key)) - other_strength)
    return round(255 * (1.0 - min(1.0, dominance / denominator)))


def soft_alpha(distance: int, transparent: float, opaque: float) -> int:
    if distance <= transparent:
        return 0
    if distance >= opaque:
        return 255
    ratio = (distance - transparent) / (opaque - transparent)
    smooth = ratio * ratio * (3.0 - 2.0 * ratio)
    return round(255 * smooth)


def despill(rgb: tuple[int, int, int], key: tuple[int, int, int], alpha: int):
    if alpha >= 252:
        return rgb
    spill = spill_channels(key)
    other = [i for i in range(3) if i not in spill]
    if not spill or not other:
        return rgb
    channels = list(rgb)
    cap = max(0, max(channels[i] for i in other) - 1)
    for i in spill:
        channels[i] = min(channels[i], cap)
    return tuple(channels)


def process(args) -> None:
    _, Image, ImageFilter = load_pillow()
    source = Path(args.input)
    output = Path(args.out)

    if not source.is_file():
        fail(f"Input image not found: {source}")
    if output.exists() and not args.force:
        fail(f"Output already exists: {output} (use --force to overwrite)")
    if output.suffix.lower() not in {".png", ".webp"}:
        fail("--out must end in .png or .webp to preserve alpha.")
    if not 0 <= args.transparent_threshold < args.opaque_threshold <= 255:
        fail("Require 0 <= transparent threshold < opaque threshold <= 255.")
    if not 0 <= args.edge_contract <= 16:
        fail("--edge-contract must be between 0 and 16.")
    if not 0 <= args.edge_feather <= 64:
        fail("--edge-feather must be between 0 and 64.")

    with Image.open(source) as opened:
        image = opened.convert("RGBA")
    key = parse_color(args.key_color) if args.auto_key == "none" else sample_key(image, args.auto_key)
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            red, green, blue, original_alpha = pixels[x, y]
            rgb = (red, green, blue)
            distance = max(abs(rgb[i] - key[i]) for i in range(3))
            key_like = distance <= 32 or key_dominance(rgb, key) >= 16
            alpha = min(
                soft_alpha(distance, args.transparent_threshold, args.opaque_threshold),
                dominance_alpha(rgb, key),
            ) if key_like else 255
            alpha = round(alpha * original_alpha / 255)
            if alpha <= 8:
                alpha = 0
            if alpha == 0:
                pixels[x, y] = (0, 0, 0, 0)
            else:
                if args.despill and key_like:
                    red, green, blue = despill(rgb, key, alpha)
                pixels[x, y] = (red, green, blue, alpha)

    alpha_channel = image.getchannel("A")
    for _ in range(args.edge_contract):
        alpha_channel = alpha_channel.filter(ImageFilter.MinFilter(3))
    if args.edge_feather:
        alpha_channel = alpha_channel.filter(ImageFilter.GaussianBlur(args.edge_feather))
    image.putalpha(alpha_channel)

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, format="PNG" if output.suffix.lower() == ".png" else "WEBP")

    flattened = getattr(alpha_channel, "get_flattened_data", None)
    alpha_values = list(flattened() if flattened else alpha_channel.getdata())
    total = width * height
    transparent = sum(value == 0 for value in alpha_values)
    partial = sum(0 < value < 255 for value in alpha_values)
    corners = [
        alpha_channel.getpixel((0, 0)),
        alpha_channel.getpixel((width - 1, 0)),
        alpha_channel.getpixel((0, height - 1)),
        alpha_channel.getpixel((width - 1, height - 1)),
    ]
    visible = sum(value > 0 for value in alpha_values) / total

    print(f"Wrote: {output}")
    print(f"Size: {width}x{height}; mode: RGBA")
    print(f"Key color: #{key[0]:02x}{key[1]:02x}{key[2]:02x}")
    print(f"Transparent pixels: {transparent}/{total}")
    print(f"Partially transparent pixels: {partial}/{total}")
    print(f"Corner alpha: {corners}")
    print(f"Visible coverage: {visible:.4f}")
    if any(corners):
        print("Warning: one or more corners remain visible.", file=sys.stderr)
    if visible == 0:
        fail("Extraction removed the entire image.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Remove a flat chroma-key background and validate the alpha result."
    )
    parser.add_argument("--check", action="store_true", help="Check Python and Pillow dependencies.")
    parser.add_argument("--input", help="Input image path.")
    parser.add_argument("--out", help="Output .png or .webp path.")
    parser.add_argument("--key-color", default="#00ff00", help="Key color when auto sampling is disabled.")
    parser.add_argument("--auto-key", choices=["none", "corners", "border"], default="border")
    parser.add_argument("--transparent-threshold", type=float, default=12.0)
    parser.add_argument("--opaque-threshold", type=float, default=220.0)
    parser.add_argument("--despill", action="store_true", help="Remove key-color spill from partial edges.")
    parser.add_argument("--edge-contract", type=int, default=0)
    parser.add_argument("--edge-feather", type=float, default=0.0)
    parser.add_argument("--force", action="store_true", help="Overwrite an existing output.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.check:
        PIL, _, _ = load_pillow()
        print(f"Ready: Python {sys.version_info.major}.{sys.version_info.minor}; Pillow {PIL.__version__}")
        return
    if not args.input or not args.out:
        parser.error("--input and --out are required unless --check is used")
    process(args)


if __name__ == "__main__":
    main()

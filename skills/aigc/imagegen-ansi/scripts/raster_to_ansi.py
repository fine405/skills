#!/usr/bin/env python3
"""Convert a transparent raster image into ANSI half-block art or JavaScript."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None  # type: ignore[assignment]


WHITE = "\x1b[97m"
RESET = "\x1b[0m"


def require_pillow() -> None:
    if Image is None:
        raise RuntimeError(
            "Pillow is required. Install it in the active environment with "
            "`uv pip install pillow` or `python3 -m pip install pillow`."
        )


def load_bitmap(
    input_path: Path, width: int, threshold: int
) -> tuple[list[str], tuple[int, int], tuple[int, int, int, int], float]:
    require_pillow()
    assert Image is not None

    image = Image.open(input_path).convert("RGBA")
    alpha = image.getchannel("A")
    corners = (
        alpha.getpixel((0, 0)),
        alpha.getpixel((image.width - 1, 0)),
        alpha.getpixel((0, image.height - 1)),
        alpha.getpixel((image.width - 1, image.height - 1)),
    )
    if any(corners):
        raise ValueError(
            "Input corners are not transparent. Remove the background before "
            "converting to ANSI."
        )

    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError("Input contains no visible pixels.")

    cropped = alpha.crop(bbox)
    height = max(2, round(width * cropped.height / cropped.width))
    height += height % 2
    sampled = cropped.resize((width, height), Image.Resampling.BOX)
    rows = [
        "".join(
            "#" if sampled.getpixel((x, y)) >= threshold else " "
            for x in range(width)
        ).rstrip()
        for y in range(height)
    ]
    visible_coverage = sum(row.count("#") for row in rows) / (width * height)
    if visible_coverage == 0:
        raise ValueError(
            "Alpha threshold removed every pixel. Lower --threshold or inspect the input."
        )
    return rows, image.size, bbox, visible_coverage


def render_half_blocks(rows: list[str], color: bool) -> str:
    width = max(map(len, rows))
    lines: list[str] = []

    for y in range(0, len(rows), 2):
        line = ""
        for x in range(width):
            top = x < len(rows[y]) and rows[y][x] == "#"
            bottom = x < len(rows[y + 1]) and rows[y + 1][x] == "#"
            line += "█" if top and bottom else "▀" if top else "▄" if bottom else " "
        lines.append(line.rstrip())

    art = "\n".join(lines)
    return f"{WHITE}{art}{RESET}" if color else art


def javascript_module(rows: list[str]) -> str:
    encoded_rows = json.dumps(rows, ensure_ascii=False, indent=2)
    return f"""import {{ realpathSync }} from "node:fs";
import {{ pathToFileURL }} from "node:url";

const BITMAP = {encoded_rows};
const SOURCE_WIDTH = Math.max(...BITMAP.map((row) => row.length));

export function renderAnsiArt(
  terminalWidth = SOURCE_WIDTH + 4,
  color = process.stdout.isTTY === true && process.env.NO_COLOR === undefined,
) {{
  const width = Math.min(SOURCE_WIDTH, Math.max(1, terminalWidth - 4));
  let height = Math.max(2, Math.round((width * BITMAP.length) / SOURCE_WIDTH));
  height += height % 2;

  const isSet = (x, y) => {{
    const sourceX = Math.floor((x * SOURCE_WIDTH) / width);
    const sourceY = Math.floor((y * BITMAP.length) / height);
    return BITMAP[sourceY]?.[sourceX] === "#";
  }};

  const margin = " ".repeat(Math.max(0, Math.floor((terminalWidth - width) / 2)));
  const lines = [];
  for (let y = 0; y < height; y += 2) {{
    let line = "";
    for (let x = 0; x < width; x += 1) {{
      const top = isSet(x, y);
      const bottom = isSet(x, y + 1);
      line += top ? (bottom ? "█" : "▀") : bottom ? "▄" : " ";
    }}
    lines.push(margin + line.trimEnd());
  }}

  const art = lines.join("\\n");
  return color ? `\\u001b[97m${{art}}\\u001b[0m` : art;
}}

if (
  process.argv[1] &&
  import.meta.url === pathToFileURL(realpathSync(process.argv[1])).href
) {{
  process.stdout.write(`${{renderAnsiArt(process.stdout.columns)}}\\n`);
}}
"""


def write_result(content: str, output_path: Path | None, force: bool) -> None:
    normalized = content.rstrip("\n") + "\n"
    if output_path is None:
        sys.stdout.write(normalized)
        return
    if output_path.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite {output_path}. Use --force or choose another path."
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(normalized, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a transparent raster into ANSI art or JavaScript."
    )
    parser.add_argument("--check", action="store_true", help="check dependencies")
    parser.add_argument("--input", type=Path, help="transparent PNG or WebP")
    parser.add_argument("--width", type=int, default=96, help="sampled pixel width")
    parser.add_argument(
        "--threshold", type=int, default=96, help="alpha threshold from 0 to 255"
    )
    parser.add_argument(
        "--format",
        choices=("ansi", "plain", "js"),
        default="ansi",
        help="output format",
    )
    parser.add_argument("--out", type=Path, help="write output to this path")
    parser.add_argument("--force", action="store_true", help="overwrite --out")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        require_pillow()
        if args.check:
            assert Image is not None
            print(f"OK: Pillow {Image.__version__}")
            return 0
        if args.input is None:
            raise ValueError("--input is required unless --check is used.")
        if args.width < 1:
            raise ValueError("--width must be at least 1.")
        if not 0 <= args.threshold <= 255:
            raise ValueError("--threshold must be between 0 and 255.")

        rows, size, bbox, coverage = load_bitmap(
            args.input, args.width, args.threshold
        )
        content = (
            javascript_module(rows)
            if args.format == "js"
            else render_half_blocks(rows, color=args.format == "ansi")
        )
        write_result(content, args.out, args.force)
        print(
            f"Input: {size[0]}x{size[1]} RGBA; alpha bbox: {bbox}; "
            f"bitmap: {args.width}x{len(rows)}; visible coverage: {coverage:.3f}",
            file=sys.stderr,
        )
        return 0
    except (FileExistsError, OSError, RuntimeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

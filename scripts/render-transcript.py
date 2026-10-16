#!/usr/bin/env python3
"""Render real logs as labelled transcript images; never fabricate command results."""
import argparse
import re
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument("input", type=Path)
parser.add_argument("output", type=Path)
parser.add_argument("--title", default="Orbit — command output")
args = parser.parse_args()
font_paths = ["/System/Library/Fonts/Menlo.ttc", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"]
font_path = next((p for p in font_paths if Path(p).exists()), None)
font = ImageFont.truetype(font_path, 14) if font_path else ImageFont.load_default(size=14)
body = re.sub(r"\x1b\[[0-9;]*[mGKHF]", "", args.input.read_text(errors="replace"))
lines = []
for line in body.splitlines():
    lines.extend(textwrap.wrap(line, width=132, replace_whitespace=False, drop_whitespace=False) or [""])
for start in range(0, max(1, len(lines)), 44):
    chunk = lines[start:start + 44]
    canvas = Image.new("RGB", (1200, 112 + len(chunk) * 21), "#14241f")
    draw = ImageDraw.Draw(canvas)
    draw.text((24, 18), args.title, font=font, fill="#e7f0df")
    draw.text((24, 44), "Rendered transcript of actual output | source: " + args.input.name, font=font, fill="#8fa58d")
    for index, line in enumerate(chunk):
        color = "#b6db98" if "PASSED" in line or "passed" in line else "#d2ddd0"
        draw.text((24, 84 + index * 21), line, font=font, fill=color)
    suffix = f"-{start // 44 + 1:02}" if len(lines) > 44 else ""
    target = args.output.with_name(args.output.stem + suffix + args.output.suffix)
    target.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(target)
    print(target)

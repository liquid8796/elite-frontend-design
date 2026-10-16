#!/usr/bin/env python3
"""Produce a muted cinematic MP4 plus poster from 1..12 genuine still images.

This is an FFmpeg animated-stills compositor; it is NOT a generative video model.
No network requests and no external API calls. Uses only Python stdlib + ffmpeg.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--images", nargs="+", required=True, type=Path, help="Ordered source stills (PNG, JPEG, WebP, etc.)")
    p.add_argument("--output", required=True, type=Path, help="Output H.264 .mp4")
    p.add_argument("--width", type=int, default=1280)
    p.add_argument("--height", type=int, default=720)
    p.add_argument("--fps", type=int, default=24)
    p.add_argument("--seconds-per-image", type=float, default=3.0)
    p.add_argument("--transition", type=float, default=0.6, help="Crossfade seconds between images (zero for single still)")
    p.add_argument("--zoom", type=float, default=0.08, help="Total Ken Burns zoom: 0.00..0.20")
    p.add_argument("--crf", type=int, default=23, help="H.264 quality: 17..32, lower is larger")
    p.add_argument("--ffmpeg", default="ffmpeg", help="FFmpeg binary/path")
    p.add_argument("--poster", type=Path, help="Optional poster path (default: output stem + -poster.jpg)")
    return p


def validate(a: argparse.Namespace) -> tuple[list[Path], Path, Path, str]:
    images = [x.expanduser().resolve() for x in a.images]
    if not 1 <= len(images) <= 12:
        raise ValueError("Provide between 1 and 12 images.")
    for img in images:
        if not img.is_file() or img.stat().st_size == 0:
            raise ValueError(f"Missing or empty image: {img}")
    if not (256 <= a.width <= 3840 and a.width % 2 == 0 and 256 <= a.height <= 2160 and a.height % 2 == 0):
        raise ValueError("Video dimensions must be even: width 256..3840, height 256..2160.")
    if not 12 <= a.fps <= 60:
        raise ValueError("fps must be 12..60.")
    if not 1 <= a.seconds_per_image <= 15:
        raise ValueError("seconds-per-image must be 1..15.")
    if not 0 <= a.transition < a.seconds_per_image / 2:
        raise ValueError("transition must be >=0 and shorter than half the still duration.")
    if not 0 <= a.zoom <= 0.20:
        raise ValueError("zoom must be 0..0.20.")
    if not 17 <= a.crf <= 32:
        raise ValueError("crf must be 17..32.")
    out = a.output.expanduser().resolve()
    if out.suffix.lower() != ".mp4":
        raise ValueError("Output must be .mp4.")
    poster = (a.poster or out.with_name(f"{out.stem}-poster.jpg")).expanduser().resolve()
    if poster.suffix.lower() not in (".jpg", ".jpeg"):
        raise ValueError("Poster must be a JPEG.")
    if out == poster or out in images or poster in images:
        raise ValueError("Outputs cannot overwrite source image files.")
    binary = shutil.which(a.ffmpeg)
    if not binary:
        raise ValueError(f"FFmpeg not found: {a.ffmpeg}. Install it or specify --ffmpeg.")
    return images, out, poster, binary


def filters(a: argparse.Namespace, n: int) -> tuple[str, str, float]:
    # Duplicate frames of each still, then a small centered camera move;
    # the zoom is deterministic and independent of a generative video model.
    frames = max(1, round(a.seconds_per_image * a.fps))
    increment = a.zoom / frames
    chains = []
    for i in range(n):
        base = (f"[{i}:v]scale={a.width}:{a.height}:force_original_aspect_ratio=increase,"
                f"crop={a.width}:{a.height},setsar=1,"
                f"zoompan=z='min(1+on*{increment:.9f},1+{a.zoom:.5f})':"
                f"x='(iw-iw/zoom)*({0.38 if i % 2 == 0 else 0.62}+"
                f"({0.24 if i % 2 == 0 else -0.24})*on/{frames})':"
                f"y='(ih-ih/zoom)*(0.52-0.04*on/{frames})':"
                f"d=1:s={a.width}x{a.height}:fps={a.fps},"
                f"trim=duration={a.seconds_per_image:.5f},setpts=PTS-STARTPTS,"
                f"format=yuv420p")
        chains.append(base + f"[v{i}]")
    if n == 1:
        return ";".join(chains), "v0", a.seconds_per_image
    prev = "v0"
    for i in range(1, n):
        dest = f"mix{i}"
        offset = i * (a.seconds_per_image - a.transition)
        if a.transition:
            chains.append(f"[{prev}][v{i}]xfade=transition=fade:duration={a.transition:.5f}:offset={offset:.5f}[{dest}]")
        else:
            chains.append(f"[{prev}][v{i}]concat=n=2:v=1:a=0[{dest}]")
        prev = dest
    seconds = n * a.seconds_per_image - (n - 1) * a.transition
    return ";".join(chains), prev, seconds


def run(a: argparse.Namespace) -> tuple[Path, Path]:
    images, out, poster, ffmpeg = validate(a)
    out.parent.mkdir(parents=True, exist_ok=True)
    poster.parent.mkdir(parents=True, exist_ok=True)
    inputs: list[str] = []
    for path in images:
        inputs += ["-loop", "1", "-framerate", str(a.fps), "-i", str(path)]
    graph, label, seconds = filters(a, len(images))
    # Limit input-processing threads for predictable memory consumption on Windows.
    cmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
           *inputs, "-filter_complex", graph,
           "-map", f"[{label}]", "-t", f"{seconds:.4f}", "-r", str(a.fps),
           "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", str(a.crf),
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        out.unlink(missing_ok=True)
        raise RuntimeError(f"FFmpeg video render failed: {exc.stderr[-1800:]}") from exc
    postcmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
               "-i", str(images[0]), "-vf",
               f"scale={a.width}:{a.height}:force_original_aspect_ratio=increase,crop={a.width}:{a.height}",
               "-frames:v", "1", "-q:v", "3", str(poster)]
    try:
        subprocess.run(postcmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"MP4 exists but poster generation failed: {exc.stderr[-1800:]}") from exc
    if not out.is_file() or out.stat().st_size == 0 or not poster.is_file():
        raise RuntimeError("FFmpeg finished but output or poster missing.")
    return out, poster


def main(argv: list[str] | None = None) -> int:
    a = parser().parse_args(argv)
    try:
        out, poster = run(a)
    except (ValueError, RuntimeError) as exc:
        print(f"media generation error: {exc}", file=sys.stderr)
        return 2
    print(f"Video: {out}")
    print(f"Poster: {poster}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

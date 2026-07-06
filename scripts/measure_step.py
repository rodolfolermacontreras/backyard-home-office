#!/usr/bin/env python3
"""
measure_step.py — Read a STEP (.stp) CAD file and report its overall size.

STEP files store 3D geometry as CARTESIAN_POINT(x, y, z) entries in millimeters.
This tool scans every point, finds the min/max on each axis, and prints the
overall bounding-box dimensions in mm, cm, inches, and feet.

Usage:
    python scripts/measure_step.py <file1.stp> [file2.stp ...]
    python scripts/measure_step.py cad/pod-core/step/*.stp

Note: For an assembly file this gives the whole-pod envelope. For a single part
file it gives that part's size. Values are geometry bounds (structure only).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Matches: CARTESIAN_POINT('',(1.23,-4.5,6.0))  -> captures "1.23,-4.5,6.0"
POINT_RE = re.compile(r"CARTESIAN_POINT\('[^']*',\(([^)]*)\)\)")
FLOAT_RE = re.compile(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?")

MM_PER_INCH = 25.4


def bounding_box(path: Path) -> tuple[list[float], list[float], int]:
    """Return (mins[x,y,z], maxs[x,y,z], point_count) for a STEP file."""
    mins = [float("inf")] * 3
    maxs = [float("-inf")] * 3
    count = 0
    with path.open("r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            for match in POINT_RE.finditer(line):
                nums = FLOAT_RE.findall(match.group(1))
                if len(nums) < 3:
                    continue
                x, y, z = float(nums[0]), float(nums[1]), float(nums[2])
                for i, v in enumerate((x, y, z)):
                    if v < mins[i]:
                        mins[i] = v
                    if v > maxs[i]:
                        maxs[i] = v
                count += 1
    return mins, maxs, count


def fmt_mm(mm: float) -> str:
    inches = mm / MM_PER_INCH
    feet = inches / 12.0
    return f"{mm:8.1f} mm  |  {mm/10:6.1f} cm  |  {inches:6.1f} in  |  {feet:5.2f} ft"


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 1

    for arg in argv:
        path = Path(arg)
        if not path.exists():
            print(f"SKIP (not found): {arg}")
            continue

        mins, maxs, count = bounding_box(path)
        if count == 0:
            print(f"{path.name}: no CARTESIAN_POINT geometry found")
            continue

        dx = maxs[0] - mins[0]
        dy = maxs[1] - mins[1]
        dz = maxs[2] - mins[2]

        print("=" * 78)
        print(f"{path.name}   ({count:,} points)")
        print(f"  Width  (X): {fmt_mm(dx)}")
        print(f"  Depth  (Y): {fmt_mm(dy)}")
        print(f"  Height (Z): {fmt_mm(dz)}")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

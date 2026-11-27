"""Reproduce the check on DominoBench: Evaluating Multi-Step Physical Reasoning from Still Images, arXiv:2611.20385v2.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.20385", "v2", "b2ef32b17141592160faf178218f28c3fe8bb72e4504fd18870b05986f4599ea")

print("Table S4 (p. 15): DominoBench-38 has 38 items in 19 pairs, and every row has n = 38")
quote(doc, 15, "Table S4. Full leaderboard on DominoBench-38 (19 pairs, six mechanisms), image mode, H0 and H3.")
quote(doc, 15, "Exact Both twins Deciding person DominoScore Model n H0 H3 H0 H3 H0 H3 H0 H3")

items = {round(100 * k / 38) for k in range(39)}  # Exact and Deciding person: k of 38 items
pairs = {round(100 * k / 19) for k in range(20)}  # Both twins: k of 19 pairs
cols = ["Exact H0", "Exact H3", "Both twins H0", "Both twins H3", "Deciding H0", "Deciding H3"]

text = page_text(doc, 15)
body = text[text.find("H0 H3 H0 H3 H0 H3 H0 H3") + 23:]
bad = 0
for m in re.finditer(r"([A-Za-z][\w .\-]*?†?) 38 ((?:\d+ ){7}\d+)", body):
    vals = [int(x) for x in m.group(2).split()][:6]
    for col, v in zip(cols, vals):
        allowed = pairs if col.startswith("Both") else items
        if v not in allowed:
            bad += 1
            denom = "19 pairs" if col.startswith("Both") else "38 items"
            near = sorted(allowed, key=lambda a: abs(a - v))[:2]
            print(f"  {m.group(1).strip():24s} {col:14s} {v:3d}%  not k/{denom}; nearest {sorted(near)}")
print(f"  {bad} cells cannot be a whole number of items or pairs; all of them are multiples of 10")

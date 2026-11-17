"""Reproduce the check on SIMIT, arXiv:2611.00053v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.00053", "v1", "8e29837631d72b746ca9358e425b2de003130051f726e6bbfec8919094dd2506")

print("Table 4 (p. 16): 500 evaluation examples per benchmark, multiple-choice accuracy for MMBench")
quote(doc, 16, "MM-Bench (EN) (Liu et al., 2024) 2000 50 500")
quote(doc, 16, "MMBench (CN/EN) and SEED-Bench use multiple-choice accuracy")

# Benchmarks scored as plain accuracy (one point per question), so each score must be k/N.
names = ["GQA", "AI2D", "ChartQA", r"MM-Bench \(CN\)", r"MM-Bench \(EN\)", "SEED-Bench"]


def fits(x, n):
    return any(round(100 * k / n, 1) == x for k in range(n + 1))


def scores(page, table):
    t = page_text(doc, page)
    t = t[t.find(table):]
    out = {}
    for name in names:
        row = re.search(name + r" ((?:\+?-?\d+\.\d+ ?)+)", t).group(1).split()
        out[name.replace("\\", "")] = [float(v) for v in row if not v.startswith(("+", "-"))]
    return out


for page, table in [(37, "Table 8:"), (41, "Table 9:")]:
    print(f"\n{table} (p. {page}): scores that are not k/500")
    for name, vals in scores(page, table).items():
        bad = [v for v in vals if not fits(v, 500)]
        note = f"all {len(vals)} fit k/500" if not bad else f"{bad} do not fit k/500; all fit k/132: {all(fits(v, 132) for v in vals)}"
        print(f"  {name:15s} {vals}  {note}")

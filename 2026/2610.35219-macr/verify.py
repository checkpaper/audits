"""Reproduce the checks on Multi-Agent Relay Thinking (MACR), arXiv:2610.35219v2.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.35219", "v2", "728fa5ac09fbb0e6b9d13f10d004ca0094a44216eadec0ee04119141160ec48f")

print("1. MACR tokens per sample on MMStar: Table 1 versus Table 2")
quote(doc, 6, "MACR 78.00±0.17 4,811 15.38 55.80±0.39 6,149 7.89 72.00±0.12 4,150 21.35")
quote(doc, 5, "MACR demands only 4,150 tokens on MMStar")
quote(doc, 7, "MACR 72.40 312 Table 2: Ablation study of MACR")
quote(doc, 7, "on 500 randomly sampled instances from MMStar")
print(f"  4,150 / 312 = {4150 / 312:.1f}x on the same benchmark; accuracy 72.00 (full) vs 72.40 (subset)")

print("\n2. Number at risk: Section 3.4.2 versus Figure 6b")
quote(doc, 7, "(3,151) roughly twice that of the other two models (1,163 and 1,658)")
quote(doc, 8, "Number at Risk 585 111 81 810 104 49 1,781 264 137")
cells = {585, 111, 81, 810, 104, 49, 1781, 264, 137, 200, 271, 649}
print("  Figure 6b at-risk cells:", sorted(cells, reverse=True))
print("  Largest cells: 1,781, 810 and 585; text values in the table:", [v for v in (3151, 1163, 1658) if v in cells])

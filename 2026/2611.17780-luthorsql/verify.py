"""Reproduce the check on LuthorSQL, arXiv:2611.17780v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.17780", "v1", "9ce78b713770fb2eabc740fafdcc2c236e46e500a6f815e4a8b21e9d78b0fd55")

print("App. F handoff paragraph and Table 10 (p. 18)")
quote(doc, 18, "does less work: 28% less agent time and 18% fewer logged tokens.")
quote(doc, 18, "Of the 330 questions with candidates it took one on 279 (87% right) and wrote its own query on the other 121 (57% right)")
quote(doc, 18, "EX (400 questions) 77.75 78.00 +0.25")
quote(doc, 18, "Tool calls (all) 207 169 −18%")
quote(doc, 18, "Output text is an estimate (output characters / 4); logged output-token counts were not lower.")

took, own = 279, 121
print(f"\n  1. {took} + {own} = {took + own}, not 330")
right = round(0.87 * took) + round(0.57 * own)
print(f"     87% of {took} = {0.87 * took:.1f}, 57% of {own} = {0.57 * own:.1f}; "
      f"about {right} right, {right} / 400 = {right / 400:.2%} (Table 10: 78.00%)")
print(f"  2. Table 10 rows with -18%: tool calls 169 / 207 - 1 = {169 / 207 - 1:+.1%}; "
      "the caption says logged output-token counts were not lower")

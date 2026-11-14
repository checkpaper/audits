"""Reproduce the checks on Cross-Primitive Consistency in Jev, arXiv:2610.38623v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.38623", "v1", "f536b19f1197864a52dc8b6b4a29574283d6f204d749113e7f0654cfd859fd1d")

print("1. Axis III, JevK5-4B: Figure 5 quadrants versus the conflict rate K in Table 3")
quote(doc, 5, "JevK5-4B 0.2614 26.69 10.83")
quote(doc, 5, "K is the Choice/Noul hard-label conflict rate")
quote(doc, 5, "33.82% 4.45% 24.74% 36.99%")
quote(doc, 5, "The dashed lines denote the 0.5 decision boundaries")
off = 24.74 + 4.45
print(f"  Off-diagonal quadrants: 24.74 + 4.45 = {off:.2f}%; K = 26.69%; gap {off - 26.69:+.2f} pp")
print(f"  All four quadrants: {24.74 + 36.99 + 33.82 + 4.45:.2f}%")

print("\n2. LODO, JevK5-2B raw-label accuracy 84.90% -> 87.42%: two different gains")
quote(doc, 1, "improves accuracy by +2.97%")
quote(doc, 2, "improves accuracy on raw labels from 84.90% to 87.42% (+2.52%)")
quote(doc, 7, "raw-label accuracy rises from 84.90% to 87.42% (+2.97%)")
print(f"  Absolute: {87.42 - 84.90:.2f} pp; relative: {(87.42 - 84.90) / 84.90:.2%}")
quote(doc, 2, "improves accuracy from 77.67% to 98.48% (+20.81%)")
print(f"  In-domain Axis II: absolute {98.48 - 77.67:.2f} pp, relative {(98.48 - 77.67) / 77.67:.2%}; the paper prints the absolute value here")

"""Reproduce the check on Self-Improvement Memory Enables Continual Recursive Self-Improvement, arXiv:2611.18856v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.18856", "v1", "a8299ba5b16577dd328d602e32f35b914b9393ffb38148d2410f358d4d90ff3d")

print("Rollout counts for TB2.1 (Table 4, p. 18)")
quote(doc, 18, "Coding S: TB2.1 89 44 / 220 45 / 225 pass@1")

print("\nTable 7 (p. 25)")
quote(doc, 25, "Evolve AHE 86.82 90.45 +3.63 91.23 +4.41 Terminus-2 85.91 89.09 +3.18 92.21 +6.30")
quote(doc, 25, "Held-out AHE 85.78 90.22 +4.44 91.28 +5.50 Terminus-2 87.56 91.56 +4.00 91.61 +4.05")

cells = [
    ("Evolve AHE", 220, [("Before", 86.82), ("Gemini After", 90.45), ("Opus After", 91.23)]),
    ("Evolve Terminus-2", 220, [("Before", 85.91), ("Gemini After", 89.09), ("Opus After", 92.21)]),
    ("Held-out AHE", 225, [("Before", 85.78), ("Gemini After", 90.22), ("Opus After", 91.28)]),
    ("Held-out Terminus-2", 225, [("Before", 87.56), ("Gemini After", 91.56), ("Opus After", 91.61)]),
]
print("\nIs each score k / n for an integer k? (tolerance 0.005, i.e. two-decimal rounding)")
for row, n, vals in cells:
    for name, v in vals:
        k = round(v * n / 100)
        ok = abs(100 * k / n - v) <= 0.005
        near = f"{100 * k / n:.2f}"
        print(f"  {row:20s} {name:12s} {v:6.2f}  nearest {k}/{n} = {near}  {'ok' if ok else 'NOT attainable'}")

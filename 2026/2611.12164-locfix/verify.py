"""Reproduce the checks on Let the Fixer Decide (locfix), arXiv:2611.12164v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.12164", "v1", "4a95d6e597ee63e91077e32ee89de3e37b7f46c7579d0c9db8c0130019cab295")

print("Abstract (p. 1) and Sec. 5.2 (p. 9)")
quote(doc, 1, "more tasks are solved (8 vs. 6)")
quote(doc, 9, "Under identical settings (temperature 0.7, 44 calls), S3r1-soft solves 8 tasks and the matched control S3r1-ctrl solves 6")
print("Table 4 (p. 10): System Temp. Output Calls Solved Out-of-budget Wrong-patch Median-calls Loops src/ No-file vs.base")
rows = [
    "Base 0.2 8,192 36 8 2 61 11 – – – –",
    "S1 0.2 8,192 36 10 54 14 30.5 13 6 4 2 / 4 (0.69)",
    "S1 0.2 6,656 36 11 56 9 31.5 18 6 7 2 / 5 (0.45)",
    "S2b 0.3 8,192 44 6 54 14 32.5 28 34 27 4 / 2 (0.69)",
    "S3r1-soft 0.2 8,192 44 8 56 10 38.5 35 36 39 4 / 2 (0.69)",
    "S3r1-hard 0.2 8,192 44 4 60 10 42.5 29 34 33 5 / 1 (0.22)",
    "S1 0.6 6,656 32 8 24 40 32 10 6 2 5 / 5 (1.00)",
    "S2a 0.7 6,656 44 7 38 27 44 12 41 38 3 / 2 (1.00)",
    "S2a-view 0.7 6,656 44 4 37 25 44 13 43 44 7 / 3 (0.34)",
    "S3r0 0.7 6,656 44 5 34 31 44 12 24 32 5 / 2 (0.45)",
    "S3r1-ctrl 0.7 6,656 44 6 32 26 44 16 28 54 6 / 2 (0.29)",
    "S3r1-soft 0.7 6,656 44 6 34 28 44 14 35 43 4 / 2 (0.69)",
    "S3r1-soft 0.7 6,656 32 4 34 31 32 15 34 44 5 / 1 (0.22)",
]
for r in rows:
    quote(doc, 10, r)

BASE = 8
print("\n1. Solved versus the vs. base column: base solves 8, so a system solves 8 - (base only) + (system only)")
for r in rows[1:]:
    c = r.split()
    name, temp, calls, solved = c[0], c[1], int(c[3]), int(c[4])
    only_base, only_sys = int(c[-4]), int(c[-2])
    implied = BASE - only_base + only_sys
    flag = "" if implied == solved else "   <-- differs"
    print(f"  {name:10s} T {temp} calls {calls}: Solved {solved:2d}, implied {implied:2d}{flag}")
print("  At temperature 0.7 and 44 calls, Table 4 gives S3r1-soft 6 and S3r1-ctrl 6, not 8 and 6.")

print("\n2. Median calls versus Out of budget (out of budget includes every task that used all tool calls)")
for r in rows[1:]:
    c = r.split()
    calls, oob, median = int(c[3]), int(c[5]), float(c[7])
    if median == calls:
        print(f"  {c[0]:10s} T {c[1]} calls {calls}: median {median:g} = budget, so at least 39 of 78 tasks used all calls;"
              f" Out of budget {oob}")

"""Reproduce the check on PRISM-T (How Far Can Untrained Neural Networks Go in Anomaly Detection?), arXiv:2611.08136v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.08136", "v1", "013e0ac8ab903e76d551d26a5064b5e89a2d27f9d93386ec67d6ddbd5ad6b264")

print("Proposition 1 and Eq. (9) (p. 4)")
quote(doc, 4, "Proposition 1 (Decomposition of the expected score gap)")
quote(doc, 4, "gives an exact population-level decomposi")

print("\nTable 7 (p. 11), means over 47 ADBench datasets")
cols = ("Raw", "w/o Act.", "PRISM")
rows = {
    "G": "G 0.78 (0.39) 0.77 (0.36) 0.80 (0.45)",
    "Gcov": "Gcov 0.24 (0.18) 0.28 (0.20) 0.49 (0.34)",
    "Gmean": "Gmean 0.55 (0.15) 0.49 (0.09) 0.31 (0.11)",
    "D": "∆ 46.88 (0.06) 114.82 (0.42) 91.50 (4.11)",
    "Dcov": "∆cov 45.18 (0.04) 110.56 (0.21) 60.58 (3.12)",
    "Dmean": "∆mean 1.69 (0.02) 4.17 (0.07) 29.33 (0.75)",
}
for s in rows.values():
    quote(doc, 11, s)
quote(doc, 11, "Entries report means, with medians in parentheses.")
mean = {k: [float(x) for x in v.split()[1::2]] for k, v in rows.items()}

print("\nA mean of sums equals the sum of means, so each column should add up to within rounding (0.01).")
for total, a, b in (("G", "Gcov", "Gmean"), ("D", "Dcov", "Dmean")):
    for j, c in enumerate(cols):
        s = mean[a][j] + mean[b][j]
        print(f"  {c:9s} {a} + {b} = {s:.2f}   {total} = {mean[total][j]:.2f}   gap {mean[total][j] - s:+.2f}")
print("  The G rows add up; the ∆ rows miss by 0.09 (w/o Act.) and 1.59 (PRISM), in units of 10^3.")

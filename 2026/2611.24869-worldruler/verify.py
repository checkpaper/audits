"""Reproduce the Table 1 check on WorldRuler, arXiv:2611.24869v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.24869", "v1", "a7d7d4d7e11e056e5cfd87e423361ad58ef2ba992c37ca35e5c270115a6d7821")

print("Sec. 4.2 (p. 8) and Sec. 4.3 (p. 10)")
quote(doc, 8, "2,900 pairs for training and 300 for testing")
quote(doc, 10, "Uncertain or invalid judgments remain in the corresponding denominators and receive no success credit")
print("Table 1 (p. 11), Habitat rows (RSR: 5 components + avg., FCR: Stages, Order, Goal + avg.)")
rows = {
    "MiniMax-H3": "MiniMax-H3 [22] 78.85 53.37 17.79 9.13 9.62 33.75 11.21 13.64 5.26 10.03",
    "CWM": "CWM [4] 93.85 49.23 3.85 0.77 0.77 29.69 13.52 12.48 16.81 14.27",
    "SWM": "SWM [17] 98.16 68.66 20.74 15.67 17.05 44.06 15.55 17.58 20.82 17.98",
    "WorldRuler": "WorldRuler 98.61 79.72 58.47 37.36 50.83 64.99 52.61 44.38 47.12 48.04",
}
for r in rows.values():
    quote(doc, 11, r)


def attainable(value, n):
    """True if some k/n, as a percentage rounded to two decimals, prints as value."""
    k = round(value * n / 100)
    return any(abs(100 * j / n - value) <= 0.005 + 1e-9 for j in (k - 1, k, k + 1) if 0 <= j <= n)


print("\nHabitat FCR values (Stages, Order, Goal) as k/n with n complete tasks:")
fcr = {m: [float(x) for x in r.split()[-4:-1]] for m, r in rows.items()}
for m, vals in fcr.items():
    smallest = [next(n for n in range(1, 5001) if attainable(v, n)) for v in vals]
    common = [n for n in range(1, 301) if all(attainable(v, n) for v in vals)]
    print(f"  {m:11s} {vals}  smallest n per value {smallest}  common n <= 300: {common or 'none'}")
allv = [v for vals in fcr.values() for v in vals]
shared = [n for n in range(1, 3001) if all(attainable(v, n) for v in allv)]
print(f"  One n <= 3,000 shared by all 12 values: {shared or 'none'}")

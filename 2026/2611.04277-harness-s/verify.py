"""Reproduce the checks on Harness-S, arXiv:2611.04277v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.04277", "v1", "4b2a410fbf444e549708727638098dabbcf394299e36466e93cc980ea704878f")

print("1. Table 1 (p. 7): are the cells means of three runs?")
quote(doc, 7, "Scores are averaged over three independent randomized runs, each with three executor rollouts per task.")
quote(doc, 17, "AppWorld 320 150 262 732 DBBench 1,600 200 300 2,100 SWE-Gym 240 100 160 500")
raw = doc[6].get_text()
raw = raw[raw.index("Frontier models"):raw.index("Experimental Setup")]
cells = re.findall(r"(\d{1,3}\.\d{2})(?:\s*±\s*\d+\.\d{2})?", raw)
if len(cells) != 150:
    sys.exit(f"expected 25 rows x 6 columns, found {len(cells)} numbers")
rows = [cells[i:i + 6] for i in range(0, 150, 6)]
N = [262, 262, 160, 160, 300, 300]  # AppWorld, SWE-Gym, DBBench test tasks, Pass@3 and Avg@3 each


def on_grid(value, n):
    """True if value is k/n (as a percentage, 2 dp) for some whole k."""
    return any(abs(100 * k / n - float(value)) <= 0.005 + 1e-9 for k in range(n + 1))


# One run with three rollouts per task: Pass@3 = k/N and Avg@3 = k/(3N).
# The mean of three runs lands on that grid only when the three counts sum to a multiple of 3.
for metric, cols, mult in (("Pass@3", (0, 2, 4), 1), ("Avg@3", (1, 3, 5), 3)):
    fit = [r[c] for r in rows for c in cols if on_grid(r[c], N[c] * mult)]
    miss = [r[c] for r in rows for c in cols if not on_grid(r[c], N[c] * mult)]
    grid = "k/N" if mult == 1 else "k/(3N)"
    print(f"  {metric}: {len(fit)} of {len(fit) + len(miss)} cells equal {grid}, a single-run value"
          + (f"; not: {', '.join(miss)}" if miss else ""))
print("  For a mean of three runs, about one cell in three would land on that grid.")

print("\n2. Section 4.6 (p. 11): Rank-1 margin over H0 before training")
quote(doc, 11, "The Rank-1 margin over H0 shrinks from 14.21 to 0.76 points in Pass@3")
quote(doc, 10, "H0 42.62 31.93 — 67.56 56.87 — Rank-1 56.87 45.42 1.53 68.32 61.45 22.52")
print(f"  Table 5: 56.87 - 42.62 = {56.87 - 42.62:.2f} (Pass@3 before), 68.32 - 67.56 = {68.32 - 67.56:.2f} (after),"
      f" {45.42 - 31.93:.2f} and {61.45 - 56.87:.2f} (Avg@3)")

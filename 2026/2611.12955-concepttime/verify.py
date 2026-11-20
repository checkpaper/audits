"""Reproduce the check on ConceptTime (Predictive Surprise as Self-Grounding Concept Bottleneck), arXiv:2611.12955v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.12955", "v1", "83d07ccd4d566724fae7e8922aaab134580e5d6ac45894de29e825c468a797ca")

cols = [f"{b} {f}" for b in ("HAR", "Epilepsy", "Sleep-EDF", "UEA") for f in ("1%", "5%", "Full")]
rows = {
    "EntroPE": "71.29 74.14 84.41 85.62 87.61 89.94 70.95 71.84 75.12 56.37 58.27 61.06",
    "TOTEM": "73.86 78.27 83.83 91.65 93.57 94.56 48.29 52.73 67.75 34.96 38.60 52.99",
    "ProSeNet": "47.63 76.38 84.12 65.51 95.06 96.91 36.67 45.40 61.25 49.67 50.32 52.61",
    "VQShape": "59.00 66.00 72.24 81.00 87.00 90.43 51.36 55.96 59.95 54.67 54.81 59.82",
    "catch22": "44.37 53.92 58.87 86.03 87.12 88.34 68.59 69.71 71.36 32.51 35.11 43.29",
    "ConceptTime-Static": "69.81 75.29 83.27 94.24 94.13 95.47 68.26 69.92 73.36 55.98 51.29 67.82",
    "ConceptTime-Dynamic": "74.60 79.60 88.91 97.91 98.01 98.39 70.21 71.92 78.15 58.50 60.10 71.82",
}
print("Table 1 (p. 7)")
for name, vals in rows.items():
    quote(doc, 7, f"{name} {vals}")
rows = {k: [float(x) for x in v.split()] for k, v in rows.items()}
quote(doc, 6, "Interpretable methods: catch22 [38], ProSeNet [43], VQShape [59], TOTEM [55].")

print("\n1. Margins over interpretable methods (Sec. 4.2, p. 7)")
quote(doc, 7, "with margins ranging from 1.5 points (Epilepsy full-shot) to over 30 points (HAR vs. catch22)")
ours = rows["ConceptTime-Dynamic"]
for j, c in enumerate(cols):
    best = max(("TOTEM", "ProSeNet", "VQShape", "catch22"), key=lambda k: rows[k][j])
    print(f"  {c:13s} {ours[j]:.2f} - {best} {rows[best][j]:.2f} = {ours[j] - rows[best][j]:+.2f}")
print("  The smallest margin is HAR 1% over TOTEM, 0.74 points.")

print("\n2. EntroPE ablation (Sec. 4.2, p. 7)")
quote(doc, 7, "loses 4.5-8.5 points across benchmarks")
for j in (2, 5, 8, 11):
    print(f"  {cols[j]:13s} {ours[j]:.2f} - {rows['EntroPE'][j]:.2f} = {ours[j] - rows['EntroPE'][j]:.2f}")
print("  Full-label gaps range from 3.03 (Sleep-EDF) to 10.76 (UEA); at Sleep-EDF 1% EntroPE is ahead (70.95 vs 70.21).")

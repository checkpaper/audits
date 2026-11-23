"""Reproduce the checks on WorldDraft, arXiv:2611.16217v1.

Run: python verify.py
"""
import itertools
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.16217", "v1", "d07e4fb35d075a5fbb4f7be096b7f1f73bd53514c9a97cbca2d0c6ae205260c3")

COLS = ["Preservation", "Realization", "Quality", "Persistence", "Structure", "Appearance", "Binding",
        "Adherence", "Retention", "Penalty", "Leakage", "Overall"]


def fmt(v, i):
    return f"{v:+.2f}" if 4 <= i <= 6 else f"{v:.2f}"


def row(page, label, values):
    quote(doc, page, label + " " + " ".join(fmt(v, i) for i, v in enumerate(values)))
    return values


def interval(base, new):
    """Range of new/base allowed by rounding both printed values to 2 decimals."""
    lo, hi = sorted([(new - 0.005) / (base + 0.005), (new + 0.005) / (base - 0.005)])
    return lo, hi


def most_sharing(base, new, cols):
    """Largest number of the given columns whose ratios share one common factor."""
    iv = [interval(base[c], new[c]) for c in cols]
    return max(sum(lo <= k <= hi for lo, hi in iv) for k in [x for pair in iv for x in pair])


def common(base, new, cols, flip=()):
    """Common factor k for cols (k for normal columns, 2 - k for flip columns), or None."""
    lo, hi = 0, 9
    for c in cols:
        a, b = interval(base[c], new[c])
        if c in flip:
            a, b = 2 - b, 2 - a
        lo, hi = max(lo, a), min(hi, b)
    return (lo, hi) if lo <= hi else None


print("Table 2 (p. 10), rows as printed")
ow = row(10, "OmniWeaving", [61.61, 66.37, 62.02, 58.01, 12.75, -14.47, -15.95, 58.13, 47.68, 10.63, 50.97, 57.62])
ow_pe = row(10, "+ Text PE", [62.63, 67.98, 63.46, 59.36, 12.98, -14.81, -16.32, 60.06, 48.79, 10.30, 49.79, 58.52])
ow_pr = row(10, "+ WorldDraft-Primer", [64.60, 70.93, 66.19, 61.90, 13.51, -15.45, -17.02, 62.97, 50.88, 10.41, 47.55, 60.13])
mm = row(10, "MiniMax-H3", [50.70, 76.38, 64.06, 70.32, 8.01, -0.89, -1.93, 76.41, 70.80, 0.74, 28.64, 63.63])
mm_pe = row(10, "+ Text PE", [51.45, 77.91, 65.34, 71.72, 8.07, -0.91, -1.97, 77.94, 72.22, 0.75, 28.07, 64.89])
mm_pr = row(10, "+ WorldDraft-Primer", [52.55, 80.21, 67.26, 73.84, 8.24, -0.93, -2.02, 80.23, 74.34, 0.78, 27.21, 65.56])

R, Q, P, B, A, ADH, RET, L = 1, 2, 3, 6, 5, 7, 8, 10
cases = [
    ("MiniMax-H3 + Primer / MiniMax-H3", mm, mm_pr, [R, Q, P, ADH, RET]),
    ("MiniMax-H3 + Text PE / MiniMax-H3", mm, mm_pe, [R, Q, P, ADH, RET]),
    ("OmniWeaving + Primer / OmniWeaving", ow, ow_pr, [Q, P, A, B, RET]),
    ("OmniWeaving + Text PE / OmniWeaving", ow, ow_pe, [Q, P, A, B, RET]),
]
for name, base, new, cols in cases:
    print(f"\n{name}")
    for c in cols + [L]:
        print(f"  {COLS[c]:<12} {base[c]:7.2f} -> {new[c]:7.2f}   ratio {new[c] / base[c]:.4f}")
    k = common(base, new, cols + [L], flip=(L,))
    print(f"  One factor k fits all {len(cols)} columns and Leakage = (2 - k) x base: "
          + (f"yes, k in [{k[0]:.4f}, {k[1]:.4f}]" if k else "no"))

print("\nReference: Table 1 (p. 8), every ordered pair of distinct models,")
print("how many of Realization, Quality, Persistence, Adherence, Retention can share one ratio")
t1 = {
    "OmniWeaving 8.3B": [61.61, 66.37, 62.02, 58.01, 12.75, -14.47, -15.95, 58.13, 47.68, 10.63, 50.97, 57.62],
    "UniVideo 13B": [53.34, 67.31, 63.01, 59.10, 15.61, -4.24, -7.43, 63.39, 51.78, 6.02, 52.24, 57.82],
    "VINO 13B": [52.83, 67.95, 63.43, 60.38, 15.99, -2.70, -5.21, 67.34, 56.75, 3.57, 38.26, 59.78],
    "Wan2.1-VACE 14B": [60.97, 60.86, 60.78, 51.68, 18.82, -2.89, -2.68, 60.93, 50.37, 8.05, 64.17, 56.89],
    "Wan2.2-VACE 14B": [60.52, 70.25, 64.11, 62.09, 11.48, -2.37, -4.74, 68.80, 59.18, 3.14, 33.60, 62.43],
    "C2R 14B": [53.05, 71.14, 65.14, 64.96, 15.98, -2.75, -5.65, 69.95, 63.11, 4.45, 43.03, 61.10],
    "Bernini-R 14B": [61.81, 72.41, 63.88, 64.80, 8.45, -3.33, -3.51, 71.17, 62.53, 2.93, 43.16, 62.97],
    "LynnReal-Omni 32B": [60.52, 75.51, 65.48, 68.41, 7.26, -3.62, -5.28, 75.32, 68.05, 2.26, 30.54, 64.89],
    "MiniMax-H3 33B": [50.70, 76.38, 64.06, 70.32, 8.01, -0.89, -1.93, 76.41, 70.80, 0.74, 28.64, 63.63],
    "SolarRenderer 33B": [63.28, 69.97, 62.48, 61.68, 12.25, -1.49, -2.02, 69.43, 60.17, 4.27, 40.37, 62.59],
    "Wan 3.0": [44.37, 80.40, 66.92, 75.41, -0.35, -0.58, -0.16, 79.82, 74.18, 0.53, 27.39, 63.36],
    "Seedance 2.5": [58.66, 75.55, 63.10, 69.20, 10.88, 2.51, 3.21, 76.60, 69.53, 1.97, 41.57, 64.73],
}
for label, v in t1.items():
    row(8, label, v)
counts = [most_sharing(t1[a], t1[b], [R, Q, P, ADH, RET]) for a, b in itertools.permutations(t1, 2)]
print(f"  {len(counts)} pairs; most columns sharing one ratio in any pair: {max(counts)} of 5")
print(f"  Table 2 MiniMax-H3 rows: {most_sharing(mm, mm_pr, [R, Q, P, ADH, RET])} of 5 (Primer), "
      f"{most_sharing(mm, mm_pe, [R, Q, P, ADH, RET])} of 5 (Text PE)")

print("\nFigure 12 (App. C.2, p. 23): ablation on MiniMax-H3")
quote(doc, 23, "Global Count drops from 30.02 to 28.70, Local Count from 45.42 to 43.43, and BBox IoU from 16.70 to 15.97")
quote(doc, 23, "dropping RF from 80.21 to 76.61 and AP from 73.84 to 70.53, while increasing Source Leakage to 26.75%")
print("  Bar labels transcribed from the figure image (Base Model, + WorldDraft-Primer):")
fig = {"Global Count": (28.59, 30.02), "Local Count": (43.26, 45.42), "BBox IoU": (15.91, 16.70),
       "RF": (76.38, 80.21), "AP": (70.32, 73.84), "SL": (26.83, 25.49)}
for name, (base, full) in fig.items():
    print(f"  {name:<12} {base:6.2f} -> {full:6.2f}   ratio {full / base:.4f}")
print("  Base SL in Figure 12 is 26.83; Table 2 gives MiniMax-H3 Leakage 28.64.")

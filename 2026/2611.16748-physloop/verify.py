"""Reproduce the checks on PhysLoop, arXiv:2611.16748v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.16748", "v1", "85f304f9be2f8a58702f0ac5bf05371859a5330f8aa29691f9481a5d95383050")

# Table 1 (p. 7): Phys. Real. Causal Win | PC SA IQ AQ | Gen Repair P-IQ
ROWS = {
    "Gemini Omni": "Gemini Omni 3.11 3.82 3.18 18.94 20.79 39.17 71.17 50.40 49.00 14.67 31.66",
    "H3": "H3 3.63 4.27 3.55 44.93 22.98 38.68 68.47 50.62 53.00 18.00 28.14",
    "Seedance 2.5": "Seedance 2.5 3.80 4.29 3.80 53.79 21.51 38.69 67.63 50.63 73.00 19.33 48.07",
    "Claude Opus 5 + Seedance 2.5": "Claude Opus 5 3.82 3.82 3.84 64.18 20.23 36.69 67.66 49.71 71.00 78.67 53.75",
    "Kimi K3 + Seedance 2.5": "Kimi K3 3.63 3.69 3.69 54.41 19.90 37.32 68.54 50.42 69.00 68.67 52.04",
    "GPT-6 Astra + Gemini Omni": "Gemini Omni 3.53 2.96 3.51 45.45 12.71 35.84 75.11 46.72 67.00 62.00 12.08",
    "GPT-6 Astra + H3": "H3 3.86 3.45 3.90 58.21 17.48 37.12 68.77 48.65 73.00 72.67 39.10",
    "GPT-6 Astra w/o Refiner": "w/o Refiner 3.94 2.59 3.95 34.33 12.53 34.88 72.42 45.75 80.00 60.67",
    "PhysLoop": "PhysLoop 4.06 3.72 4.12 75.76 15.29 36.28 69.93 48.70 85.00 86.00 52.06",
}
vals = {}
for name, row in ROWS.items():
    quote(doc, 7, row)
    vals[name] = [float(x) for x in row.split()[-11:] if x != "–"] if "w/o" not in name else \
        [float(x) for x in row.split()[-10:]]

print("\n1. Win column: protocol")
quote(doc, 9, "Each video is assigned to multiple raters, with method identities hidden and presentation order randomized.")
quote(doc, 7, "Win is computed from 301 unblinded supplementary pairwise comparisons by one author")
quote(doc, 18, "Each pairwise contrast compares a UE-guided output with the direct output of the same video model.")
win = [v[3] for v in vals.values()]
print(f"  The nine Win values sum to {sum(win):.2f} (mean {sum(win) / 9:.2f}), as in a round robin among all nine rows.")

print("\n2. Repair column: 50 tasks, one result each")
quote(doc, 8, "yielding 50 repair tasks")
quote(doc, 8, "allow up to five repeat calls to the video generation model per task and return one final result")
off = []
for name, v in vals.items():
    r = v[9]
    k = r * 50 / 100
    fits = abs(k - round(k)) * 100 / 50 < 0.005
    print(f"  {name:30s} {r:6.2f}  x50 = {k:6.3f}  {'k/50' if fits else 'not k/50'}   x150 = {r * 1.5:6.2f}")
    off += [] if fits else [name]
print(f"  {len(off)} of 9 Repair rates are not k/50.")

print("\n3. 'Highest scores across all human-evaluation dimensions'")
quote(doc, 10, "The full PhysLoop configuration achieves the highest scores across all human-evaluation dimensions")
real = sorted(((v[1], n) for n, v in vals.items()), reverse=True)
print("  Real. ranking:", ", ".join(f"{n} {r:.2f}" for r, n in real))
print(f"  PhysLoop is {[n for _, n in real].index('PhysLoop') + 1} of 9 on visual realism.")

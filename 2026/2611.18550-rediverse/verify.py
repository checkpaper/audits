"""Reproduce the checks on ReDiverse, arXiv:2611.18550v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.18550", "v1", "c5ea0706cc543d6e5df605fd7dd73a04537376be09523ff983bf4a7d5fda1fce")

print("1. Sec. 5.2 (p. 8) against Table 4a (p. 7): ReDiverse versus Noise Optimization")
quote(doc, 8, "surpasses Noise Optimization on all diversity metrics except Vendi for SD3")
metrics = ["DINO", "DS", "LP", "TP", "Vendi"]
rows = {
    "SDXL": ("Noise Opt. 67.0 37.9 71.2 25.1 7.83", "ReDiverse 65.0 33.3 67.9 23.0 7.03"),
    "SD3": ("Noise Opt. 56.9 26.4 61.2 18.3 6.74", "ReDiverse 60.1 28.3 64.9 20.3 6.24"),
}
for backbone, (noise, ours) in rows.items():
    quote(doc, 7, noise)
    quote(doc, 7, ours)
    a = [float(v) for v in noise.split()[2:]]
    b = [float(v) for v in ours.split()[1:]]
    lost = [m for m, x, y in zip(metrics, a, b) if y < x]
    print(f"  {backbone}: ReDiverse below Noise Opt. on {lost or 'none'}")

print("\n2. Table 5a (p. 10) against Table 8 (p. 25): TPIPS_avg for 'Regress at all blocks'")
quote(doc, 10, "Teacher 61.0 21.7 0.885 Student 46.9 13.9 0.955")
quote(doc, 10, "Later block: 16 55.4 +3.8 17.0 +1.6 0.839 −0.095")
quote(doc, 10, "Regress at all blocks 57.8 +6.2 26.6 0.801 −0.133")
quote(doc, 10, "ReDiverse-FT (ℓ=12, t=1) 51.6 15.4 0.934")
quote(doc, 25, "Teacher 61.0 32.9 30.2 6.26 31.8 28.6 0.885")
quote(doc, 25, "Student 46.9 19.7 20.1 3.89 31.9 29.3 0.955")
quote(doc, 25, "Block 12 (default) 51.6 23.3 22.4 4.72 32.0 28.4 0.934")
quote(doc, 25, "Block 16 55.4 25.1 24.2 5.53 31.8 28.2 0.839")
quote(doc, 25, "All blocks 57.8 28.5 26.6 6.05 31.7 27.7 0.801")
pairs = {"Teacher": (21.7, 30.2), "Student": (13.9, 20.1), "Default (block 12)": (15.4, 22.4),
         "Block 16": (17.0, 24.2), "All blocks": (26.6, 26.6)}
print(f"  {'row':20s} Tab.5 TPIPS_avg  Tab.8 TPIPS  difference")
for name, (avg, overall) in pairs.items():
    print(f"  {name:20s} {avg:14.1f} {overall:12.1f} {overall - avg:11.1f}")

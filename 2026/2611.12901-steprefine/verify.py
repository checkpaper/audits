"""Reproduce the checks on Rethinking in Spikes (StepRefine), arXiv:2611.12901v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.12901", "v1", "189a6ab954a2cd582e9a9dc24ed74bcba201b1bf1fbd5af1dff8d0d1436f95b7")

print("Default setting (Sec. 4.1, p. 6)")
quote(doc, 6, "Across all backbones and benchmarks, we decode with generation length L = 256, total denoising steps T = 256, and low-confidence remasking.")

print("\n1. Dream-VL-7B MMHalu baseline at the default setting")
quote(doc, 6, "MMHalu 3.35 3.39 3.25 3.43 3.50 (+2.5) 3.76 4.01 (+4.2) 3.54 3.68 (+2.3) 2.38 2.54 (+2.7)")
quote(doc, 21, "Low Confidence 3.47 3.68")
quote(doc, 21, "Base 3.37 3.54 3.47 3.18 3.69 3.58 StepRefine 3.55 3.63 3.68 3.72 3.86 3.67")
print("  Table 1 (columns: LLaDA-V x5, LLaDA-O, Dream-VL, LaViDa-L): Dream-VL Base 3.54, StepRefine 3.68")
print("  Table 5(a) low confidence and Table 5(b) L = 256, T = 256: Base 3.47, StepRefine 3.68")
print("  3.54 is the Table 5(b) Base value at T = 128. Gain: +0.14 in Table 1 vs +0.21 in Table 5.")

print("\n2. Fig. 2(c) 'Low-confidence' reference bars (p. 4) versus Table 1 LLaDA-V (p. 6)")
quote(doc, 4, "(a) (b) 56.5 52.7 59.2 58.6 56.5 59.2 58.6 55.9 55.0 55.7 58.8 58.1")
quote(doc, 4, "Top: replacing low-confidence remasking with random remasking at 10% of randomly selected steps")
rows = {"VStar": "VStar 55.5 57.1 56.5 56.5 58.6", "RealWorldQA": "RealWorldQA 57.5 58.3 58.8 58.6 59.2",
        "MathVista": "MathVista 54.7 55.2 54.6 55.9 56.5"}
for r in rows.values():
    quote(doc, 6, r)
fig = page_text(doc, 4).split("(a) (b) ")[1].split(" (c)")[0].split()
print(f"  Fig. 2(c) bar labels: {' '.join(fig)}")
print("  Values drawn in both panels (the Low-confidence reference): 56.5, 59.2, 58.6")
for name, r in rows.items():
    v = r.split()[1:]
    print(f"  {name:11s} Table 1 LLaDA-V Base {v[0]}, StepRefine {v[4]}")
print("  The reference bars equal Table 1 StepRefine (58.6 / 59.2 / 56.5), not the low-confidence Base (55.5 / 57.5 / 54.7).")

"""Reproduce the check on ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents, arXiv:2611.31198v1.

Run: python verify.py
"""
import itertools
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.31198", "v1", "774b679c4f74f5ddf466c097951da2ee5febb146f012750a48411547859df20b")

print("Claim")
quote(doc, 6, "every reported number is the mean of three independent runs.")

print("\nSample counts, Table 8 (p. 13)")
for phrase in ["InfoSeek (Chen et al., 2023) 2000", "MM-BrowseComp (Li et al., 2025) 243", "VisBrowse-Bench (Zhang et al., 2026b) 169"]:
    quote(doc, 13, phrase)

print("\nRows (Table 2 p. 6, Table 3 p. 7)")
quote(doc, 6, "Qwen3-VL-32B 64.55 56.99 50.47 57.14")
quote(doc, 6, "GPT-5 56.10 53.04 49.64 52.84")
quote(doc, 7, "Qwen3-VL-8B 6.00 70.00 51.46 9.97 7.27 40.00 32.33 34.71 14.40 11.24 26.57")
quote(doc, 7, "Qwen3-VL-8B 7.00 71.00 55.56 11.58 7.27 42.67 33.08 34.54 16.60 11.22 27.90")

cells = [
    ("Table 2, Qwen3-VL-32B + ToolSmith, InfoSeek", 56.99, 2000),
    ("Table 2, GPT-5 + ToolSmith, InfoSeek", 53.04, 2000),
    ("Table 3, Qwen3-VL-8B base tools, MM-BC", 6.00, 243),
    ("Table 3, Qwen3-VL-8B + ToolSmith, VisBrowse", 11.22, 169),
]
print("\nA mean of three runs on n items is k / (3n) for an integer k.")
print("Also tried: each run's accuracy rounded to 2 decimals before averaging.")
for name, v, n in cells:
    k0 = round(v * 3 * n / 100)
    near = ", ".join(f"{100 * k / (3 * n):.4f}" for k in (k0 - 1, k0, k0 + 1))
    runs = [round(100 * k / n, 2) for k in range(round(v * n / 100) - 40, round(v * n / 100) + 41)]
    hit = any(abs(round(sum(c) / 3, 2) - v) < 1e-9 for c in itertools.combinations_with_replacement(runs, 3))
    print(f"  {name}: {v:.2f} (n = {n}); nearest means {near}; reachable with per-run rounding: {hit}")

print("\nClaim on the 8B OOD gains")
quote(doc, 6, "8B improves on eight of the ten, with the remaining two essentially flat.")
quote(doc, 7, "∆ +1.00 +1.00 +4.10 +1.61 0.00 +2.67 +0.75 −0.17 +2.20 −0.02 +1.33")
d = [1.00, 1.00, 4.10, 1.61, 0.00, 2.67, 0.75, -0.17, 2.20, -0.02]
print(f"  positive deltas: {sum(x > 0 for x in d)} of 10; zero or negative: {[x for x in d if x <= 0]}")

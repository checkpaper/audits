"""Reproduce the check on FoundSurface, arXiv:2611.34128v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.34128", "v1", "248a53370f054df0e9e38af2709fac1c1b9f0f85903d47d9e2eca7392b303008")

COLS = "ADE RMSE Abs-Rel Sq-Rel delta"

print("Table 12 (p. 18): standard deviations, ScanNet++ | 7Scenes | MultiScan (5 metrics each)")
sd = {
    "Projection [78]": "±0.129 ±0.170 ±0.103 ±0.134 ±0.127 ±0.073 ±0.155 ±0.032 ±0.056 ±0.042",
    "PriorDA [83]": "±0.129 ±0.170 ±0.103 ±0.134 ±0.127 ±0.047 ±0.082 ±0.183 ±0.017 ±0.042",
    "CUT3R [80]": "±0.146 ±0.190 ±0.135 ±0.200 ±0.200 ±0.045 ±0.092 ±0.025 ±0.028 ±0.040",
    "RayletDF [84]": "±0.145 ±0.229 ±0.121 ±0.385 ±0.080 ±0.045 ±0.092 ±0.025 ±0.028 ±0.040",
}
for name, vals in sd.items():
    quote(doc, 18, f"{name} {vals}")

print("\nTable 1 (p. 6): means, ScanNet++ | 7Scenes")
mean = {
    "Projection [78]": "0.580 0.959 0.360 0.554 0.636 0.188 0.391 0.091 0.078 0.887",
    "PriorDA [83]": "0.198 0.290 0.123 0.101 0.868 0.154 0.266 0.074 0.034 0.913",
    "CUT3R [80]": "0.335 0.446 0.222 0.173 0.703 0.197 0.305 0.105 0.054 0.878",
    "RayletDF [84]": "0.179 0.334 0.119 0.205 0.896 0.158 0.295 0.084 0.049 0.907",
}
for name, vals in mean.items():
    quote(doc, 6, f"{name} {vals}")


def block(s, i):
    return s.split()[5 * i:5 * i + 5]


print()
for a, b, i, ds in [("Projection [78]", "PriorDA [83]", 0, "ScanNet++"), ("CUT3R [80]", "RayletDF [84]", 1, "7Scenes")]:
    same = block(sd[a], i) == block(sd[b], i)
    print(f"{ds}: {a} and {b} standard deviations identical in all 5 metrics ({COLS}): {same}")
    print(f"  {a} {' '.join(block(sd[a], i))}")
    print(f"  {b} {' '.join(block(sd[b], i))}")
    print(f"  Their Table 1 means: {' '.join(block(mean[a], i))} vs {' '.join(block(mean[b], i))}")

"""Reproduce the checks on Evolving Infra, arXiv:2611.12304v2.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.12304", "v2", "84f4d8948bf0decb9336b0e5a2ea670c693b924aaa42950a3eb7428854f0c269")

print("1. CC with 126 agents, Evolving Infra starting from 6P3D: main result versus ablation")
quote(doc, 12, "Both start from the prefill-heavy split 6P3D")
quote(doc, 29, "126 2.14 54.4 18.6 5.85 13.2 14.1")
quote(doc, 13, "3P6D 4P5D 5P4D 6P3D 0 5 10 15 Latency (s) 11.2 11.3 11.4 11.4 (a) Initial PD split")
quote(doc, 13, "4.57 6.27 6.25 (b) Online adaptation")
quote(doc, 13, "CC with 126 concurrent agents")
print(f"  Mean E2E: 13.2 s (Table C.3) vs 11.4 s (Fig. 8a, from 6P3D): {13.2 / 11.4 - 1:.1%} higher in the main result")
quote(doc, 14, "Enabling online phase-split adaptation at the best static split lowers the throughput by only 0.3%")
print(f"  Throughput: 5.85 req/s from 6P3D (Table C.3) vs 6.25 req/s from 4P5D (Fig. 8b); the planner converges to 4P5D in all four Fig. 8a runs")
quote(doc, 14, "In all four runs, the planner converges to 4P5D")
quote(doc, 14, "its mean E2E latency varies by at most 1.8%")
print(f"  Fig. 8a spread: {11.4 / 11.2 - 1:.2%}; 13.2 s would be {13.2 / 11.2 - 1:.1%} above the 3P6D run")

print("\n2. N_branch from Little's law, X = N_branch / (E2E + pause)")
quote(doc, 29, "for example 159 and 161 on CC with 126 concurrent agents")
for name, x, e, p in (("Dynamo", 2.14, 54.4, 18.6), ("Evolving Infra", 5.85, 13.2, 14.1)):
    lo, hi = (x - 0.005) * (e - 0.05 + p - 0.05), (x + 0.005) * (e + 0.05 + p + 0.05)
    print(f"  {name}: {x} x ({e} + {p}) = {x * (e + p):.1f}, range with rounding [{lo:.1f}, {hi:.1f}]")
print("  Table C.3 gives about 156 and 160; 161 is outside both ranges, and 159 fits Evolving Infra but not Dynamo.")

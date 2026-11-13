"""Reproduce the check on Hybrid Computer Use, arXiv:2610.41432v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.41432", "v1", "3b383495866c103b7319da516f6fbf1b2b5dd336c55664d848c7658e0ea64bf2")

print("Cost per task for the same GPT-5.4 OSWorld 1.0 runs in Table 2 (p. 8) and Table 4 (p. 16)")
quote(doc, 19, "three runs for all five GPT-5.4 ablation configurations")
quote(doc, 19, "Cost at provider list prices")
quote(doc, 8, "Configuration Score (%) ↑Steps ↓Input (M) ↓Time (s) ↓Cost ($) ↓ HCU 65.59 28.60 0.941 351.3 2.52")
quote(doc, 8, "CUA Driver 62.30 40.74 2.181 500.8 5.65")
quote(doc, 16, "CUA Driver and Evaluated HCU: mean of three runs.")
quote(doc, 16, "Input tokens (K) 2,174.5 927.1 717.7")
quote(doc, 16, "Cost ($) 0.983 0.504 0.402")
t2 = {"HCU": (65.59, 0.941, 2.52), "CUA Driver": (62.30, 2.181, 5.65)}   # score, input M tokens, cost
t4 = {"HCU": (65.77, 0.9271, 0.504), "CUA Driver": (62.47, 2.1745, 0.983)}
for k in t2:
    print(f"  {k:10}: score {t2[k][0]} vs {t4[k][0]}, input {t2[k][1]}M vs {t4[k][1]}M, cost ${t2[k][2]} vs ${t4[k][2]} "
          f"({t2[k][2] / t4[k][2]:.2f}x)")
print(f"  HCU cost saving over CUA Driver: {1 - 2.52 / 5.65:.1%} (Table 2) vs {1 - 0.504 / 0.983:.1%} (Table 4)")

"""Reproduce the check on ODE Policy (Robot Learning via Action Dynamics, Not Actions), arXiv:2611.01729v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.01729", "v1", "b4654b6bbb5decfc7cac94d19ea721adfb2744ba5990a0e9b0888c34cfc65f5a")

print("1. Baseline of the gripper-in-ODE ablation (Sec. 9.3, p. 21)")
quote(doc, 21, "the success rate drops from 79.2%, 95.0%, and 92.8% to 74.5%, 91.8%, and 92.2% at epochs 1, 5, and 10")
print("\nTable S7 (p. 34): default ODE-MLP at epochs 1 / 10 / 100")
quote(doc, 34, "ODE-MLP (ours) FiLM-MLP 79.2 93.9 93.8")
print("\nTable S8 (p. 34): diversity head, epochs 1 / 5 / 10 / 20")
quote(doc, 34, "No offset 85.3±1.9 (98/81/91/72) 95.0±1.0 (99/97/96/87) 92.8±1.0")
quote(doc, 34, "Component mean (ours) 79.8±1.6 (98/78/83/60) 94.8±0.4 (100/97/96/87) 94.3±1.3")
print("95.0 and 92.8 are the 'No offset' row; the default ('Component mean (ours)') gives 94.8 and 94.3, and Table S7 gives 93.9 at epoch 10.")
for name, base in (("as stated", (79.2, 95.0, 92.8)), ("default", (79.2, 94.8, 94.3))):
    drops = [round(b - a, 1) for b, a in zip(base, (74.5, 91.8, 92.2))]
    print(f"  drop vs {name:9s}: {drops}")

print("\n2. Boundary-to-inside acceleration ratio on the real cup task (Table S5, p. 32)")
quote(doc, 32, "Acceleration at chunk boundaries (rad/s2) 1.04 0.29 ± 0.06 6.40 ± 0.82 10.9 ± 4.5")
quote(doc, 32, "Acceleration inside chunks (rad/s2) 1.09 0.34 ± 0.06 3.15 ± 0.10 4.02 ± 2.30")
quote(doc, 32, "Boundary to inside ratio 0.96 0.86 2.03 2.97")
for name, b, i, r in (("Demonstrations", 1.04, 1.09, 0.96), ("ODE policy", 0.29, 0.34, 0.86), ("FM-DiT", 6.40, 3.15, 2.03), ("DDIM-UNet", 10.9, 4.02, 2.97)):
    print(f"  {name:14s} {b} / {i} = {b / i:.2f}   printed {r}")
print("The other three ratios match the two rows within rounding; DDIM-UNet gives 2.71 vs the printed 2.97 (a per-trial mean of ratios could differ).")

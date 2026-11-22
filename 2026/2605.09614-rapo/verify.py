"""Reproduce the check on RAPO (Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning), arXiv:2605.09614v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2605.09614", "v1", "b43992811f81d12c79ec61900d8fd33564d43f6a84fae13aab3064659c0270c1")

print("App. G.3, Table 10 (p. 32): averages under greedy and temperature-1 decoding")
for row in (
    "Base greedy 13.16 26.78 14.50 31.25 18.90 58.82 27.24",
    "Base temp=1 27.30 36.75 26.87 47.13 24.44 60.47 37.16",
    "GRPO greedy 11.51 27.41 13.75 32.81 22.49 59.22 27.87",
    "GRPO temp=1 28.29 44.35 28.50 48.71 30.61 64.28 40.79",
    "greedy 16.12 33.63 15.50 33.71 25.55 63.92 31.41",
    "temp=1 33.55 46.13 31.25 49.55 32.20 65.36 43.01",
):
    quote(doc, 32, row)
avg = {"Base": (27.24, 37.16), "GRPO": (27.87, 40.79), "RAPO": (31.41, 43.01)}
quote(doc, 32, "smaller for RAPO, 11.46, than for GRPO, 12.92")
for m, (g, s) in avg.items():
    print(f"  {m:4s} gap = {s:.2f} - {g:.2f} = {s - g:.2f}")
print("RAPO's gap is 11.60, not 11.46; the Base model has the smallest gap (9.92).")

print("\nTable 1 (p. 6, temperature 1) and Table 12 (p. 33, DAPO group at temperature 0.6): Base row")
quote(doc, 29, "we set the sampling temperature to 1.0")
base = "Base 41.74 50.21 38.34 62.28 37.59 67.20 49.56"
quote(doc, 6, base)
quote(doc, 33, "except that the temperature is set to 0.6")
quote(doc, 33, base)
print("The Base row is identical in both tables although the evaluation temperatures differ.")

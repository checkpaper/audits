"""Reproduce the checks on MemOnce, arXiv:2611.27973v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.27973", "v1", "c20be4e83216c120d5bca104f42c2c4be78f278ad27241814261dbfd49046c81")

print("1. Sec. 5 (p. 8) versus the full 400M table (p. 26)")
quote(doc, 8, "MemOncer=1 and MemOncer=8 attain the highest and second-highest average zero-shot accuracies across all evaluated architectures")
quote(doc, 8, "MemOncer=8 (Ours) 21.08 32.45 34.0 67.8 41.9 51.8 52.3 27.7 81.7 61.6 52.35")
quote(doc, 26, "Kimi-Linear (Kimi Team et al., 2026) 315M 11.15 14.22 26.70 33.44 223.33 0.664 0.402 0.521 0.531 0.284 0.840 0.602 0.357 0.5250")
quote(doc, 26, "MemOnce (r = 8) 400M 10.89 14.05 21.08 32.45 151.80 0.678 0.419 0.518 0.523 0.277 0.817 0.616 0.340 0.5235")
kimi = [0.664, 0.402, 0.521, 0.531, 0.284, 0.840, 0.602, 0.357]
print(f"  Kimi-Linear Avg from its eight values: {sum(kimi) / 8:.4f} (printed 0.5250), above MemOnce r=8 0.5235;"
      " Kimi-Linear is not a row of Table 2")

print()
print("2. Scaling table (p. 24), ~600M MemOnce r = 8 row")
quote(doc, 24, "MemOnce (r = 8) 603M 10.34 12.87 19.52 31.04 144.66 0.680 0.437 0.527 0.546 0.299 0.848 0.597 0.355 0.5392")
row = [0.680, 0.437, 0.527, 0.546, 0.299, 0.848, 0.597, 0.355]
print(f"  mean of the eight task values: {sum(row) / 8:.4f} (printed 0.5392; rounding of the inputs allows at most 0.0005)")
quote(doc, 24, "MemOnce (r = 1) 603M 10.16 12.35 18.08 30.70 139.43 0.673 0.440 0.530 0.551 0.301 0.845 0.591 0.396 0.5409")
r1 = [0.673, 0.440, 0.530, 0.551, 0.301, 0.845, 0.591, 0.396]
print(f"  for comparison, r = 1 row: {sum(r1) / 8:.4f} (printed 0.5409)")

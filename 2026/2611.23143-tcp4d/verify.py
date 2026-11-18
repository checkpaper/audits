"""Reproduce the check on TCP4D, arXiv:2611.23143v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.23143", "v1", "85ec653efce2e4c42ab89c56fa1997d463710b18d20e5b9604d699634cf06e8d")

print("Abstract (p. 1)")
quote(doc, 1, "joint training on source and augmented demonstrations improves target-robot success by 41.5% over augmented-only training")
print("Sec. 4.3 (p. 9): augmented-only versus joint training")
quote(doc, 9, "On ARX-X5, joint training increases the mean success rate from 30.5% to 72.0% relative to augmented-only training.")
quote(doc, 9, "On UR5-WSG, joint training improves the mean success rate from 32.0% to 39.0%")

arx, ur5 = (30.5, 72.0), (32.0, 39.0)
print(f"\n  ARX-X5 gain:  {arx[1] - arx[0]:.1f} pp ({arx[1] / arx[0] - 1:.0%} relative)")
print(f"  UR5-WSG gain: {ur5[1] - ur5[0]:.1f} pp ({ur5[1] / ur5[0] - 1:.0%} relative)")
m0, m1 = (arx[0] + ur5[0]) / 2, (arx[1] + ur5[1]) / 2
print(f"  mean of the two target robots: {m0:.2f}% -> {m1:.2f}% = {m1 - m0:.2f} pp ({m1 / m0 - 1:.0%} relative)")

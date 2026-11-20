"""Reproduce the check on CHORD, arXiv:2611.22668v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.22668", "v1", "99a8228f079ec259e71b13e7eafa0ceee8134d987ad89d261b790ca666ffd9ad")

print("CelebA target-only WGA: Tables 4 and 5 (p. 7) vs Discussion (p. 8)")
quote(doc, 7, "We report mean WGA over ten random seeds.")
quote(doc, 7, "Single View ✓ 84.27")
quote(doc, 7, "Target Only: 84.27")
quote(doc, 7, "CHORD: 89.06")
quote(doc, 8, "On CelebA, we keep the ERM model and the final transformation fixed")
quote(doc, 8, "Target-only achieves 82.39% WGA")
quote(doc, 8, "Pretrained versus random partitions yield 89.06")
print("\nTable 1 (p. 6), NSF row")
quote(doc, 6, "NSF[28] ✗ ✗ 95.65 91.12 88.70 84.27")
print("\n  Both settings use the same ERM model, 10 classifier seeds and give CHORD 89.06,")
print(f"  but target-only is 84.27 in Tables 4-5 and 82.39 in the Discussion ({84.27 - 82.39:+.2f}).")
print("  84.27 is also the CelebA WGA of the NSF baseline in Table 1.")

"""Reproduce the check on Calpha, arXiv:2611.20986v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.20986", "v1", "3ea168a388463fc11e3e38cd5c0f2f1f787c1fb6a1ed1312413aa3c99d7e7645")

print("Table 4 (p. 6): BioMatrix-4B mean TM-score on CAMEO-2025, all 200 targets")
quote(doc, 6, "CAMEO-2025")
quote(doc, 6, "(334) (128) (155) (70) (200) (16)")
quote(doc, 6, "BioMatrix-4B‡ 0.158 0.164 0.163 0.161 0.311 0.145")
print("Sec. 4.4 (p. 7): split into 15 verbatim training sequences and 185 others")
quote(doc, 7, "15 sequences occur verbatim in the public BioMatrix training set. Its 4B model scores 0.96 on these and 0.28 on the other 185.")

mean = (15 * 0.96 + 185 * 0.28) / 200
low = (15 * 0.955 + 185 * 0.275) / 200
print(f"\n  (15 x 0.96 + 185 x 0.28) / 200 = {mean:.4f}   (Table 4: 0.311)")
print(f"  lowest mean the rounded values allow = (15 x 0.955 + 185 x 0.275) / 200 = {low:.4f}")
print(f"  with mean 0.311 and 15 targets at 0.96, the other 185 average {(200 * 0.311 - 15 * 0.96) / 185:.3f}")

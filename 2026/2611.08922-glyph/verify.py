"""Reproduce the check on Glyph, arXiv:2611.08922v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.08922", "v1", "662d39941fa302f223eb309e021bb3c591757439cf530e51ccf939217e96af7c")

print("1. Glyph vs Phecodes: introduction (p. 4) and supplement (p. 38)")
quote(doc, 4, "Internal Test (69.3% vs. 49.1%, p = 9.77")
quote(doc, 4, "External Site #1 (74.3% vs. 63.9%, p = 2.93")
quote(doc, 38, "Internal Test (47.2% vs. 69.3%, p = 9.77")
quote(doc, 38, "External Site #1 (59.9% vs. 74.3%, p = 1.95")
quote(doc, 38, "of which 49.1% and 63.9% reproduced in the two held-out cohorts")
print("  The supplement gives p = 9.77e-4 and 1.95e-3 for the Recent Phecode arm (47.2%, 59.9%).")
print("  The introduction pairs 9.77e-4 and 2.93e-3 with the all-history arm (49.1%, 63.9%);")
print("  p = 2.93e-3 appears only in the introduction.")

print("\n2. External Site #2 average (Figure 2, p. 7; Results, p. 8)")
quote(doc, 8, "well above the 33.8% cohort average at External Site #2")
quote(doc, 7, "External Site 2 (n=14,199) Discovery reproduced? 290 (33.8%) 1,411 (62.7%) N/A 1,701 (54.7%)")
quote(doc, 7, "Report findings 467,415 858 Image 48,363 2,251")
rep, img = 858, 2251
print(f"  Report findings row: 290 / {rep} = {290 / rep:.1%}")
print(f"  All tested at External #2: 1,701 / {rep + img:,} = {1701 / (rep + img):.1%}")
print("  33.8% is the report-findings rate; the cohort-wide rate in Figure 2 is 54.7%.")

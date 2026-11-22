"""Reproduce the check on Click3R (Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks), arXiv:2611.12875v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.12875", "v1", "73ff83e96415b0d8323c35e83cab743ff7d316afe08ac1d4c37c69facbbccf62")

print("Click3R with no clicks, as reported in different tables\n")
print("Table 2 (p. 7): Hard3DBench 2-view mAA@30, in-distribution (404 pairs) and out-of-distribution (300 pairs)")
quote(doc, 7, "In-Distribution (404 pairs / 400 tuples)")
quote(doc, 7, "CLICK3R w/o prompts 55.3 0.244 38.8 2.121")
quote(doc, 7, "CLICK3R w/o prompts 50.8 0.781 54.7 0.310")

print("\nTable 3 (p. 9): the 100 OOD pairs with human clicks")
quote(doc, 9, "CLICK3R w/o prompts 17.30° 13.0% 47.0% 4.6 21.5 36.2")

print("\nTable 11 (p. 20): same 100 pairs")
quote(doc, 20, "On the 100 pairs of Table 3")
quote(doc, 20, "No prompts 18.64° 35.6")

print("\nTable 12 (p. 20): K = 0 clicks on the same 404 / 300 / 100 pairs")
quote(doc, 20, "H3B: Hard3DBench 2-view (404 ID, 300 OOD pairs)")
quote(doc, 20, "K =0 55.9 49.4 35.6")

rows = [
    ("H3B ID mAA@30", 55.3, 55.9),
    ("H3B OOD mAA@30", 50.8, 49.4),
    ("100-pair mAA@30", 36.2, 35.6),
    ("100-pair medRRE", 17.30, 18.64),
]
print()
for name, a, b in rows:
    print(f"  {name:16s} Table 2/3: {a:6.2f}   Table 11/12: {b:6.2f}   diff {b - a:+.2f}")
print("With K = 0 no clicks are sampled, yet each of the four numbers differs between tables.")

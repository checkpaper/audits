"""Reproduce the check on GlyphAtlas, arXiv:2611.20192v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.20192", "v1", "2835d437dbd9cb949fc0f40b51a7ab92719b5f7d476a4115a3bf7e3856a0e331")

print("Table 1 (p. 6), GlyphAtlas row and FLUX-Text row")
quote(doc, 6, "GlyphAtlas 88.68 0.9555 11.99 0.0759 77.92 0.8806 11.50 0.0534")
quote(doc, 6, "FLUX-Text [13] 84.19 0.9400 13.85 0.0729 71.32 0.8510 13.68 0.0541")
print("Table S6 (p. 18), 64-px rows of the Fixed and Random models")
quote(doc, 18, "Fixed 64 88.48 0.9552 12.00 0.0759 77.77 0.8806 11.50 0.0574")
quote(doc, 18, "Random 64 88.68 0.9555 12.27 0.0756 77.92 0.8802 11.90 0.0574")

cols = ["EN ACC", "EN NED", "EN FID", "EN LPIPS", "ZH ACC", "ZH NED", "ZH FID", "ZH LPIPS"]
t1 = [88.68, 0.9555, 11.99, 0.0759, 77.92, 0.8806, 11.50, 0.0534]
fixed = [88.48, 0.9552, 12.00, 0.0759, 77.77, 0.8806, 11.50, 0.0574]
rand = [88.68, 0.9555, 12.27, 0.0756, 77.92, 0.8802, 11.90, 0.0574]
print()
for c, a, f, r in zip(cols, t1, fixed, rand):
    src = " and ".join(n for n, v in (("Fixed", f), ("Random", r)) if v == a) or "neither"
    print(f"  {c:9s} Table 1 {a:<7}  Fixed {f:<7}  Random {r:<7}  matches {src}")

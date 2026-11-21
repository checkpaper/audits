"""Reproduce the check on Accord (Universal Online Metric Localization and Dense Mapping), arXiv:2611.25279v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.25279", "v1", "51746acc3510c4ee25068ee4ddf5df68872a3b8156dfc89f49666ee3d82884c3")

print("App. D, 'Two settings of the filter' (p. 15)")
quote(doc, 15, "the setting with the lowest mean error at the control points was taken (Tab. 13)")
quote(doc, 15, "the densities as measured and the walks at three times their bounds")

print("\nTable 13 (p. 17), mean RMSE (m) at the control points")
quote(doc, 17, "densities as measured, ×1 / 1.5 / 2 / 3 0.167 / 0.201 / 0.296 / 0.415")
quote(doc, 17, "and walks at their bounds, ×1 / 3 / 10 0.154 / 0.159 / 0.173")
walks = {"x1": 0.154, "x3": 0.159, "x10": 0.173}
best = min(walks, key=walks.get)
print(f"  lowest walk setting: {best} ({walks[best]}); chosen: x3 ({walks['x3']})")

# The chosen value is the one set in bold in Table 13.
page = doc[16]
bold = [s["text"].strip() for b in page.get_text("dict")["blocks"] for l in b.get("lines", []) for s in l["spans"]
        if "0.15" in s["text"] and ("Medi" in s["font"] or s["flags"] & 16)]
print(f"  bold in Table 13: {bold}")

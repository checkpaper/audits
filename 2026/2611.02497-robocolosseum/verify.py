"""Reproduce the check on RoboColosseum, arXiv:2611.02497v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.02497", "v1", "6a1d567b54e5171b0bf2a3e8342cd813c0cc1e1843c37059c3483886aadb265c")

print("Section 4.2 (p. 10) versus Figure 5 (p. 11)")
quote(doc, 10, "with expected comparison scores ranging from 58% to 77%")
quote(doc, 10, "its observed task success rates range from only 6% to 13%, and no evaluated system exceeds 13% success in any category")
text = page_text(doc, 11)
a = text[:text.index("(a) Relative Performance")]
c = text[text.index("(b) Mean Normalized Progress"):text.index("(c) Success Rate")]
scores = [int(x) for x in re.findall(r"(\d+) ?±", a)]
success = [int(x) for x in re.findall(r"(\d+)±", c)]
if len(success) != 48:
    sys.exit(f"expected 8 systems x 6 categories in panel (c), found {len(success)}")
print(f"  Panel (a), first row (MolmoAct2): {scores[:6]}, range {min(scores[:6])} to {max(scores[:6])}")
print(f"  Panel (a): 77 appears {scores.count(77)} times among all {len(scores)} scores")
print(f"  Panel (c), first row (MolmoAct2) success: {success[:6]}, range {min(success[:6])} to {max(success[:6])}")
print(f"  Panel (c) cells above 13%: {sorted(v for v in success if v > 13)}")

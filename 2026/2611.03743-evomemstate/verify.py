"""Reproduce the check on EvoMemState, arXiv:2611.03743v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.03743", "v1", "8d92f7dd8ca1de068c7dff75f8323d616d736341c2d8fbf97995436aeed2801a")

print("Table 1 (p. 6): MemTrapBench Avg. versus the mean of its four scenario columns")
quote(doc, 6, "Avg. ↑ Safety Score ↑ CogBias Acc. ↑ Bound. Acc. ↑ Trauma Acc. ↑ Avg. ↑")
text = page_text(doc, 6)
table = text[:text.index("Table 1:")]
# Each row: method name, 5 MemSyco values, 4 MemTrap scenarios + Avg, 4 LoCoMo values, Overall.
rows = re.findall(r"([A-Z][A-Za-z0-9\- ]+?(?: \([^)]*\))?) ((?:\d+\.\d ){14}\d+\.\d)", table)
if len(rows) != 20:
    sys.exit(f"expected 20 rows (10 methods x 2 backbones), found {len(rows)}")
for i, (name, nums) in enumerate(rows):
    v = [float(x) for x in nums.split()]
    scen, avg = v[5:9], v[9]
    mean = sum(scen) / 4
    ok = abs(mean - avg) <= 0.05 + 1e-9
    model = "Qwen3-8B" if i < 10 else "GPT-4o-mini"
    if not ok:
        print(f"  {model} {name.strip()}: scenarios {scen} average {mean:.2f}, printed Avg. {avg}  <- differs")
fits = sum(abs(sum(float(x) for x in n.split()[5:9]) / 4 - float(n.split()[9])) <= 0.05 + 1e-9 for _, n in rows)
print(f"  {fits} of 20 rows: printed Avg. equals the mean of the four scenarios (to 0.05)")

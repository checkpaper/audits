"""Reproduce the checks on DeepSeek-V4.1-Flash, arXiv:2609.19969v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2609.19969", "v1", "0cfdda19c8e1691b5226dd0d4949e2397051268e8a823c2fb61db94ea20c4ac0")

print("\n1. World knowledge versus V4-Pro-Base")
quote(doc, 6, "achieves world knowledge, reasoning and coding abilities comparable to DeepSeek-V4-Pro-Base")

# Table 1, p. 24. Columns: V4-Flash-Base, V4-Pro-Base, V4.1-Flash-Base.
text = page_text(doc, 24)
rows = ["AGIEval (EM)", "MMLU-Pro (EM)", "C-Eval (EM)", "MultiLoKo (LLM-Judge)",
        "Simple-QA verified (EM)", "SuperGPQA (EM)"]
behind = 0
for name in rows:
    m = re.search(re.escape(name) + r" \S+ ([\d.]+) ([\d.]+) ([\d.]+)", text)
    if not m:
        sys.exit(f"p. 24: row not found: {name}")
    flash, pro, new = map(float, m.groups())
    behind += new < pro
    print(f"  {name:26} V4-Pro-Base {pro:5.1f}  V4.1-Flash-Base {new:5.1f}  {'behind' if new < pro else 'ahead'}")
print(f"  V4.1-Flash-Base trails V4-Pro-Base on {behind} of {len(rows)} World Knowledge rows (Table 1, p. 24)")

print("\n2. The 5% to 10% held-out improvement")
quote(doc, 6, "delivers 5%–10% improvements on held-out evaluations")
# Figure 6, p. 25, is a raster image. Values below are its printed bar labels.
bpb = {  # task: (V4-Flash-Base, V4-Pro-Base, V4.1-Flash-Base)
    "Internal Docs": (0.617, 0.59, 0.564),
    "Internal Code Repos": (0.1562, 0.1494, 0.1443),
    "Academic Materials": (0.4929, 0.4677, 0.4305),
}
for task, (flash, pro, new) in bpb.items():
    print(f"  {task:20} BPB reduction vs V4-Pro-Base {100 * (pro - new) / pro:4.1f}%"
          f"   vs V4-Flash-Base {100 * (flash - new) / flash:4.1f}%")

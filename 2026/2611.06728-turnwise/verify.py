"""Reproduce the check on Turns Matter: Advancing Streaming Video RL via Turn-Level Credit (TurnWise), arXiv:2611.06728v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.06728", "v1", "bccb1e9a5aa0c208e8c08be05a651ee005fc0d0a929cf169f9639ca525ed8042")

quote(doc, 8, "Method ProactiveVQA OVO-Timing StreamingBench PAUC ↑ Timing F1 ↑ RealTime Acc. ↑ Proactive Acc. ↑ Avg. ↑")
quote(doc, 8, "+ TurnWise 44.69 43.01 29.18 57.36 43.56 18.02 14.61 32.15 21.59 75.85 23.00 49.43")
t = page_text(doc, 8)
t = t[t.index("Qwen2.5-VL-3B Baseline"):t.index("Qwen3-VL-4B") + 2000]
rows = re.findall(r"(Qwen2\.5-VL-3B Baseline|Qwen3-VL-4B Baseline|\+ [A-Za-z0-9]+) ((?:\d+\.\d\d ){11}\d+\.\d\d)", t)
print("\nTable 1 (p. 8), StreamingBench columns: RealTime, Proactive, Avg.")
backbone = "3B"
on = 0
for name, vals in rows:
    if name.startswith("Qwen3-VL-4B"):
        backbone = "4B"
    v = [float(x) for x in vals.split()]
    rt, pro, avg = v[-3], v[-2], v[-1]
    grid = abs(pro / 0.4 - round(pro / 0.4)) < 1e-6
    on += grid
    print(f"  {backbone} {name:24s} RealTime {rt:6.2f}  Proactive {pro:6.2f}  {'= ' + str(round(pro / 0.4)) + '/250' if grid else '<-- not a multiple of 0.4 (k/250)'}  Avg {avg:.2f} (mean {((rt + pro) / 2):.3f})")
print(f"\n{on} of {len(rows)} Proactive accuracies are multiples of 0.4 (k/250); 23.00 would need 57.5 of 250.")

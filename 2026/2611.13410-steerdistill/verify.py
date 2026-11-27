"""Reproduce the checks on SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering, arXiv:2611.13410v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.13410", "v1", "12145019f576142a34d8a2321f17fe15cbeeff535b416186c8de41c22e8c1ee8")

print("1. Table 1 (p. 6): share of benchmark scores whose second decimal is 0 or 5, by block")
quote(doc, 6, "Table 1. Agentic benchmark results across models and quantization settings. Scores are percentages")
t = page_text(doc, 6)
t = t[t.index("Qwen3 8B BF16"):]
METHODS = ["GPTQ", "EfficientQAT", "BitDistiller", "On-Policy QAD", "QeRL", "Ours"]
heads = list(re.finditer(r"(Qwen3 8B |Qwen3\.5 4B |Gemma 4 12B-it )?(BF16|W4A16|W4A8|W2A16) ", t))
blocks = [t[h.start():(heads[i + 1].start() if i + 1 < len(heads) else len(t))] for i, h in enumerate(heads)]
model = None
total_other = [0, 0]
for b in blocks:
    m = re.match(r"(Qwen3 8B |Qwen3\.5 4B |Gemma 4 12B-it )?(BF16|W4A16|W4A8|W2A16) ", b)
    if not m:
        continue
    model = (m.group(1) or "").strip() or model
    prec = m.group(2)
    vals = []
    for meth in (["–"] if prec == "BF16" else METHODS):
        mm = re.search(re.escape(meth) + r" ((?:\d+\.\d\d ){5})\d+\.\d\d", b)
        if mm:
            vals += [float(x) for x in mm.group(1).split()]  # five benchmarks, Avg. excluded
    if not vals:
        continue
    on = sum(1 for v in vals if round(v * 100) % 5 == 0)
    tag = "   <--" if on == len(vals) else ""
    print(f"  {model:15s} {prec:6s} {on:2d}/{len(vals):2d} on the 0.05 grid{tag}")
    if not tag:
        total_other[0] += on
        total_other[1] += len(vals)
print(f"  All other blocks together: {total_other[0]}/{total_other[1]} (a second decimal of 0 or 5 is about 1 in 5 for ordinary scores)")
quote(doc, 6, "W4A8 GPTQ 35.90 22.90 54.70 66.80 30.20 42.10 EfficientQAT 40.20 27.10 60.00 71.80 34.00 46.62")


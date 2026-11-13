"""Reproduce the check on SWAM, arXiv:2611.12870v2.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.12870", "v2", "d2c727f13d32046b46d479322384673f5b25b5d838e15907a65800820bcd6577")

print("Ablation success rates (Tables 3-9) on 50 tasks x 25 episodes = 1,250 episodes per setting")
quote(doc, 11, "we jointly post-train a single model on all 50 tasks")
quote(doc, 11, "we run 25 evaluation episodes for ablation studies and 100 episodes for main results")
quote(doc, 12, "Caption Easy (C2C) Hard (C2R) Original 84.64 50.80 Rephrased 86.08 54.76 Detailed + Env. 86.48 56.16")
values = []
for page in range(12, 16):
    text = page_text(doc, page)
    for m in re.finditer(r"Table [3-9]\.", text):
        values += re.findall(r"\b\d{2}\.\d{2}\b", text[m.start():m.start() + 700])
off = [v for v in values if abs(round(float(v) / 0.08) * 0.08 - float(v)) > 0.005]
print(f"  {len(values) - len(off)} of {len(values)} values are multiples of 0.08 (k/1250); not: {off}")
print(f"  54.76% of 1,250 = {0.5476 * 1250:.1f} successes; nearest attainable 54.72 (684) and 54.80 (685)")

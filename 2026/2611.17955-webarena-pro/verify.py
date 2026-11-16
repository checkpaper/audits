"""Reproduce the check on WebArena-Pro, arXiv:2611.17955v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.17955", "v1", "522f39f2faa50c121d121d17024164d486098c8a5bc4c0dba3c111f363e59d19")

print("GenericAgent Test runs: Appendix C.1 versus Tables 5 and 9 (300 tasks per model)")
quote(doc, 16, "Across the 2,400 Test runs, 878 of the 1,683 unsuccessful runs (52.2%) reached the 50-step limit")
quote(doc, 19, "Of Claude Opus 4.7’s 224 unsuccessful Test runs, 155 reached the 50-step limit")
models = ["Qwen 3.5 9B", "Qwen 3.6 27B", "Qwen 3.8 27B", "Gemma4 26B A4B", "Gemma4 31B",
          "Gemini 3.1 Flash Lite", "Gemini 3.1 Pro omni†", "Claude Opus 4.7"]
t5 = page_text(doc, 9)
wins = 0
for m in models:
    sr = float(re.search(re.escape(m) + r"(?: \d+\.\d){6} (\d+\.\d)", t5).group(1))
    k = round(sr * 3)
    wins += k
    print(f"  Table 5 {m:24s} overall {sr:4.1f}% = {k}/300")
print(f"  Table 5, eight GenericAgent rows: {wins} successes, {2400 - wins} unsuccessful of 2,400")
t9 = page_text(doc, 16)
extra = float(re.search(r"Table 9:.*?Gemini 3\.1 Pro(?: \d+\.\d){6} (\d+\.\d)", t9).group(1))
print(f"  Table 9 Gemini 3.1 Pro (non-omni), also in Figure 5: {extra}% = {round(extra * 3)}/300")
print(f"  All nine Figure 5 configurations: {wins + round(extra * 3)} successes in 2,700 runs")
print(f"  Appendix C.1 implies 2,400 - 1,683 = {2400 - 1683} successes")

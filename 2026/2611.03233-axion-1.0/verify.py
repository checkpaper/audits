"""Reproduce the check on Axion 1.0, arXiv:2611.03233v2.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.03233", "v2", "6704b2420537cb11740c748ef7f4cd1f89b789c38eb5c614d8e7f8605587f98c")

# BioMysteryBench (human-difficult) is the second score column in Tables 1 to 3.
# Rows evaluated by the Axion team: the Axion models and the baselines marked with *.
ROWS = [
    (9, "Table 1", r"GPT-5\.6 Sol \[28\] − (\d+\.\d)∗"),
    (9, "Table 1", r"Gemini 3\.1 Pro \[12\] \d+\.\d (\d+\.\d)∗"),
    (9, "Table 1", r"Axion 1\.0-35B \d+\.\d (\d+\.\d) "),
    (9, "Table 1", r"Axion 1\.0-122B \d+\.\d (\d+\.\d) "),
    (10, "Table 2", r"(?:Qwen3\.6-35B-A3B|Qwen3\.5-122B-A10B|\+ SFT Stage II?|\+ RL \(Axion 1\.0\)) \d+\.\d (\d+\.\d) "),
    (11, "Table 3", r"Axion 1\.0-(?:4B|9B|35B|122B) \d+\.\d (\d+\.\d) "),
]

print("BioMysteryBench (human-difficult) scores evaluated by the Axion team")
values = []
for page, table, pattern in ROWS:
    found = [m.group(1) for m in re.finditer(pattern, page_text(doc, page))]
    if not found:
        sys.exit(f"p. {page}: row not found: {pattern}")
    values += [(table, page, v) for v in found]

for table, page, v in values:
    k = [k for k in range(18) if f"{100 * k / 17:.1f}" == v]
    fit = f"= {k[0]}/17" if k else "is not k/17 for any k"
    print(f"  {table} (p. {page}): {v:>5}  {fit}")

print()
quote(doc, 8, "We report the best score from a single run, rather than an aggregate over runs")
quote(doc, 8, "On BMB, Axion 1.0-122B reaches 41.7%")
quote(doc, 9, "RL also improves BMB for the 122B model (35.3% to 41.7%)")
print("  Nearest values on a 17-question grid: 7/17 = 41.2, 8/17 = 47.1")

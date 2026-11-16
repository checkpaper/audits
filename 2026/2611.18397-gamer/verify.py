"""Reproduce the check on Gamer, arXiv:2611.18397v1.

Run: python verify.py
"""
import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.18397", "v1", "c2829b2fff6e70b3716f51874b7a0d4f048ae4c48e9d09ce7cca8581b3ea37d5")

print("Bestial Ferocity milestone types: Table 14 rows versus Table 14 footnote")
quote(doc, 18, "They contain 30 and 55 evaluation milestones, grouped into 22 and 40 parent steps")
quote(doc, 48, "Types. N: navigation (32), D: dialogue (16), C: combat (2), U: UI interaction (2), P: puzzle (3).")
lines = [s.strip() for s in doc[47].get_text().split("\n")]
rows = lines[:lines.index("Total: 55 milestones")]
types = [rows[i] for i in range(len(rows) - 1)
         if rows[i] in ("N", "D", "C", "U", "P") and re.fullmatch(r"\d+", rows[i + 1])]
print(f"  Table 14 type column, {len(types)} rows: {dict(collections.Counter(types))}")

print("\nTable 6, Bestial Ferocity Nav. and Dialogue cells, each task run three times")
quote(doc, 22, "we evaluate each task three times and report the averaged success rate")
text = page_text(doc, 22)
models = ["Gemini-3.8-Flash", "GPT-5.6-Sol", "GPT-5.6-Luna", "Claude-Opus-5.0", "GLM-5.3-Flash",
          "DeepSeek-V4-Flash-Vision", r"Qwen3-VL-8B \(Base\)", "Gamer-CPT", "Gamer-SFT", "Gamer-RL"]
fits = {(32, 16): 0, (28, 20): 0}
for m in models:
    v = [float(x) for x in re.findall(r"\d+\.\d", re.search(m + r"((?: \d+\.\d){11})", text).group(1))]
    nav, dia = v[5], v[6]
    def ok(x, n):
        return abs(round(x * 3 * n / 100) / (3 * n) * 100 - x) < 0.051
    row = []
    for n_nav, n_dia in fits:
        good = ok(nav, n_nav) and ok(dia, n_dia)
        fits[(n_nav, n_dia)] += good
        row.append(f"N{n_nav}/D{n_dia} {'fits' if good else 'no'}")
    print(f"  {m.replace(chr(92), ''):26s} Nav {nav:5.1f} Dialogue {dia:5.1f}: " + ", ".join(row))
for (n_nav, n_dia), k in fits.items():
    print(f"  {k} of {len(models)} rows fit {n_nav} navigation and {n_dia} dialogue milestones")

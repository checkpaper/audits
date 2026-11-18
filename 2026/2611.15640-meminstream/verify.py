"""Reproduce the check on MemInStream, arXiv:2611.15640v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.15640", "v1", "dc131e3c6c305b2c2abfdfb2731c8507e6cfaa05d84c45b93fd6c17ca572ab0b")

print("Sec. 5.3 (p. 8)")
quote(doc, 8, "Among online models, StreamForest achieves the highest average accuracy across all four memory categories, "
              "with particularly strong performance on State Tracking & Updating (37.06%)")

# Table 2 (p. 9): each row has 17 task scores and 4 category averages; the averages sit at positions 6, 11, 17, 20.
text = page_text(doc, 9)
online = text[text.index("Open-Source Online MLLMs (Training-Free)"):text.index("Task abbreviations")]
rows = {}
for m in re.finditer(r"([A-Za-z][\w.\-() ]*?) (\d+B) (\S+) ((?:\d+\.\d ){20}\d+\.\d)", online):
    name = f"{m.group(1).replace('Open-Source Online MLLMs (Training-Based) ', '')} {m.group(3)}"
    v = [float(x) for x in m.group(4).split()]
    rows[name] = [v[6], v[11], v[17], v[20]]
if len(rows) != 12:
    sys.exit(f"parsed {len(rows)} online rows, expected 12")

cats = ["Episodic Retrieval", "State Tracking & Updating", "Multi-Evidence Integration", "Contextual Memory"]
print("\nTable 2 (p. 9), online models: best category average")
for i, c in enumerate(cats):
    best = max(rows, key=lambda r: rows[r][i])
    sf = rows["StreamForest 1"][i]
    print(f"  {c:27s} best {best:28s} {rows[best][i]:5.1f}   StreamForest {sf:5.1f}")

print("\nFig. 5 (p. 11): JoyAI-VL-Interaction with memory")
quote(doc, 11, "31.8 28.6 22.3 26.9 41.0 43.9 32.6 29.7 JoyAI w/o memory JoyAI w/ memory")

"""Reproduce the check on Non-penetrating World Models (NoPeWorld), arXiv:2611.27963v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.27963", "v1", "6b97b3ab1112a9a43206338ed1a841e6b3a6ecbc2ffa403adada68e38660f96e")

print("Sec. 4.4, Task 1 (p. 7)")
quote(doc, 7, "The better mode alters 4–15% of safe inputs, 31.1% on Hy-Nomas.")
print("Table 3 (p. 5): Missed Coll/Pred, False Coll/Pred, Score Raw/Coll/Pred")
rows = {
    "LingBot-World 2.0": "2.6 2.4 7.0 9.3 56.3 89.3 88.1",
    "HY-WorldPlay": "4.0 6.6 9.2 29.9 56.3 81.8 79.7",
    "Echo-WM": "3.3 2.5 19.2 12.7 51.2 83.7 84.6",
    "Evoke-Turbo": "11.5 – 4.4 – 47.2 79.7 –",
    "WorldPlay2†": "0.6 1.4 14.6 17.9 53.2 85.9 82.6",
    "Hy-Nomas†": "1.5 5.7 49.4 31.1 55.7 76.7 72.7",
}
for name, cells in rows.items():
    quote(doc, 5, f"{name} {cells}")
print()
for name, cells in rows.items():
    c = [None if x == "–" else float(x) for x in cells.split()]
    false = {"Coll": c[2], "Pred": c[3]}
    score = {"Coll": c[5], "Pred": c[6]}
    best = max((m for m in score if score[m] is not None), key=lambda m: score[m])
    print(f"  {name:18s} better mode by Score: {best} ({score[best]}), its False rate {false[best]}%")

"""Reproduce the checks on Scaling Mathematical Proof Supervision from Structured Textbooks (TOME-Math), arXiv:2610.40394v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.40394", "v1", "dbac10731240c657315c3aecf984be92b3c444c09621356bbdfbba4ce64a7b18")

print("The estimates are described as inverse-probability weighted")
quote(doc, 29, "We retain each response’s sampling probability so that population-level estimates can be inverse-probability weighted rather than treating this deliberately balanced sample as representative of the raw response distribution.")
quote(doc, 30, "should be reported as the weighted point estimate followed by the problem-clustered 95% bootstrap confidence interval in brackets.")

print("\n1. Table 8 Panel A: the Overall row versus the six subject rows (p. 30)")
rows = {
    "Abstract algebra": "Abstract algebra 100 42.1 [35.8, 48.7] 9.8 [4.2, 17.6] 19.3 [13.1, 26.5] 84.7 [79.6, 89.2]",
    "Differential geometry": "Differential geometry 100 37.8 [31.5, 44.4] 11.4 [5.6, 19.2] 20.7 [14.5, 28.0] 83.5 [78.3, 88.1]",
    "Discrete mathematics": "Discrete mathematics 100 52.3 [45.8, 58.7] 7.2 [2.6, 14.0] 16.9 [11.2, 23.7] 87.4 [82.6, 91.5]",
    "Mathematical analysis": "Mathematical analysis 100 54.6 [48.1, 60.9] 6.8 [2.4, 13.4] 15.8 [10.3, 22.4] 88.1 [83.5, 92.0]",
    "Probability": "Probability 100 55.4 [48.9, 61.6] 7.9 [3.0, 15.0] 17.5 [11.7, 24.3] 86.6 [81.7, 90.8]",
    "Topology": "Topology 100 45.2 [38.7, 51.8] 9.1 [3.8, 16.8] 18.6 [12.5, 25.7] 85.2 [80.2, 89.6]",
}
overall = "Overall 600 47.9 [44.6, 51.2] 8.7 [6.3, 11.5] 18.1 [15.3, 21.1] 85.9 [83.8, 87.9]"
vals = []
for q in rows.values():
    quote(doc, 30, q)
    nums = [float(x) for x in q.replace("[", " ").replace("]", " ").replace(",", " ").split() if x.replace(".", "").isdigit()]
    vals.append(nums[1::3][:4])  # point estimates: accept, false accept, false reject, H-L agree
quote(doc, 30, overall)
names = ["Human accept", "False accept", "False reject", "H-L agree"]
reported = [47.9, 8.7, 18.1, 85.9]
for k, name in enumerate(names):
    mean = sum(v[k] for v in vals) / 6
    print(f"  {name:13s} unweighted mean of six subjects {mean:.3f}   Overall row {reported[k]}")

print("\n2. Table 8 Panel B: Overall recomputed from the population shares (p. 30)")
panel_b = [
    ("8 of 8 150 42.3 [40.9, 43.7] 91.3 [86.4, 94.8] 7.5 [4.1, 12.3] 91.3 [86.4, 94.8]", 42.3, 91.3, 91.3),
    ("7 of 8 150 7.8 [7.0, 8.7] 68.4 [60.5, 75.6] 30.2 [23.1, 38.2] 31.6 [24.4, 39.5]", 7.8, 68.4, 31.6),
    ("1–6 of 8 150 18.1 [17.0, 19.3] 22.1 [15.9, 29.4] 76.4 [69.0, 82.7] 77.9 [70.6, 84.1]", 18.1, 22.1, 77.9),
    ("0 of 8 150 31.8 [30.5, 33.1] 2.8 [0.9, 6.4] 96.4 [92.3, 98.6] 97.2 [93.6, 99.1]", 31.8, 2.8, 97.2),
]
for q, *_ in panel_b:
    quote(doc, 30, q)
acc = sum(s * a for _, s, a, _ in panel_b) / 100
agr = sum(s * g for _, s, _, g in panel_b) / 100
print(f"  Human accept weighted by population share {acc:.2f}   Overall row 47.9")
print(f"  H-L agree weighted by population share    {agr:.2f}   Overall row 85.9")

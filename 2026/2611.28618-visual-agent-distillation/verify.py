"""Reproduce the check on Distilling Visual Agents from Limited Interaction Experience, arXiv:2611.28618v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.28618", "v1", "a0911a5b2443dc865059bbc94a9aff624b2573a2bb01132d246dbc1f57200213")

print("Table S3 (p. 13): four supplementary training repetitions per selector, 240 episodes per panel")
quote(doc, 13, "All four repetitions are retained for each method; each panel has 240 evaluation episodes.")
runs = {
    "Complete selector": ["79.58 (191/240) 26.67 (64/240)", "80.00 (192/240) 21.67 (52/240)",
                          "82.92 (199/240) 20.83 (50/240)", "85.42 (205/240) 25.83 (62/240)"],
    "Representativeness only": ["80.00 (192/240) 25.83 (62/240)", "80.42 (193/240) 27.50 (66/240)",
                                "80.00 (192/240) 17.92 (43/240)", "82.50 (198/240) 22.92 (55/240)"],
    "Fixed random K4": ["74.17 (178/240) 26.67 (64/240)", "75.00 (180/240) 23.33 (56/240)",
                        "77.92 (187/240) 15.83 (38/240)", "80.42 (193/240) 20.83 (50/240)"],
}
for name, rows in runs.items():
    quote(doc, 13, name + " 1 " + rows[0] + " 2 " + rows[1] + " 3 " + rows[2] + " 4 " + rows[3])


def successes(row):
    return [int(x.split("/")[0].strip("(")) for x in row.split() if "/" in x]


print("\nRun 4 minus run 3, in successes out of 240 (standard, long horizon):")
for name, rows in runs.items():
    s3, s4 = successes(rows[2]), successes(rows[3])
    print(f"  {name:24s} standard {s3[0]} -> {s4[0]} ({s4[0] - s3[0]:+d}), long horizon {s3[1]} -> {s4[1]} ({s4[1] - s3[1]:+d})")
print("\nAll three separately trained selectors gain exactly +6 standard and +12 long-horizon successes from run 3 to run 4.")
for a, b in [(0, 1), (1, 2)]:
    names = list(runs)
    diffs = [[y - x for x, y in zip(successes(runs[n][a]), successes(runs[n][b]))] for n in names]
    print(f"  For comparison, run {b + 1} minus run {a + 1}: " + ", ".join(f"{d[0]:+d}/{d[1]:+d}" for d in diffs))

"""Reproduce the check on RoboTryOn (Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On), arXiv:2611.05163v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.05163", "v1", "6b41a14881663fce655108a78cbc6fc73fa436607081a822d58dc8830ae0a3be")

TRIALS = 28
quote(doc, 25, "Success rates (%) over 28 trials per task using π0.5 on OpenArm and RB-Y1.")
quote(doc, 26, "Table 13: Component ablation, per task. Success rate (%) on the OpenArm with π0.5 for the variants of Table 3a.")
tasks = ["PnP Bottle", "PnP Doll", "PnP Box", "PnP Ball", "PnP Coffee Pot", "PnP Bottle to Shelf", "Pouring",
         "Brushing", "Box Convey", "Air Fryer", "PnP Ball in Cup"]
full = "92.9 71.4 71.4 67.9 75.9 64.3 89.3 85.7 82.1 78.6 60.7 50.0 73.0"
noar = "85.7 64.3 64.3 60.7 68.8 57.1 82.1 78.6 75.0 71.4 53.6 46.4 66.3"
quote(doc, 26, "RoboTryOn (Ours) (full) " + full)
quote(doc, 26, "w/o Autoregressive reference " + noar)


def per_task(row):
    v = [float(x) for x in row.split()]
    return v[:4] + v[5:12]  # drop the two Avg. columns


print(f"\nSuccesses out of {TRIALS} (full -> w/o autoregressive reference):")
deltas = []
for t, a, b in zip(tasks, per_task(full), per_task(noar)):
    ka, kb = round(a * TRIALS / 100), round(b * TRIALS / 100)
    assert abs(100 * ka / TRIALS - a) < 0.06 and abs(100 * kb / TRIALS - b) < 0.06
    deltas.append(kb - ka)
    print(f"  {t:20s} {ka:2d} -> {kb:2d}  ({kb - ka:+d})")
print(f"\n{deltas.count(-2)} of {len(deltas)} tasks drop by exactly 2 of 28 trials; the other by {[d for d in deltas if d != -2]}.")

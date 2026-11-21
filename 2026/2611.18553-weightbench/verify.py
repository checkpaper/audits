"""Reproduce the check on WeightBench (Evaluating Language Models as Weight-Space Programmers), arXiv:2611.18553v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.18553", "v1", "5318082260b3caee68b33cb8fb7b9b19986cd202f403f466e275b29bad1f5bf5")

print("1. Runs per model (Sec. 5, p. 4; Table 1, p. 5)")
quote(doc, 4, "with two samples per task for the Claude models and one for DeepSeek and GPT-6.1-sol")
quote(doc, 5, "Tasks evaluated 42 42 42 42 38 Runs (quarantined) 78 (7) 77 (1) 77 (11) 42 (13) 38 (7)")
tasks = [42, 42, 42, 42, 38]
runs = [78, 77, 77, 42, 38]
samples = [2, 2, 2, 1, 1]
for t, r, s in zip(tasks, runs, samples):
    print(f"  {t} tasks x {s} sample(s) = {t * s:3d} expected, {r:3d} reported")
print("  The three Claude columns are 6-7 runs short of two samples per task.")

print("\n2. Red-team trial count (App. D, pp. 8-9)")
quote(doc, 8, "containing 29 cheat scenarios")
quote(doc, 8, "and 30 honest controls")
quote(doc, 9, "three independent trials per scenario on the cluster (180 total runs)")
quote(doc, 9, "0 false positives across all 90 honest control trials")
print(f"  (29 + 30) x 3 = {(29 + 30) * 3}, not 180; 180 would need 60 scenarios (30 + 30).")

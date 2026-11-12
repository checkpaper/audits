"""Reproduce the checks on World In-Context Learning for Agentic Robot Manipulation (RoboScript), arXiv:2611.12885v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.12885", "v1", "d45eb61ae09fb35320b811cd6aabd28af81b550342272dfae080e1fbb27a045c")

print("Section 5.4 (p. 12): rehearsal on the 11 harder tasks")
quote(doc, 8, "Each task is evaluated on 10 episodes per setting")
quote(doc, 12, "On 11 such tasks, deploying the memory from imitation without rehearsal gives 46.1%, "
               "against 54.5% for the full method. The gain is 8.4 points on average and reaches "
               "13.3 points under randomization")


def nearest(value, n):
    """The two values k/n (in %) either side of value, and the one equal to it at 1 dp, if any."""
    k = int(value * n / 100)
    below, above = 100 * k / n, 100 * (k + 1) / n
    hit = next((v for v in (below, above) if abs(v - value) <= 0.05 + 1e-9), None)
    return hit, below, above


# 11 tasks x 10 episodes x 2 settings: a two-setting mean is k/220; a single setting is k/110.
# A difference of two such values is again a multiple of 1/220 (mean) or 1/110 (one setting).
for label, value, n in (("full method, mean of two settings", 54.5, 220),
                        ("without rehearsal, mean of two settings", 46.1, 220),
                        ("gain, mean of two settings", 8.4, 220),
                        ("gain under randomization, one setting", 13.3, 110)):
    hit, below, above = nearest(value, n)
    if hit is not None:
        print(f"  {label}: {value} = {hit:.2f}, a k/{n} value")
    else:
        print(f"  {label}: {value} is not k/{n}; the nearest are {below:.2f} and {above:.2f}")

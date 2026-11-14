"""Reproduce the checks on HeLM, arXiv:2611.02660v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.02660", "v1", "462b04e0e3efd9158b511404c00e4ee329c74680225362b3d9ca59a79010a5ab")

print("Table 8 strict task success versus the trial counts")
quote(doc, 22, "Each task variant is evaluated over 5 trials")
quote(doc, 23, "a trial counts as successful only if (i) all required subtasks are completed")
quote(doc, 23, "HeLM (Ours) 100.0 87.8 96.6 66.7 55.6 81.3")
for phrase in ("Press the blue button N times. 3", "buttons in order. 6 Order",
               "wiped from left to right. 6 Order", "bottom left. 4 Target", "to the [C] plate. 6 Transfer"):
    quote(doc, 17, phrase)
quote(doc, 23, "Keyframe-HLP 0.0 86.7 20.0 0.0 40.0 29.3")
reported = {"A1": (3, 100.0), "A2": (6, 87.8), "A3": (6, 96.6), "A4": (4, 66.7), "A5": (6, 55.6)}
print("  Variants from Table 6 (p. 17): A1 3, A2 6, A3 6, A4 4, A5 6; 5 trials each")
for task, (var, val) in reported.items():
    n = 5 * var
    near = sorted(range(n + 1), key=lambda k: abs(100 * k / n - val))[:2]
    ok = any(abs(round(100 * k / n, 1) - val) < 0.051 for k in range(n + 1))
    alts = ", ".join(f"{k}/{n} = {100 * k / n:.1f}" for k in sorted(near))
    print(f"  {task}: {val} with n = {n}: {'attainable' if ok else 'not attainable'} (nearest {alts})")
print("  A3 96.6 is 29/30 = 96.67 truncated; A2, A4 and A5 fit no count. Keyframe-HLP values (86.7, 20.0, 40.0) all fit.")
print("  Averaging per variant first gives the same grid: steps of 20/var points.")

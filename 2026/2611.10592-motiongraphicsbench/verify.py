"""Reproduce the check on MotionGraphicsBench, arXiv:2611.10592v2.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.10592", "v2", "b141875be24c53fb337b9a85be9a20a0b704311728a929f06b3e2f7575e34034")

print("Protocol: three Full runs on the balanced test set of 180 animations")
quote(doc, 8, "we report mean results across three runs per condition on the balanced test set of 180 animations.")
quote(doc, 23, "For instances that finish earlier, we retain their final program results in subsequent iteration summaries. Table 10 reports mean agreement across the three Full runs.")

print("\nTable 9 / Table 10 (p. 24)")
quote(doc, 24, "Full construction 1 93.33% 90.00% 96.67% 2 92.78% 88.89% 96.67% 3 93.89% 91.11% 96.67%")
quote(doc, 24, "Iteration 1 61.79% Iteration 2 88.32% Iteration 3 91.28% Iteration 4 92.02% Iterations 5–7 93.32% Final verification programs 93.33%")
print(f"  Final: runs 168, 167, 169 of 180 -> mean {(168 + 167 + 169) / 540 * 100:.2f}%")

print("\nA mean of three agreement rates over 180 animations is k / 540 (steps of 0.185 points)")
for name, v in [("Iteration 1", 61.79), ("Iteration 2", 88.32), ("Iteration 3", 91.28), ("Iteration 4", 92.02), ("Iterations 5-7", 93.32), ("Final", 93.33)]:
    k = round(v * 540 / 100)
    ok = abs(100 * k / 540 - v) <= 0.005
    print(f"  {name:15s} {v:6.2f}%  nearest {k}/540 = {100 * k / 540:.2f}%  {'ok' if ok else 'NOT attainable'}")

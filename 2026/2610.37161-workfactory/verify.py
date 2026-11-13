"""Reproduce the check on WorkFactory, arXiv:2610.37161v3.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.37161", "v3", "68b3811705cb70f3bfcfb298859a6682ce586e97add8bafc051d033fc84babd4")

print("Abstract versus Section 4.3: who gains more from 30K to 110K tasks?")
quote(doc, 1, "larger models benefit more from additional task data but exhibit diminishing returns at smaller data scales")
quote(doc, 9, "Qwen3.5-4B 661 4.67 26.92 1.71 + WorkPilot-4B 1375 (+714)")
quote(doc, 9, "Qwen3.6-35B-A3B 879* 28.91 47.12 7.14 + WorkPilot-35B-A3B 1565 (+686)")
quote(doc, 9, "Qwen3.6-27B 975 37.81 49.41 10.18 + WorkPilot-27B 1612 (+637)")
quote(doc, 9, "By 30K tasks, the 35B-A3B and 27B models have captured 88% and 94% of their respective gains")
quote(doc, 9, "The 4B model also gains 546 Elo by 30K tasks")
for name, base, final, at30 in (("4B", 661, 1375, 661 + 546), ("35B-A3B", 879, 1565, 879 + 0.88 * 686),
                                ("27B", 975, 1612, 975 + 0.94 * 637)):
    print(f"  {name:8} base {base}, 30K about {at30:.0f}, 110K {final}: 30K -> 110K adds about {final - at30:.0f} Elo")
print("  The 4B model gains the most from 30K to 110K and the 27B model the least.")

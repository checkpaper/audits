"""Reproduce the check on G-CAST: Governed Continual Self-Training for E-Commerce Agents, arXiv:2611.17814v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.17814", "v1", "09e97c2a03154979dfc0a108a0c4c9620a8447ea2876fa50ec2e97f96741b13a")

print("Suite size")
quote(doc, 5, "evaluated on the cumulative suite of all active slices, which grows from 100 to 400 queries across the four periods.")
quote(doc, 6, "3 P1–3 (300 queries)")

print("\nTable 4 (p. 8)")
quote(doc, 8, "Cumulative reward 0.8810 0.8926 0.9288 Period 1 reward 0.9248 0.9380 0.9336 Period 2 reward 0.8381 0.8486 0.8990 Period 3 reward 0.8801 0.8812 0.9538")
quote(doc, 8, "Skill-selection accuracy 0.6867 0.6956 0.8667")
cum = {"Static": 0.8810, "Ungated": 0.8926, "Gated": 0.9288}
periods = {"Static": (0.9248, 0.8381, 0.8801), "Ungated": (0.9380, 0.8486, 0.8812), "Gated": (0.9336, 0.8990, 0.9538)}
print("\n1. Cumulative reward vs the mean of the three 100-query period rewards")
for arm, ps in periods.items():
    m = sum(ps) / 3
    print(f"  {arm:8s} reported {cum[arm]:.4f}  mean {m:.5f}  difference {cum[arm] - m:+.4f}")

print("\n2. Skill-selection accuracy as k / 300")
for arm, v in {"Static": 0.6867, "Ungated": 0.6956, "Gated": 0.8667}.items():
    k = round(v * 300)
    print(f"  {arm:8s} {v:.4f}  nearest {k}/300 = {k / 300:.5f}  matches to 4 decimals: {round(k / 300, 4) == v}")
    if round(k / 300, 4) != v:
        print(f"           neighbours {k - 1}/300 = {(k - 1) / 300:.5f}, {k + 1}/300 = {(k + 1) / 300:.5f}; "
              f"smallest n with an exact k/n: {next(n for n in range(1, 2000) if round(round(v * n) / n, 4) == v)}")

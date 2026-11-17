"""Reproduce the checks on SWE-CoWork, arXiv:2611.20218v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.20218", "v1", "9872017f1059dea56f33fdab925b18b538ed7791a4f80087b568b74b4ba9b105")


def counts(value, n, dp):
    """Every whole count k out of n that prints as value at dp decimals."""
    return [k for k in range(n + 1) if round(100 * k / n, dp) == value]


print("1. Figure 7 (p. 17): failed F2P nodes in panel (c) against panel (b) and Table 2")
quote(doc, 13, "F2P and P2P use the release totals of 2,699 and 562 test nodes")
quote(doc, 13, "Claude-Opus-5.5 63.84 93.24 6.93")
for phrase in ["n = 453 73.7%", "n = 1,425 68.8%", "n = 821 49.8%",
               "Discovery 16 (2%) Ask 415 (42%) Implement 548 (56%)"]:
    quote(doc, 17, phrase)
groups = {"public": (453, 73.7), "disclosed": (1425, 68.8), "not disclosed": (821, 49.8)}
failed = {}
for name, (n, rate) in groups.items():
    ks = counts(rate, n, 1)
    failed[name] = [n - k for k in ks]
    print(f"  {name:14s} n={n:5d} {rate}% -> passed {ks}, failed {failed[name]}")
print(f"  panel (b) n total = {sum(n for n, _ in groups.values())}")
print(f"  Table 2: 63.84% of 2,699 -> passed {counts(63.84, 2699, 2)}, failed {2699 - counts(63.84, 2699, 2)[0]}")
print(f"  panel (c) failed nodes = 16 + 415 + 548 = {16 + 415 + 548}; panel (b) allows at most {sum(max(v) for v in failed.values())} failed nodes")
print(f"  panel (c) ask = 415, against {failed['not disclosed']} failed not-disclosed nodes")

print("\n2. Table 2 (p. 13): F2P as k/2699 and P2P as k/562")
rows = {
    "Claude-Opus-5.5": (63.84, 93.24), "GPT-6 Astra": (62.91, 89.15), "Seed Evolving": (39.09, 94.48),
    "Qwen3.8-Max": (35.70, 91.80), "GLM 5.3": (31.27, 87.72), "Qwen3.8-Flash": (30.70, 93.40),
    "DeepSeek V4.1 Flash": (28.20, 94.30), "Kimi K3": (27.08, 84.88), "GLM 5.2": (24.40, 95.20),
    "Seed 2.1 Pro": (21.01, 81.85), "DeepSeek V4 Pro": (13.04, 90.21),
}
for name, (f2p, p2p) in rows.items():
    quote(doc, 13, f"{name} {f2p:.2f} {p2p:.2f}")
for name, (f2p, p2p) in rows.items():
    a, b, c = counts(f2p, 2699, 2), counts(p2p, 562, 2), counts(p2p, 561, 2)
    print(f"  {name:20s} F2P {f2p:6.2f} k/2699={str(a or 'none'):8}  P2P {p2p:6.2f} k/562={str(b or 'none'):8} k/561={c or 'none'}")

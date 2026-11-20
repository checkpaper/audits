"""Reproduce the check on Coda-DaVinci, arXiv:2611.26595v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.26595", "v1", "7d6bad4fa0b6b7a4838989afd2f9f577849e390e18c465e10041e4a997cc8ae5")

print("Table 1 (p. 7): last four columns are the three-benchmark averages C, I, P, N")
quote(doc, 7, "G1/P0/PE1 2.455 2.970 2.636 2.606 2.414 2.172 1.345 0.897 2.062 2.469 2.438 2.281 2.309 2.553 2.170 1.968")
quote(doc, 7, "G1/P1/PE1 2.182 2.697 2.515 2.273 2.724 2.897 1.828 1.379 3.000 3.000 2.111 2.278 2.562 2.837 2.175 1.950")
quote(doc, 7, "G1/P0/PE2 2.788 3.000 2.576 2.545 2.586 2.310 1.448 1.034 2.938 2.969 2.531 2.656 2.777 2.777 2.213 2.117")
quote(doc, 7, "G1/P1/PE2 2.818 2.970 2.727 2.515 2.966 2.931 2.034 1.448 3.000 3.000 2.500 2.594 2.926 2.968 2.436 2.213")
print("\nTable 2 (p. 8): P1 minus P0")
quote(doc, 8, "G1/PE1 +0.200 +0.250 +0.062 +0.012 +0.131")
quote(doc, 8, "G1/PE2 +0.149 +0.191 +0.223 +0.096 +0.165")
quote(doc, 8, "improvements in both the four-metric mean and the naturalness and realism average across the three benchmarks under every tested P0/P1 comparison")

rows = {"PE1": ([2.309, 2.553, 2.170, 1.968], [2.562, 2.837, 2.175, 1.950], [0.200, 0.250, 0.062, 0.012]),
        "PE2": ([2.777, 2.777, 2.213, 2.117], [2.926, 2.968, 2.436, 2.213], [0.149, 0.191, 0.223, 0.096])}
for pe, (p0, p1, t2) in rows.items():
    d = [b - a for a, b in zip(p0, p1)]
    print(f"\n  G1/{pe} from Table 1: " + " ".join(f"{x:+.3f}" for x in d) + f"  mean {sum(d) / 4:+.3f}")
    print(f"  G1/{pe} in Table 2:   " + " ".join(f"{x:+.3f}" for x in t2))
print("\n  G1/PE2 matches; G1/PE1 matches only in the mean. By Table 1, N falls 1.968 -> 1.950 under P1 for G1/PE1.")

"""Reproduce the throughput check on DeepMem, arXiv:2611.05255v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.05255", "v1", "b0dd64ea217a3c86be2c1c061283aeb8cf6f8ed34acedafdd600633a9a4e1aaf")

print("Table 3 (p. 9): evaluation throughput in bytes per second")
quote(doc, 9, "DEEPMEM (NR) 137,963 136,905 139,287 138,051 DEEPMEM 118,963 120,905 119,287 119,718")
print("Table A.1 (p. 13): the same two rows")
quote(doc, 13, "DEEPMEM 1.0134 1.4402 2.4854 1.9694 118,963 120,905 119,287 119,718")
quote(doc, 13, "No shared-state refinement 1.0145 1.4462 2.5021 1.9758 137,963 136,905 139,287 138,051")
quote(doc, 13, "average BPB-evaluation throughput decreases from approximately 138,052 to 119,718 bytes/s")

nr = {"FineWeb-Edu": 137963, "PG19": 136905, "Stack-smol": 139287}
full = {"FineWeb-Edu": 118963, "PG19": 120905, "Stack-smol": 119287}
print()
for k in nr:
    d = nr[k] - full[k]
    print(f"  {k:12s} NR {nr[k]:,}  DeepMem {full[k]:,}  difference {d:,}  last three digits {nr[k] % 1000:03d} / {full[k] % 1000:03d}")
print("Each difference is a whole multiple of 1,000, so the last three digits agree in all three columns.")

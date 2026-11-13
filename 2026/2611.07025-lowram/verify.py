"""Reproduce the checks on LowRAM, arXiv:2611.07025v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.07025", "v1", "f9c11993967297be20dd05c6c844177010528febbdda3f77e1c1d261e7402f77")

print("Table 3 (p. 8): RULER CR, score | LongBench CR, score")
T3 = {
    "Mistral-7B": ["LowRAM 4× 96.0 4× 97.9", "LowRAM-E 8× 91.8 8× 96.6", "LowRAM-Q 4.8× 99.6 6.4× 99.4",
                   "LowRAM-EQ 6.7× 93.6 10.7× 96.9"],
    "Llama-3.1-8B": ["LowRAM 4× 93.9 4× 99.6", "LowRAM-E 8× 79.9 8× 90.6", "LowRAM-Q 4.8× 99.4 6.1× 95.8",
                     "LowRAM-EQ 6.7× 96.4 8.8× 91.3"],
}
for rows in T3.values():
    for r in rows:
        quote(doc, 8, r)

print("\nTable 10 (p. 23): three settings per method, each RULER | LongBench")
T10 = {
    "Mistral-7B": ["LowRAM 2× 99.4 2× 100.7 3× 98.8 3× 99.4 4× 96.0 4× 97.9",
                   "LowRAM-E 4× 99.2 4× 97.8 6× 97.3 6× 97.5 8× 91.8 8× 96.6",
                   "LowRAM-Q 3.3× 99.8 4.5× 99.9 4.1× 99.6 5.6× 99.5 4.8× 99.6 6.4× 99.4",
                   "LowRAM-EQ 5.13× 99.1 7.5× 97.7 6.7× 93.6 9.3× 97.4 8.7× 89.1 10.7× 96.9"],
    "Llama-3.1-8B": ["LowRAM 2× 99.6 2× 98.7 3× 97.9 3× 98.5 4× 93.9 4× 99.6",
                     "LowRAM-E 4× 97.3 4× 94.3 6× 90.0 6× 92.4 8× 79.9 8× 90.6",
                     "LowRAM-Q 3.4× 99.9 4.4× 96.5 4.2× 99.7 5.3× 95.8 4.8× 99.4 6.1× 95.8",
                     "LowRAM-EQ 5.2× 98.2 7.1× 93.5 6.7× 96.4 8.8× 91.3 8.8× 82.7 10.2× 89.4"],
}
for rows in T10.values():
    for r in rows:
        quote(doc, 23, r)

print("\nWhich Table 10 setting each Table 3 cell comes from (1, 2, 3 = lowest to highest compression)")
for model in T3:
    for t3, t10 in zip(T3[model], T10[model]):
        name, *c3 = t3.split()
        _, *c10 = t10.split()
        settings = [c10[0:4], c10[4:8], c10[8:12]]
        ruler = [i + 1 for i, s in enumerate(settings) if s[0:2] == c3[0:2]]
        lb = [i + 1 for i, s in enumerate(settings) if s[2:4] == c3[2:4]]
        print(f"  {model:13s} {name:10s} RULER from setting {ruler}, LongBench from setting {lb}; "
              f"setting 3 = {' '.join(settings[2])}")

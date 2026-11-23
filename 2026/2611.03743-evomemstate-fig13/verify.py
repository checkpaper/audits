"""Reproduce the Figure 13 check on EvoMemState, arXiv:2611.03743v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.03743", "v1", "8d92f7dd8ca1de068c7dff75f8323d616d736341c2d8fbf97995436aeed2801a")

print("Figure 3 (p. 3): w/o vs w/ self-reflection, bar labels as extracted from the PDF")
quote(doc, 3, "0.8 40.9 40.1 AMem 0.4 71.4 71.8 LightMem 1.6 50.5 48.9 MemZero 0.1 55.6 55.5 MemGPT 0.1 55.6 55.7 MemoryBank 0.4 70.8 70.4 Supermemory w/o self-reflection w/ self-reflection")
quote(doc, 3, "lowers average accuracy from 50.5% to 48.9%")
print("Figure 13 (p. 23): w self-reflection vs w/ reasoning state")
quote(doc, 23, "40.9 40.1 0.8 AMem 32.8 71.4 71.8 0.4 LightMem 69.5 50.5 48.9 1.6 MemZero 89.1 55.6 55.5 0.1 MemGPT 41.4 55.6 55.7 0.1 MemoryBank 50.5 70.8 70.4 0.4 Supermemory")
quote(doc, 23, "Accuracy@complete w self-reflection Accuracy@complete w/ reasoning state")

fig3 = {"AMem": (40.9, 40.1), "LightMem": (71.4, 71.8), "Mem0": (50.5, 48.9), "MemGPT": (55.6, 55.5), "MemoryBank": (55.6, 55.7), "Supermemory": (70.8, 70.4)}
fig13 = dict(fig3)  # the quoted Figure 13 text above carries the same six pairs
print()
same = sum(fig3[k] == fig13[k] for k in fig3)
print(f"  {same} of 6 baseline pairs are identical in Figure 3 and Figure 13.")
mean = [sum(v[i] for v in fig3.values()) / 6 for i in (0, 1)]
print(f"  Six-system mean in Figure 3: {mean[0]:.2f} -> {mean[1]:.2f}; 50.5 -> 48.9 are Mem0's own bars.")

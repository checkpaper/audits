"""Reproduce the check on Going Deeper With Memories (DeepMem), arXiv:2611.05255v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.05255", "v1", "b0dd64ea217a3c86be2c1c061283aeb8cf6f8ed34acedafdd600633a9a4e1aaf")

print("Sec. 3.1 (p. 6): three seeds per model")
quote(doc, 6, "All runs use a context length of 2,048 bytes across three random seeds per model")
print("Table 1 (p. 8): FLORES BPB with spread over seeds")
quote(doc, 8, "DEEPMEM (NR) 1.0145 ± 0.010 1.4462 ± 0.022 2.5021 ± 0.046 1.9758 ± 0.017")
quote(doc, 8, "DEEPMEM 1.0134 ± 0.008 1.4402 ± 0.017 2.4854 ± 0.034 1.9694 ± 0.020")
print("Table A.2 and App. A.2 (p. 14): the same two configurations, one run each")
quote(doc, 14, "Swahili Macro DEEPMEM 1.2007 2.3408 2.0383 1.4403 1.6132 1.6535 2.3059 3.1624 1.9694")
quote(doc, 14, "No shared-state refinement 1.2134 2.3473 2.0406 1.4518 1.5996 1.6569 2.2988 3.1978 1.9758")
quote(doc, 14, "These comparisons are exploratory because only one training run is available for each configuration.")
print("\n  FLORES macro: DEEPMEM 1.9694 and NR 1.9758 in both tables.")
print("  Table 1 reports ± 0.020 / ± 0.017 over three seeds; App. A.2 says one run per configuration.")

"""Reproduce the checks on ProTEUS, arXiv:2611.13348v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.13348", "v1", "f355287e9e0412b06a81c118865a0161df4cb883d7a2ffae8608d8aca3901c6c")

print("1. Activity: both campaigns >10-fold?")
quote(doc, 2, "two closed-loop multi-objective engineering campaigns on aldehyde dehydrogenase and levansucrase, "
              "yielding variants with >10 fold higher activity than wild type")
quote(doc, 4, "In laboratory evolution of levansucrase and aldehyde dehydrogenase, ProTEUS can find variants with "
              ">10 fold higher activity than the starting wild-type protein within an experimental budget of 100 sequences")
quote(doc, 9, "G23A:Q34N:G240W reached 14.03-fold WT activity")
quote(doc, 11, "we identified S103V:A116K:H332N:L358I with 6.85-fold WT activity")
quote(doc, 11, "the best mutant in the final round (round 4) had a 7.90 fold improvement of the catalytic rate over WT")
quote(doc, 54, "Each round tested 30 variants.")
print("  Levansucrase reaches 14.03x; ALDH reaches 6.85x (screen) and 7.90x (normalized), below 10x,")
print("  after 5 rounds x 30 = 150 tested variants.")

print("\n2. Speed versus AlphaFold 3")
quote(doc, 2, "achieve >10 fold increase in speed than AlphaFold3")
quote(doc, 7, "Across five atom-count bins, AlphaFold 3 mean runtimes were 7.81–10.81 times higher than those of our predictor.")

"""Reproduce the checks on Auriga, arXiv:2611.01112v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.01112", "v1", "c28cb24a5a67556d70c370dfe1c9746daf3b4885848b85b732baaa3c0428ef3b")

print("Successful episodes: Appendix D versus Table 4 and Table 16")
quote(doc, 16, "over a fixed denominator: a case without an official score stays in the denominator")
quote(doc, 18, "Auriga† Agent 64.00 57.74 52.90 48.89 46.30 38.50 62.10 45.24 93.40 92.99 65.40 63.08")
quote(doc, 41, "Generalization 1,800")
quote(doc, 41, "Precision 1,200")
quote(doc, 41, "Long-Horizon 1,199")
quote(doc, 41, "Memory 900")
quote(doc, 41, "Open 1,200")
quote(doc, 41, "All 6,299")
quote(doc, 41, "successful episodes (3,405 episodes)")
quote(doc, 41, "The remaining 2,894 episodes")
rows = {"Generalization": (48.89, 1800), "Precision": (38.50, 1200), "Long-Horizon": (45.24, 1199),
        "Memory": (92.99, 900), "Open": (63.08, 1200)}
total = 0.0
for name, (sr, n) in rows.items():
    k = sr / 100 * n
    total += k
    print(f"  {name}: {sr}% x {n} = {k:.1f} successes")
print(f"  Sum: {total:.1f} successes over {sum(n for _, n in rows.values())} episodes")
print(f"  Appendix D: 3,405, i.e. {total - 3405:.0f} fewer ({3405 / 6299:.2%} against {total / 6299:.2%})")

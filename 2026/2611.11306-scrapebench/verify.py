"""Reproduce the checks on ScrapeBench, arXiv:2611.11306v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.11306", "v1", "6db2ca2763ac3a1b33ffbd6f8c75558564ae00b90220a55f1a8e1b11601cb26b")

N = 30 * 15
print("Sec. 6 (p. 9): 30 participants per condition, 15 websites each")
quote(doc, 9, "with 30 participants in each of the P1, P4, and P7 prompt conditions")
quote(doc, 9, "scrape 15 randomly sampled websites one at a time")
print(f"  decisions per condition = 30 x 15 = {N}")


def hits(pct):
    return [k for k in range(N + 1) if round(100 * k / N, 1) == pct]


print("\n1. Human rates in Tables 16 and 18 (p. 32)")
quote(doc, 32, "Over-Refusal Rates (NOT EXPLICITLY PROHIBITED) 38.9% 42.8% 45.8%")
quote(doc, 32, "robots.txt opened 0.0% 39.4% 58.7%")
for pct in (38.9, 42.8, 45.8, 39.4, 58.7):
    ks = hits(pct)
    near = [f"{k}/{N} = {100 * k / N:.2f}%" for k in range(N + 1) if abs(100 * k / N - pct) < 0.25]
    print(f"  {pct}%: k/{N} matches {ks if ks else 'none'}   nearest: {', '.join(near)}")

print("\n   Cross-check: the EP compliance row fits n = 450 exactly")
quote(doc, 32, "Compliance Rates (EXPLICITLY PROHIBITED) 48.9% 57.3% 65.1% 24.19")


def chi2(ks, n=N):
    tot, k_all, s = n * len(ks), sum(ks), 0.0
    for k in ks:
        for obs, exp in ((k, n * k_all / tot), (n - k, n * (tot - k_all) / tot)):
            s += (obs - exp) ** 2 / exp
    return s


ep = [hits(p)[0] for p in (48.9, 57.3, 65.1)]
print(f"  counts {ep} of {N}: chi2 = {chi2(ep):.2f} (Table 16: 24.19)")

print("\n2. Design effects (App. E.3, p. 31)")
quote(doc, 31, "ICC = 0.345 for the compliance study")
quote(doc, 31, "These values correspond to design effects of 5.69 and 4.34")
for icc, de in ((0.345, 5.69), (0.238, 4.34)):
    print(f"  1 + (15 - 1) x {icc} = {1 + 14 * icc:.3f}   (paper: {de}; implied ICC {(de - 1) / 14:.3f})")

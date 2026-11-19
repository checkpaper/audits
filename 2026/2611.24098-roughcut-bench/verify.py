"""Reproduce the check on RoughCut-Bench, arXiv:2611.24098v1.

Run: python verify.py
"""
import math
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.24098", "v1", "2318e200fd81c93f48256e59a48a0ab8c04b1d92779ee5da8d3808154b04b3dd")

print("Definitions")
quote(doc, 3, "931 (65.7%) 191 (13.5%) 296 (20.9%)")
quote(doc, 5, "denote the numbers of successful and annotated RM→R pairs")
quote(doc, 5, "speech metrics are computed from decision counts aggregated across all cases")

# Table 3 (p. 7): IM P R F1 | RM->R Succ. | D P R F1
text = page_text(doc, 7)
table = text[text.index("Model\\Metric IM RM→R D"):text.index("Table 3:")]
rows = re.findall(r"([A-Z][\w.\- ]+?) (0\.\d{3}) (0\.\d{3}) (0\.\d{3}) (0\.\d{3}) (0\.\d{3}) (0\.\d{3}) (0\.\d{3})", table)
if len(rows) != 8:
    sys.exit(f"parsed {len(rows)} rows of Table 3, expected 8")


def f1_range(p, r):
    """Smallest and largest harmonic mean allowed by 3-decimal rounding of P and R."""
    vals = [2 * a * b / (a + b) for a in (p - 5e-4, p + 5e-4) for b in (r - 5e-4, r + 5e-4)]
    return min(vals), max(vals)


print("\nTable 3 (p. 7): RM→R success as k/191, and F1 as the harmonic mean of P and R")
print(f"  {'model':15s} {'Succ.':>6s} {'nearest k/191':>16s}   {'IM F1':>6s} {'allowed':>15s}   {'D F1':>6s} {'allowed':>15s}")
for name, ip, ir, if1, s, dp, dr, df1 in rows:
    name = name.split("Succ. P R F1 ")[-1]
    ip, ir, if1, s, dp, dr, df1 = map(float, (ip, ir, if1, s, dp, dr, df1))
    k = math.floor(s * 191)
    lat = "fits" if any(round(j / 191, 3) == s for j in (k, k + 1)) else f"{k / 191:.4f}/{(k + 1) / 191:.4f}"
    cells = []
    for f, (lo, hi) in ((if1, f1_range(ip, ir)), (df1, f1_range(dp, dr))):
        ok = lo - 5e-4 <= f <= hi + 5e-4
        cells.append(f"{f:6.3f} [{lo:.4f},{hi:.4f}]{' ' if ok else '*'}")
    print(f"  {name:15s} {s:6.3f} {lat:>16s}   {cells[0]}  {cells[1]}")
print("  * F1 outside the range allowed by P and R")

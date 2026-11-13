"""Reproduce the check on Drex (Towards Foundation Decision Models), arXiv:2611.07854v2.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.07854", "v2", "6bff5f00a89644dc7562972ab4b769349f4f01d002a764db296777f3386d2bd8")

print("Table 7 (p. 24): flip rates on 1,591 decisions and on the 173 with K >= 6")
quote(doc, 21, "This leaves 1,591 decisions (915 binary, 503 with 3–5 options, 173 with six or more).")
quote(doc, 24, "SFT only 64.9 86.5 4.4 1.45 5.3 14.1 SFT →RLAF, without ℓπ, ℓs 66.4 87.7 3.9 1.38 6.3 17.8 "
               "SFT →RLAF (before vision SFT) 66.9 88.0 3.5 1.34 4.2 13.0 "
               "Released: SFT →RLAF →vision SFT 66.8 87.9 3.6 1.35 4.3 13.3")


def fit(value, n):
    k = round(value * n / 100)
    hit = abs(100 * k / n - value) <= 0.05 + 1e-9
    return f"{k}/{n}" if hit else f"not k/{n} (nearest {100 * int(value * n / 100) / n:.2f}, {100 * (int(value * n / 100) + 1) / n:.2f})"


for name, overall, k6 in (("SFT only", 5.3, 14.1), ("RLAF without l_pi, l_s", 6.3, 17.8),
                          ("RLAF before vision SFT", 4.2, 13.0), ("Released", 4.3, 13.3)):
    print(f"  {name:24} {overall}% = {fit(overall, 1591)};  K>=6 {k6}% = {fit(k6, 173)}")

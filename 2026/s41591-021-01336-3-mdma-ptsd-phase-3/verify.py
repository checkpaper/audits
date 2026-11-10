"""Reproduce the checks on Mitchell et al., Nature Medicine 2021, doi:10.1038/s41591-021-01336-3.

Run: python verify.py
"""
import pathlib
import sys
from math import sqrt
from statistics import NormalDist

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch_url, quote  # noqa: E402

doc = fetch_url("https://www.nature.com/articles/s41591-021-01336-3.pdf", "s41591-021-01336-3.pdf",
                "f412a0d6ff8ab3f3942293bbfcf0ecc300a385f556038b1839d9977a29188214")


def cohen_d(m1, s1, n1, m2, s2, n2):
    """Cohen's d with pooled s.d. and the usual large-sample 95% CI."""
    sp = sqrt(((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2))
    d = (m1 - m2) / sp
    se = sqrt((n1 + n2) / (n1 * n2) + d * d / (2 * (n1 + n2)))
    return sp, d, d - 1.96 * se, d + 1.96 * se


print("1. Within-group effect sizes (Results, Efficacy, PDF p. 2)")
quote(doc, 2, "the effect size was 2.1 (95% CI = −5.6 to 1.4) in the MDMA group and 1.2 (95% CI = −4.9 to 2.5) in the placebo group")
for label, est, lo, hi in [("MDMA", 2.1, -5.6, 1.4), ("placebo", 1.2, -4.9, 2.5)]:
    print(f"  {label:8} estimate {est}  CI midpoint {(lo + hi) / 2:.1f}  estimate inside CI: {lo <= est <= hi}")

print("\n2. CAPS-5 d = 0.91, labelled de jure (n = 89)")
quote(doc, 2, "was −24.4 (s.d. 11.6) (n = 42) in the MDMA-assisted therapy group compared with −13.9 (s.d. 11.5) (n = 37)")
quote(doc, 2, "d = 0.91 (95% CI = 0.44–1.37, pooled s.d. = 11.55) in the de jure estimand")
sp, d, lo, hi = cohen_d(24.4, 11.6, 42, 13.9, 11.5, 37)
print(f"  From the completer means (n = 42/37): pooled s.d. {sp:.2f}, d {d:.2f}, 95% CI {lo:.2f} to {hi:.2f}")

print("\n3. SDS: P = 0.0116 with a 95% CI that includes zero")
quote(doc, 2, "P = 0.0116, d.f. = 71, effect size = 0.43, 95% CI = −0.01 to 0.88, pooled s.d. = 2.53")
quote(doc, 2, "was −3.1 (s.d. 2.6) (n = 42) in the MDMA-assisted therapy group and −2.0 (s.d. 2.4) (n = 37)")
se = (0.88 - (-0.01)) / (2 * 1.96)
z = 0.43 / se
print(f"  The reported CI implies z = {z:.2f}, two-sided P = {2 * (1 - NormalDist().cdf(z)):.3f}")
sp, d, lo, hi = cohen_d(3.1, 2.6, 42, 2.0, 2.4, 37)
print(f"  From the completer means (n = 42/37): pooled s.d. {sp:.2f}, d {d:.2f}, 95% CI {lo:.2f} to {hi:.2f}")

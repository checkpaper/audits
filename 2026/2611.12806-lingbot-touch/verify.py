"""Reproduce the checks on Learning Heterogeneous Tactile Representation for General Dexterous Manipulation (LingBot-Touch), arXiv:2611.12806v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.12806", "v1", "5f0c52f41165e1f370a7da775e0659e7d41a77f4333a8c835558300993e75ba3")

print("1. Abstract range versus the gains in Sec. 5.2")
quote(doc, 2, "raises the success rate of Diffusion Policy [10], π0.5 [8], LingBot-VLA [31], and T-Rex [21] by 14 to 26 percentage points")
quote(doc, 15, "gains of 13.9, 21.8, 24.8, and 23.2 percentage points")
gains = [(35.6 - 21.6), (69.9 - 48.1), (73.1 - 48.3), (68.6 - 45.4)]
print("  From the Sec. 5.2 means: " + ", ".join(f"{g:.1f}" for g in gains) + f" pp; largest {max(gains):.1f}, not 26.")

print("\n2. Table 2 (p. 16): 'success rates ... in percent over 20 trials per task'")
quote(doc, 16, "Success rates are reported in percent over 20 trials per task.")
row = "Deformable cup transport 46.25 42.50 63.75 72.50 81.25 78.75 93.30 93.75 96.70 95.00 97.50 100.00"
quote(doc, 16, row)
t = page_text(doc, 16)
body = t[t.index("Sharpa Wave"):]
cells = [float(x) for x in re.findall(r"\b\d{1,3}\.\d{2}\b", body)]
on20 = sum(1 for c in cells if abs(c / 5 - round(c / 5)) < 1e-9)
print(f"  Two-decimal cells on p. 16: {len(cells)}; multiples of 5 (k/20 trials): {on20}")
for v in (93.30, 96.70):
    print(f"  {v}: would need {v / 5:.2f} successes out of 20; also not a multiple of 1.25 or 1.0 (4- or 5-point partial credit over 20 trials)")
print("  Values such as 46.25 or 63.75 are partial-credit scores (App. B rubrics), not success rates over 20 trials.")

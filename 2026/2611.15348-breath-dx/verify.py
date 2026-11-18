"""Reproduce the checks on Breath-Dx, arXiv:2611.15348v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.15348", "v1", "fbe0a8e8d9d78ba85af419db248dcaf7d290330441ac0d5c3febcf55a901f19b")

print("1. Temporal-validation drop")
quote(doc, 1, "All methods degrade significantly under temporal validation (0.05-0.12 AUC drop compared to random cross-validation)")
quote(doc, 8, "The average AUC drop across all diseases and methods is approximately 0.05-0.12.")
quote(doc, 8, "Lung cancer (C34) InceptionTime 0.812 0.746 Hepatitis (B18) CatBoost+Stats 5 0.751 0.698 COPD (J44) Graphormer 0.831 0.767 Healthy (Z00) CNN 0.674 0.600")
pairs = {"C34": (0.812, 0.746), "B18": (0.751, 0.698), "J44": (0.831, 0.767), "Z00": (0.674, 0.600)}
drops = {k: round(r - t, 3) for k, (r, t) in pairs.items()}
print(f"  Table V drops: {drops}; max {max(drops.values()):.3f}, mean {sum(drops.values()) / 4:.3f}")

print("\n2. A15 'near chance (0.45-0.55) across all methods'")
quote(doc, 6, "diabetes (E11) and respiratory tuberculosis (A15) remain near chance (AUC in range 0.45-0.55) across all methods")
quote(doc, 7, "LogisticRegression baseline 0.648 ±0.038 0.524 ±0.010 0.718 ±0.010 0.302 ±0.026 0.687 ±0.024 0.457 ±0.032 0.622 ±0.015 0.533 ±0.022 0.688 ±0.044")
page = re.sub(r"\s+", " ", doc[6].get_text())
table = page[page.find("Model + Features"):]
rows = re.findall(r"([A-Za-z][A-Za-z0-9 +\-]*?)((?: [01]\.\d{3} ±0\.\d{3}){9})", table[:3500])
out = []
for name, cells in rows:
    a15 = float(re.findall(r"([01]\.\d{3}) ±", cells)[8])
    if not 0.45 <= a15 <= 0.55:
        label = re.sub(r"^.*A15 |^(Feature-based|Convolution-based|Graph-based|Time series) ", "", name.strip())
        out.append((label, a15))
print(f"  Table III rows parsed: {len(rows)}; A15 outside 0.45-0.55: {len(out)}")
for name, v in out:
    print(f"    {name}: {v}")

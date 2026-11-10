"""Reproduce the checks on LimiX-2, arXiv:2609.17488v1.

For an undirected skeleton, SHD = FP + FN and F1 = 2TP / (2TP + FP + FN),
so F1 = 2TP / (2TP + SHD). Each row of Table 7 therefore fixes TP, and the
true edge count E = TP + FN lies between TP and TP + SHD.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text  # noqa: E402

doc = fetch("2609.17488", "v1", "81cac82427da6f6b935b53099aa6b29577a9775c2ad94bd5ba513d5df544232f")

# Table 7, p. 22. Columns: Sachs, UF, CausalChamber, PATHFINDER, DIABETES, PIGS.
COLUMNS = ["Sachs", "UF", "CausalChamber", "PATHFINDER", "DIABETES", "PIGS"]
MODELS = ["LimiX-2", "EXAONE Tabular", "TabFM", "TabICLv2", "TabPFN-3", "Xiaomi-TabLDM",
          "XGBoost", "TabCausal", "PC", "GES", "LiNGAM", "AVICI", "NOTEARS-MLP", "DAG-GNN"]
CELL = r"([\d.]+|TIMEOUT|–)"
text = page_text(doc, 22)
table = {}
for model in MODELS:
    pat = re.escape(model) + r" F1 score ↑" + (" " + CELL) * 6 + r" SHD ↓" + (" " + CELL) * 6
    m = re.search(pat, text)
    if not m:
        sys.exit(f"p. 22: row not found: {model}")
    table[model] = (m.groups()[:6], m.groups()[6:])

# Edge counts listed by bnlearn: https://www.bnlearn.com/bnrepository/
BNLEARN = {"PATHFINDER": 195, "PIGS": 592}

for net, arcs in BNLEARN.items():
    col = COLUMNS.index(net)
    print(f"\n{net} (Table 7, p. 22)")
    lo, hi = 0, float("inf")
    for model, (f1s, shds) in table.items():
        if not re.fullmatch(r"[\d.]+", f1s[col]):
            continue
        f1, shd = float(f1s[col]), int(shds[col])
        # F1 is printed to 4 decimals, so accept any integer TP that rounds to it.
        tps = [tp for tp in range(0, 10 * shd + 10) if abs(2 * tp / (2 * tp + shd) - f1) <= 5e-5]
        if not tps:
            sys.exit(f"{model}: no integer TP matches F1 {f1} and SHD {shd}")
        row_lo, row_hi = min(tps), max(tps) + shd
        lo, hi = max(lo, row_lo), min(hi, row_hi)
        print(f"  {model:15} F1 {f1:.4f}  SHD {shd:4}  TP {tps[0] if len(tps) == 1 else tps}"
              f"  edges in [{row_lo}, {row_hi}]")
    print(f"  All rows together: edge count in [{lo}, {hi}]. bnlearn lists {arcs} arcs."
          f" {'Consistent.' if lo <= arcs <= hi else 'Outside the range.'}")

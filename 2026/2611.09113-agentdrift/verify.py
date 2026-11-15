"""Reproduce the checks on Authorization Drift (ADB), arXiv:2611.09113v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.09113", "v1", "dd35ecae13ea3b95c4bb5b00539a41dc1a394ce4a30e9e1a819acda2ef041248")

print("1. Trajectory count versus 13 models x 648 samples x 4 rollouts")
quote(doc, 1, "Across 13 LLMs and three frameworks (25,207 trajectories)")
quote(doc, 2, "Our evaluation contains 25,207 evaluated trajectories from 13 LLMs spanning 4B to 397B parameters under NORMAL")
quote(doc, 2, "We release ADB, a 648-sample dual-path benchmark")
quote(doc, 7, "DR and per-dimension rates are mean±std over 4 rollouts")
full = 13 * 648 * 4
print(f"  13 x 648 x 4 = {full:,}; 25,207 is {25207 / full:.1%} of that")
print(f"  13 x 648 x 3 = {13 * 648 * 3:,}")

print("2. Table 3 Security row versus CCSR = CSR / (1 - DR)")
quote(doc, 5, "CCSR(m) = CSR(m)/(1 −DR(m))")
rows = {
    "Productivity & Workspace": (0.733, 0.495, 0.316, 0.626),
    "Security": (0.781, 0.411, 0.433, 0.724),
    "Finance & E-Commerce": (0.774, 0.403, 0.417, 0.699),
    "Personal & Lifestyle": (0.666, 0.394, 0.391, 0.645),
    "IT & Cloud": (0.802, 0.341, 0.497, 0.755),
    "Social & Communication": (0.751, 0.324, 0.472, 0.699),
    "Data & Research": (0.738, 0.321, 0.484, 0.712),
}
for name, (tsr, dr, csr, ccsr) in rows.items():
    quote(doc, 7, f"{name} {tsr:.3f} {dr:.3f} {csr:.3f} {ccsr:.3f}")
    lo, hi = (csr - 5e-4) / (1 - (dr - 5e-4)), (csr + 5e-4) / (1 - (dr + 5e-4))
    ok = lo - 5e-4 <= ccsr <= hi + 5e-4
    print(f"  {name}: CSR/(1-DR) = {csr / (1 - dr):.4f} (range {lo:.4f}-{hi:.4f}), printed {ccsr} -> {'ok' if ok else 'MISMATCH'}")

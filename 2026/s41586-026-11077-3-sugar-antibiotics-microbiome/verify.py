"""Reproduce the checks on Dai et al., Nature 2026, doi:10.1038/s41586-026-11077-3.

Run: python verify.py
"""
import csv
import pathlib
import sys

import numpy as np
from statsmodels.duration.hazard_regression import PHReg

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch_url, quote  # noqa: E402

paper = fetch_url("https://www.nature.com/articles/s41586-026-11077-3.pdf", "s41586-026-11077-3.pdf",
                  "0a3382cf0fa900e60797d10b29435367c0b2e87a982e078c80915f396dc2e533")
supp = fetch_url("https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-11077-3/MediaObjects/"
                 "41586_2026_11077_MOESM1_ESM.pdf", "s41586-026-11077-3-supplementary.pdf",
                 "25bd5b289b63a46d891cd064f53d515429a0e9b9508ede6c5d7b14d1a06b4b0b")
DATA = "https://zenodo.org/records/23444717/files/"  # the authors' data deposit
blast = download(DATA + "63_asv_blast_annotation.csv?download=1", "63_asv_blast_annotation.csv",
                 "cb2d75218a2aab2c9d1d1a2e0d537188de82e756846b984e5ea1c03f1fe3c24b")
clinical = download(DATA + "df_main_clinical_outcome.csv?download=1", "df_main_clinical_outcome.csv",
                    "d0f78994e4870faab34577c45fc9d67f1ca50679be81dfc4a34e508b4aeb7e48")

print("1. Species named in the Fig. 4 title (PDF p. 6)")
quote(paper, 6, "Fig. 4 | Sugar and antibiotics synergize to exacerbate E. faecalis expansion")
quote(paper, 6, "Associations between E. faecium (amplicon sequence variant 1 (ASV_1)) relative abundance")
with open(blast, newline="") as f:
    asv1 = next(r for r in csv.DictReader(f) if r["asv_key"] == "asv_1")
print(f"  Authors' BLAST table, asv_1: {asv1['species']}, {asv1['pident']}% identity over {asv1['align_length']} bp")

print("\n2. Fig. 3a legend HR for the sugar groups (PDF p. 5)")
quote(paper, 5, "comparable mortality risk (multivariable HR = 0.72, 95% confidence interval = 0.18–2.85, P = 0.6)")
quote(supp, 5, "Below-median 0.59 0.15, 2.32 0.400")
print("  Refit of the authors' model (reproduce/63_fig3_e6_clinical.R, fit_sugar_density_binarized):")
with open(clinical, newline="") as f:
    rows = [r for r in csv.DictReader(f) if float(r["OStime_30"]) > 0]  # day-12 landmark, as in the code
below = np.array([r["SugarCal_cat_high"] == "Below-median" for r in rows], float)
days = np.array([float(r["day_exposed"]) for r in rows])
cols = [below, days, below * days]
cols += [np.array([r["source_and_gvhdppx"] == lv for r in rows], float)
         for lv in ("Cord+CNI-based", "Unmodified+CNI-based", "Unmodified+PTCy-based")]
cols += [np.array([r["intensity"] == lv for r in rows], float) for lv in ("reduced", "ablative")]
fit = PHReg(np.array([float(r["OStime_30"]) for r in rows]), np.column_stack(cols),
            status=np.array([float(r["OSevent"]) for r in rows]), ties="efron").fit()
hr, (lo, hi) = np.exp(fit.params), np.exp(fit.conf_int()).T
print(f"  {len(rows)} patients, {int(sum(float(r['OSevent']) for r in rows))} deaths")
for i, name in enumerate(["Below-median sugar", "Abx exposure (days)", "Below-median x abx days"]):
    print(f"  {name:24} HR {hr[i]:.2f} (95% CI {lo[i]:.2f} to {hi[i]:.2f}), P = {fit.pvalues[i]:.3f}")

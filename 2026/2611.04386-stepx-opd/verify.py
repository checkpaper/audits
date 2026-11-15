"""Reproduce the checks on StepX-OPD, arXiv:2611.04386v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.04386", "v1", "63db820b01c1523148ee9682f2ed3788b91ac5dba87ed12c2d017f11daf55437")

print("Velocity-regression ablation: Sec. 5.4 text versus Table 6")
quote(doc, 21, "Average is (GenEval + OCR + DeQA/5 + PickScore/26)/4")
quote(doc, 10, "Omitting the term, applying it from step 0, and applying it from step 500 reach Averages of 0.8894, 0.8895, and 0.8901, so the result is stable across this choice")
rows = [
    ("w/o regression", 0.9134, 0.8956, 4.178, 22.05, 0.8731),
    ("from step 0", 0.9444, 0.8950, 4.177, 22.96, 0.8895),
    ("from step 500", 0.9442, 0.8986, 4.170, 22.98, 0.8901),
    ("from step 1000", 0.9069, 0.8845, 3.996, 22.62, 0.8652),
]
for name, gen, ocr, deqa, pick, avg in rows:
    quote(doc, 10, f"{name} {gen:.4f} {ocr:.4f} {deqa:.3f} {pick:.2f} {avg:.4f}")
    calc = (gen + ocr + deqa / 5 + pick / 26) / 4
    print(f"  {name}: recomputed Average {calc:.5f}, printed {avg}")
print("  Table 6 is internally consistent; the text gives 0.8894 for w/o regression, the table 0.8731.")
print(f"  Gain from the term (step 500 minus w/o): text {0.8901 - 0.8894:.4f}, table {0.8901 - 0.8731:.4f}")

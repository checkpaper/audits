"""Reproduce the check on TPHC (Improving Hyper-Connections with Tensor-Parallel Grouped Updates), arXiv:2611.23026v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.23026", "v1", "9a6b87f13ad7460282ed6fd46368dbc886df2b6f5b74e5a0e14412f8db153c47")

print("Sec. 4.1 (p. 6)")
quote(doc, 6, "0.7–1.0% below mHC and 0.4–1.7% below mHC-TFA on both")

print("\nTable 1 (p. 6): train and val loss")
rows = {
    "mHC4": "mHC4 52.2 33.0 56.6 27.6 50.4 72.1 48.6 2.0967 2.0985",
    "mHC-TFA4": "mHC-TFA4 52.4 33.2 56.7 27.2 52.0 72.0 48.9 2.0904 2.0923",
    "TPHC4": "TPHC4 52.7 33.0 54.9 28.3 52.6 71.9 48.9 2.0819 2.0838",
    "mHC8": "mHC8 52.4 34.0 55.2 27.8 50.4 72.8 48.8 2.0907 2.0924",
    "mHC-TFA8": "mHC-TFA8 52.8 34.8 54.9 28.3 51.5 71.7 49.0 2.0841 2.0859",
    "TPHC8": "TPHC8 54.2 34.8 56.2 26.9 51.1 72.4 49.3 2.0689 2.0706",
    "mHC16": "mHC16 52.8 34.6 55.9 28.8 50.5 71.4 49.0 2.0867 2.0885",
    "mHC-TFA16": "mHC-TFA16 53.1 32.8 57.2 28.2 52.5 72.1 49.3 2.0818 2.0835",
    "TPHC16": "TPHC16 54.2 35.8 55.2 29.3 51.9 71.9 49.7 2.0671 2.0688",
}
for s in rows.values():
    quote(doc, 6, s)
loss = {k: [float(x) for x in v.split()[-2:]] for k, v in rows.items()}

for base in ("mHC", "mHC-TFA"):
    gaps = []
    for n in (4, 8, 16):
        for j, split in enumerate(("train", "val")):
            b, t = loss[f"{base}{n}"][j], loss[f"TPHC{n}"][j]
            gaps.append((b - t) / b * 100)
            print(f"  N={n:2d} {split:5s} TPHC vs {base:7s}: {(b - t) / b * 100:.2f}% lower")
    print(f"  range vs {base}: {min(gaps):.2f}–{max(gaps):.2f}%\n")
print("vs mHC the stated 0.7–1.0% holds; vs mHC-TFA the largest gap is 0.73%, not 1.7%.")

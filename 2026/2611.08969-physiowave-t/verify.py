"""Reproduce the check on PhysioWave-T (Token-Efficient Wavelet Foundation Models for Biosignals), arXiv:2611.08969v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.08969", "v1", "0e3fbb2b18f82c7c0c4b7a5058db13ce0eb47a32b41ad0a59417b381b1139d2c")

print("Event sensitivity at 11 false alarms per hour on SeizeIT2\n")
print("Abstract (p. 1)")
quote(doc, 1, "from 61.4 % to 74.4 % with RALF")
print("\nIntroduction (p. 2)")
quote(doc, 2, "RALF raises event sensitivity at 11 false alarms per hour from 61.4 % to 78.9 %")
print("\nSec. 5.5 (p. 10)")
quote(doc, 10, "to 74.4 % with RALF and 78.9 % with weighted-logit fusion")
print("\nThe Introduction credits RALF with 78.9 %, which Sec. 5.5 attributes to weighted-logit fusion; RALF is 74.4 %.")

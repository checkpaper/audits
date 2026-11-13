"""Reproduce the check on StreamDuo, arXiv:2611.01120v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.01120", "v1", "33d3bf62577680c60a484126c0410ccdb12505b28775cb660c4b3b48ef82e3c2")

row = "1.84 0.536 0.082 0.118 0.085 0.050 0.095 4.91 3.32"
print("The Proact-VL baseline in Tables 1, 2 and 5 and in Appendix A")
quote(doc, 1, "cuts source-game leakage from 9.9% to 1.0%")
quote(doc, 7, "Proact-VL [47] ICML’26 " + row)
quote(doc, 7, "Tab. 2 adds the components of StreamDuo one at a time, all with the same inference settings. "
              "The first row follows the recipe of Proact-VL.")
quote(doc, 8, "× × × " + row)
quote(doc, 15, "Proact-VL [47] 1,811 200 9.9%")
quote(doc, 15, "Run with the same inference settings as StreamDuo, the recipe of Proact-VL leaks 5.8% of its names.")
print("  Table 2 row 1 equals the Table 1 Proact-VL row in all nine columns; that run leaks 9.9% (Table 5).")
print("  Appendix A gives 5.8% for the Proact-VL recipe under StreamDuo's inference settings.")

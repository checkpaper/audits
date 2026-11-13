"""Reproduce the check on CEPO, arXiv:2610.34722v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.34722", "v1", "366151e9dc0f4fd612e831f08cd19d7db7692fff9ba03fad8a749c5c1018c03b")

print("Appendix B.2 (p. 15) versus Table S7 (p. 16)")
quote(doc, 15, "vanilla PE2 exhibits larger performance degradation as more executor prompts are jointly optimized, "
               "whereas CEPO mitigates this instability")
quote(doc, 16, "1 GENERAL (ours) 61.0 57.9")
quote(doc, 16, "4 GENERAL →CRITIC →TEXT →IMAGE 57.5 57.6 5 GENERAL →CRITIC →TEXT →IMAGE →SUM 56.9 55.3")
rows = {1: (61.0, 57.9), 2: (59.7, 56.1), 3: (60.0, 56.3), 4: (57.5, 57.6), 5: (56.9, 55.3)}
for n, (cepo, pe2) in rows.items():
    print(f"  |I|={n}: PE2+CEPO {cepo} ({cepo - rows[1][0]:+.1f}), PE2 {pe2} ({pe2 - rows[1][1]:+.1f})")
print("  From |I|=1 to |I|=5, PE2+CEPO drops 4.1 points and PE2 drops 2.6.")

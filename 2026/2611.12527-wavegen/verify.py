"""Reproduce the checks on WaveGen, arXiv:2611.12527v1.

Run: python verify.py
"""
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.12527", "v1", "74738e45c6d4451976e023af3938dd96e1063bb704c2941f3ed11e8537f1faae")

print("1. Table 10 (p. 17): WaveGen (0.6B) dimensions")
quote(doc, 17, "DiT Input Dim. 768 1024 1158 Hidden Dim. 1536 4096 4632")
quote(doc, 17, "Head 12 16 16")
print(f"  1158 / 16 heads = {1158 / 16}, not an integer; 4632 = 4 x 1158 = {4 * 1158}")
print(f"  The other two models: 768 / 12 = {768 / 12:g}, 1024 / 16 = {1024 / 16:g}")

print("\n2. Table 7 (p. 7): v-prediction versus x-prediction with Spectral Forcing")
quote(doc, 7, "x-pred v-loss ✓ 5.57 0.46 3.45 v-pred v-loss ✓ 3.93 0.48 2.94")
quote(doc, 7, "v-prediction yields slightly better text-speech alignment and speaker similarity")
print(f"  WER 3.93 vs 5.57: {(5.57 - 3.93) / 5.57:.1%} lower for v-pred")
quote(doc, 8, "Ours (Final) Lv + λmsLms-v-spec 4.96 0.47 3.72")
print("  The final x-pred model (4.96) still has a higher WER than v-pred (3.93).")

print("\n3. Table 3 (p. 6) and Appendix (p. 19): MOS intervals")
quote(doc, 6, "nMOS 4.117±0.112 3.938±0.119 3.917±0.128 3.883±0.123 3.954±0.117 3.958±0.129 4.000±0.126")
quote(doc, 6, "sMOS 3.932±0.038 3.989±0.037 3.972±0.038 3.968±0.037 4.008±0.037 3.952±0.037 3.988±0.037")
quote(doc, 19, "20 native speakers of American English participated. Each participant rated 100 samples per model")
n = 20 * 100
for name, h in (("nMOS", 0.112), ("nMOS", 0.129), ("sMOS", 0.037)):
    print(f"  {name} ±{h}: as a 95% CI over {n} ratings, SD = {h / 1.96 * math.sqrt(n):.2f}")
print("  The largest possible SD on a 1 to 5 scale is 2.00.")
print(f"  For nMOS ±0.112 to be a 95% CI, at most {math.floor((1.96 * 2 / 0.112) ** 2)} ratings could remain.")

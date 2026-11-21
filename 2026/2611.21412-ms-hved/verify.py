"""Reproduce the check on MS-HVED (Flexible Multi-Stack Super-Resolution of Clinical Brain MRI), arXiv:2611.21412v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.21412", "v1", "a71f429497f14864fc378906bb51f7d95682d5c152eb0e893151fb48eae25bca")

print("Introduction (pp. 2-3)")
quote(doc, 2, "On paired real healthy-control")
quote(doc, 3, "MS-HVED improves perceptual quality and structural similarity over the baselines")

print("\nSec. 5.2.1 (p. 10)")
quote(doc, 10, "the FOV-weighted stack average achieved the high- est PSNR, SSIM, and NCC")

print("\nTable 6 (p. 14): PSNR, SSIM, NCC, Percept. on the 7 paired real cases")
rows = {
    "ECLARE": "ECLARE [39] 21.88±1.05 .792±.014 .622±.051 .435±.034",
    "TripleSR": "TripleSR [41] 21.56±0.90 .771±.014 .584±.043 .498±.025",
    "Naive mean": "Naive mean 22.18±0.89 .797±.012 .656±.029 .426±.016",
    "Naive + FOV": "Naive + FOV 23.35±1.09 .841±.009 .750±.035 .352±.022",
    "SegResNet": "SegResNet 22.22±1.08 .813±.013 .652±.065 .277±.021",
    "MS-HVED": "MS-HVED 22.70±1.06 .835±.009 .697±.054 .244±.016",
}
for s in rows.values():
    quote(doc, 14, s)
ssim = {k: float(v.split()[-3].split("±")[0]) for k, v in rows.items()}
best = max(ssim, key=ssim.get)
print(f"  best SSIM: {best} {ssim[best]:.3f}; MS-HVED {ssim['MS-HVED']:.3f}")
print("  MS-HVED has the lowest perceptual loss but not the highest SSIM: Naive + FOV is higher.")

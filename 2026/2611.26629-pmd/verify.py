"""Reproduce the check on Posterior Matching Distillation, arXiv:2611.26629v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.26629", "v1", "ce7b40268b791ddf510adcf1de0e45a15ab5c186a73f93b8390497ef8c0bf94f")

print("Default tilt radius (App. Table, p. 19)")
quote(doc, 19, "Normalized tilt radius Uniform on [0.25, 0.50]")
print("\nTable 2 (p. 8), FLUX.2 PMD diversity: Vendi, LPIPS, DINOv2, DreamSim")
quote(doc, 8, "PMD (FLUX.2) 3.3708 0.5705 0.3690 0.3503")
print("\nTable 5 (p. 20), tilt-radius ablation: Vendi, DreamSim, DINOv2, LPIPS, FID COCO-10k")
quote(doc, 20, "U(0.25, 0.5) 3.370 0.3503 0.3690 0.5705 17.47")
print("\nTable 1 (p. 7), FLUX.2 rows, last column FID on 10K MS-COCO 2014 prompts")
quote(doc, 7, "PMD (Ours) 4 0.8163 84.25 0.4936 12.58 22.97 34.13 24.12")
quote(doc, 7, "FID are evaluated using 10K prompts from MS-COCO 2014")
quote(doc, 6, "FID of 31.57")
print("\n  The default-radius row of Table 5 has the same four diversity values as PMD (FLUX.2) in Table 2,")
print(f"  but its COCO-10k FID is 17.47, against 24.12 in Table 1 (difference {24.12 - 17.47:.2f}).")

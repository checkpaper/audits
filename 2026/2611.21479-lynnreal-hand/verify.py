"""Reproduce the check on LynnReal-Hand, arXiv:2611.21479v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.21479", "v1", "551ef9c74c6ab5b1324b16595119c71df525c8323c76bc3778aafcabeb95657b")

print("1. Table 3 (p. 11): latency per 17 frames and FPS")
quote(doc, 11, "Ultra-Fast-VAE reaches 34.43 dB PSNR at 46.77 ms per 17 frames")
rows = [
    ("Native H3", "Native H3 2423.5 35.04 0.0434 9.05 831.30 20.44", 831.30, 20.44),
    ("Tiny-H3", "Tiny-H3 9.9 30.40 0.1040 13.78 10.90 1555.64", 10.90, 1555.64),
    ("StreamRender1", "StreamRender1 1617.8 33.74 0.0533 10.09 143.31 118.63", 143.31, 118.63),
    ("StreamRender2", "StreamRender2 1617.8 33.95 0.0516 9.88 157.65 123.91", 157.65, 123.91),
    ("SolarX V3", "SolarX V3 2423.5 34.09 0.0484 10.20 552.79 30.54", 552.79, 30.54),
    ("LightVAE", "LightVAE 1752.1 35.13 0.0423 8.97 586.40 28.97", 586.40, 28.97),
    ("Ultra-Fast-VAE", "Ultra-Fast-VAE 361.2 34.43 0.0511 9.80 46.77 363.21", 46.77, 363.21),
]
for name, text, ms, fps in rows:
    quote(doc, 11, text)
    print(f"  {name:15s} 17 / {ms} ms = {17000 / ms:8.2f} FPS   table {fps:8.2f}   FPS x latency = {fps * ms / 1000:.2f} frames")

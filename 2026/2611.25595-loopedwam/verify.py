"""Reproduce the check on LoopedWAM: Looped World Action Models for Elastic Inference, arXiv:2611.25595v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, quote  # noqa: E402

doc = fetch("2611.25595", "v1", "408cc71046aeaf8c06e5b900dd3f802d03bd4c0fff104b963cf7eeb0ecdd311a")
COMMIT = "51aac2536c4857275a66f0229ad02a1351a5c341"
code = download(
    f"https://raw.githubusercontent.com/anhdao69/LoopedWAM/{COMMIT}/src/loopedwam/models/loopedwam.py",
    "loopedwam_51aac25_loopedwam.py",
    "69139c0b404146fc2bf6e586e1e51a2c674e2b686a69e23da39a99304a823210",
).read_text()

print("Paper")
quote(doc, 7, "They hold 479.2M and 105.3M parameters, 584.5M in total (frozen VAE and text encoder excluded).")
quote(doc, 9, "Mem.: peak GPU memory (VAE included, text encoder not)")
quote(doc, 9, "LoopedWAM 0.58B 4 10 2.05 91.8")

print(f"\nReleased code (commit {COMMIT[:7]}, src/loopedwam/models/loopedwam.py)")
for phrase in ["Policy weights are FP32; on CUDA the frozen VAE runs in BF16.", "Call under BF16 autocast."]:
    if phrase not in code:
        sys.exit(f"code: phrase not found: {phrase}")
    print(f'  "{phrase}"')

params = 584.5e6
for name, nbytes in [("FP32", 4), ("BF16", 2)]:
    print(f"  {name} policy weights: {params * nbytes / 1e9:.2f} GB ({params * nbytes / 2**30:.2f} GiB)")
print("  Table 4 peak for LoopedWAM (VAE included): 2.05")

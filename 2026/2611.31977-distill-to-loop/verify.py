"""Reproduce the check on Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models, arXiv:2611.31977v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.31977", "v1", "96a496f2a734cfdc9b05100321ceddc4349f505c90571745dbdc87604a431ded")

print("Claims")
quote(doc, 7, "As the loops continue to K = 8 and K = 16, the samples stay stable and do not degrade.")
quote(doc, 3, "Looped-DiT reaches that quality with less compute, but its quality drops once it runs more loops than it was trained with.")
quote(doc, 9, "degrade when they run more loops than in training.")
quote(doc, 7, "trained with K = 4 rounds.")

print("\nTable 1 (p. 7), distilled student: Overall GenEval, ImageReward, PickScore, HPSv2.1, Avg.")
quote(doc, 7, "SD3-medium [10] (teacher) 50.5 – 0.994 0.753 0.506 0.840 0.285 0.508 0.648 0.908 22.214 0.278 100.0")
rows = {
    4: "Dooop (Ours) 50.5 4 0.988 0.795 0.503 0.830 0.273 0.565 0.659 0.919 22.312 0.276 100.7",
    8: "Dooop (Ours) 92.6 8 0.984 0.803 0.475 0.832 0.245 0.548 0.648 0.889 22.278 0.275 99.3",
    16: "Dooop (Ours) 177.0 16 0.991 0.760 0.438 0.838 0.250 0.525 0.633 0.853 22.229 0.273 97.6",
}
vals = {}
for k, q in rows.items():
    quote(doc, 7, q)
    vals[k] = [float(x) for x in q.split()[-5:]]
    print(f"  K = {k:2d}: " + "  ".join(f"{v:g}" for v in vals[k]))
names = ["GenEval", "ImageReward", "PickScore", "HPSv2.1", "Avg"]
for i, name in enumerate(names):
    seq = [vals[k][i] for k in (4, 8, 16)]
    print(f"  {name}: {seq[0]:g} -> {seq[1]:g} -> {seq[2]:g}  decreasing: {seq[0] > seq[1] > seq[2] or (seq[0] >= seq[1] > seq[2])}")
print(f"  K = 16 average {vals[16][4]} vs teacher 100.0")

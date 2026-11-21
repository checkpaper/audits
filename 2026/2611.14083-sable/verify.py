"""Reproduce the check on Sable (A Small-Field Sumcheck Argument for Bit-Exact Inference of LLMs), arXiv:2611.14083v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.14083", "v1", "44309ee4c6ca1c5b39938fa861d60f0098e4ad2b0bbd030ff872b200579eed14")

print("Claim (p. 32)")
quote(doc, 32, "without it, the global evaluation proof needed two more full passes over every layer, about 25% of the proving time at every shape")

print("\nTable 10 (p. 43): each optimization against the state just before it, 1x4K / 1x16K / 4x4K")
quote(doc, 43, "Per-layer reduction (Section 7.5) 64 layers, three shapes (s) 108.2/304.7/479.1 99.3/269.6/419.3")
quote(doc, 43, "Leaf kernel writes the next GKR layer 64 layers, three shapes (s) 93.1/259.3/404.9 92.4/254.0/397.1")
quote(doc, 43, "each measured against the state just before it")
before, after = (108.2, 304.7, 479.1), (99.3, 269.6, 419.3)
final = (92.4, 254.0, 397.1)
for b, a, f in zip(before, after, final):
    print(f"  {b:6.1f} -> {a:6.1f} s: per-layer reduction saves {(b - a) / b * 100:4.1f}% "
          f"(all later optimizations together: {(b - f) / b * 100:4.1f}%)")
print("  The saving is 8-13%, below 'about 25% at every shape', and even the whole chain saves under 18%.")

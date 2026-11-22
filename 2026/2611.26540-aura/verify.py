"""Reproduce the check on AURA (AUdio-dRiven streaming Avatar), arXiv:2611.26540v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.26540", "v1", "9462f5c0745b0830e34b77cd3c074022e835e5fbc0aee31e45fb4f14cc59f822")

print("1. Output resolution of AURA 1.3B")
quote(doc, 2, "AURA 1.3B streams 576p video in real time")
quote(doc, 10, "AURA 1.3B generates 576p video (768×512 or 576×576")
quote(doc, 12, "AURA 1.3B outputs 480p at 16 Hz")
quote(doc, 12, "AURA 1.3B (ours) 1.3B 480p 4 28.8/96.9 20.7")
for w, h in ((768, 512), (576, 576)):
    print(f"  {w}x{h} = {w * h:,} px (576p 16:9 = {1024 * 576:,}, 480p 16:9 = {854 * 480:,})")

print("\n2. Dataset duration")
quote(doc, 10, "The final dataset totals 30,000 clips (38.7 h")
quote(doc, 10, "The resulting clips average 4.8 s")
print(f"  30,000 x 4.8 s = {30000 * 4.8 / 3600:.2f} h; 38.7 h implies a mean of {38.7 * 3600 / 30000:.2f} s per clip")
print(f"  rounding 4.8 allows 4.75-4.85 s, i.e. {30000 * 4.75 / 3600:.1f}-{30000 * 4.85 / 3600:.1f} h")

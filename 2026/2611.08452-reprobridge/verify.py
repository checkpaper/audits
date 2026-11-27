"""Reproduce the check on ReproBridge: Building Reproducibility into ML Research Artifacts, arXiv:2611.08452v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.08452", "v1", "abf9ad39b587312397d448f2799c6a562e658356e0b3fb640eb3b4d94b238abb")

print("1. Eq. 1 (p. 4): the compatibility interval is centred on the reference mean")
quote(doc, 4, "with sample mean ¯ 𝑥𝑗and sample standard deviation 𝑠𝑗.")
quote(doc, 4, "The compatibility interval is 𝐼(𝑞) 𝑗 = [¯ 𝑥𝑗−𝑟(𝑞) 𝑗 , ¯ 𝑥𝑗+ 𝑟(𝑞) 𝑗 ]")

print("\n2. HELIX worked example (App. D.5, p. 34)")
quote(doc, 34, "The recorded MAE changes from 0.15265 to 0.12986 for T004 and from 0.50527 to 0.41160 for T006; the respective compatibility intervals are [0.12524, 0.13448] and [0.38442, 0.43878].")
for task, new, lo, hi in [("T004", 0.12986, 0.12524, 0.13448), ("T006", 0.41160, 0.38442, 0.43878)]:
    mid = (lo + hi) / 2
    print(f"  {task}: interval midpoint (= reference mean) {mid:.5f}, refined-artifact MAE {new:.5f}, difference {abs(new - mid):.5f}")

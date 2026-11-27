"""Reproduce the checks on Plan4D: Generative Plannable 4D Worlds, arXiv:2611.26516v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.26516", "v1", "ed9fe42aa98ce81c776afcdc2eb4eba5e86f0cde2aab92f4c17d7e2134a257d3")

COLS = ["SC", "BC", "AQ", "IQ", "MS", "Cap.Sim", "AbsRel", "d1", "d2", "Chamfer-L1", "RPE-R", "RRA@10", "RRA@5"]
PO = "Point Odyssey Ours .9233 .9423 .5355 .5941 .9856 .5579 .0822 .9215 .9720 .3013 .1985 .9965 .9864"
RL = "RLBench Ours .8459 .9017 .4619 .4767 .9897 .5583 .0822 .9215 .9721 .3012 .1985 .9963 .9864"

print("Table 8 (p. 32), 'Ours' rows on PointOdyssey and RLBench")
quote(doc, 32, "Table 8: Quantitative comparison across five benchmarks.")
quote(doc, 32, PO)
quote(doc, 32, RL)
po = [float(x) for x in PO.split()[-13:]]
rl = [float(x) for x in RL.split()[-13:]]
print(f"  {'metric':10s} {'PointOdyssey':>12s} {'RLBench':>8s} {'|diff|':>7s}")
for c, a, b in zip(COLS, po, rl):
    print(f"  {c:10s} {a:12.4f} {b:8.4f} {abs(a - b):7.4f}")
geo = [abs(a - b) for a, b in zip(po[6:], rl[6:])]
vid = [abs(a - b) for a, b in zip(po[:6], rl[:6])]
print(f"  depth/reconstruction/camera (7 columns): max |diff| {max(geo):.4f}")
print(f"  video quality (6 columns): max |diff| {max(vid):.4f}")

print("\nTesserAct Chamfer-L1 on the same two benchmarks")
quote(doc, 32, "TesserAct .9019 .9391 .4920 .5351 .9932 .5094 .6347 .2953 .5390 .3904")
quote(doc, 32, "TesserAct .8424 .9235 .4312 .5932 .9842 .1791 5.481 .2003 .3950 .3904")

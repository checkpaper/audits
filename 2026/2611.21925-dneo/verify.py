"""Reproduce the check on DNeo, arXiv:2611.21925v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.21925", "v1", "635c8b3835573ffad890bf1e97354969a8f66499dada206513e4bd90271d1e8b")

print("1. Head ablation: Sec. 5.4.2 text versus Table 6 (p. 14)")
quote(doc, 14, "DSpark + DFlash-2 Head 2.217 DSpark + DSpark Head 2.273 DSpark + DNeo Head (ours) 2.361")
quote(doc, 14, "exhibits +0.056 τ and +0.141 τ over the DFlash-2 head, and DSpark head alone")
dflash2_head, dspark_head, dneo_head = 2.217, 2.273, 2.361
print(f"  Table 6: DNeo head - DFlash-2 head = {dneo_head - dflash2_head:+.3f} (text +0.056)")
print(f"  Table 6: DNeo head - DSpark head   = {dneo_head - dspark_head:+.3f} (text +0.141)")
print("  Table 8 (p. 21), a different additive setup, gives both text numbers:")
quote(doc, 21, "+ per-layer MoFA routing 2.505 +0.001 + dense DFlash-2 score head 2.590 +0.085 + fused DNeo head 2.646 +0.056")
print(f"  Table 8: 2.646 - 2.590 = {2.646 - 2.590:+.3f}, 2.646 - 2.505 = {2.646 - 2.505:+.3f}")

print("\n2. Transformers throughput at B = 32: Sec. 5.3 text versus Table 3 (p. 12)")
quote(doc, 12, "DNeo also achieves up-to +58% higher throughput (at B=32) than DFlash-2 (Transformers serving)")
quote(doc, 12, "DFlash-2 590 2,023 5,781 7,971 9,318 272 743 1,303 1,475 1,511")
quote(doc, 12, "DNeo (ours) 705 2,247 6,580 9,058 10,324 404 1,101 2,033 2,201 2,269")
dflash2 = dict(zip([1, 4, 16, 32, 64], [272, 743, 1303, 1475, 1511]))
dneo = dict(zip([1, 4, 16, 32, 64], [404, 1101, 2033, 2201, 2269]))
for b in dneo:
    print(f"  Transformers B = {b:2d}: {dneo[b]:5d} / {dflash2[b]:5d} = {dneo[b] / dflash2[b] - 1:+.1%}")

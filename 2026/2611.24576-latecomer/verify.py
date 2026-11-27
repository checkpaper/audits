"""Reproduce the checks on Late Entry in Looped Language Models, arXiv:2611.24576v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.24576", "v1", "92186e9f9735ae2415cd51421daa3bc03027093707d9e62c0c23862fecd2d6b2")

print("1. Synchronous cache completion at K = 2: Sec. 2 / Fig. 2 versus Table 14")
quote(doc, 5, "Running the final two passes per token while synchronously completing each emitted token’s four-pass cache before the next step (𝐷= 4) lifts accuracy to .853 (+10.4 points) on GSM8K and .708 (+12.0 points) on IFEval.")
quote(doc, 27, "Table 14. Cache-completion policy ablation on full GSM8K (𝑛= 1,319) and IFEval (𝑛= 541).")
quote(doc, 27, "Synchronous (repair before next step) Sequential .852 .864 .684 .717")
print("  Same decoder (K = 2, one token per step, four-pass cache completed before the next step):")
print(f"  GSM8K .853 vs .852 ({round(.853 * 1319)} vs {round(.852 * 1319)} of 1,319); IFEval .708 vs .684 ({round(.708 * 541)} vs {round(.684 * 541)} of 541)")

print("\n2. 'cutting rollbacks 2x to 16x' (p. 18) versus the rollback columns of the same table")
quote(doc, 18, "margin gating (𝜏∈[0.15, 0.30]) filters benign near-tie flips (Δ𝑧≤𝜏), cutting rollbacks 2× to 16×")
rows = {
    "GSM8K K = 3": ("GSM8K 𝐾= 3 .868 (62.3) .867 4.13× .867 1.14 4.19× (+2%) .870 (.25) 0.29", 1.14, 0.29),
    "GSM8K K = 2": ("GSM8K 𝐾= 2 .868 (62.3) .867 4.13× .867 2.02 5.20× (+26%) .877 (.15) 1.26", 2.02, 1.26),
    "MATH500 K = 2": ("MATH500 𝐾= 2 .532 (62.7) .526 4.08× .526 2.11 5.23× (+28%) .548 (.30) 0.96", 2.11, 0.96),
    "IFEval K = 2": ("IFEval 𝐾= 2 .732 (63.8) .739 2.15× .739 5.98 2.66× (+24%) .719 (.15) 4.08", 5.98, 4.08),
    "MBPP K = 2": ("MBPP 𝐾= 2 .616 (63.4) .626 3.79× .626 2.00 4.61× (+22%) .618 (.30) 0.70", 2.00, 0.70),
}
print("  Ouro-2.6B rollback column (rb), tau = 0 Wake -> margin-gated Wake:")
for name, (q, a, b) in rows.items():
    quote(doc, 18, q)
    r = a / b
    print(f"  {name:14s} {a:.2f} -> {b:.2f}  = {r:.2f}x{'   <-- below 2x' if r < 2 else ''}")

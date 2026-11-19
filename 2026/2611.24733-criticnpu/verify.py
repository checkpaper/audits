"""Reproduce the check on CriticNPU, arXiv:2611.24733v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.24733", "v1", "1ffdc09ad8cbda318ae9bb125d8927ab65c94d748681b4063c52eef04433516d")

print("1. CMA-ES decode win rate: App. E.1 caption (p. 23) versus Table 1 (p. 7)")
quote(doc, 23, "CMA-ES’s fast convergence on decode is a local-minimum artefact — its decode win rate in Table 1 is 0–3 of 16.")
quote(doc, 7, "CMA-ES 0/16 130 3/16 130 3/16 130 2/16 130 0/16 130 0/16 130")
quote(doc, 7, "CMA-ES 16/16 130 16/16 130 16/16 130 16/16 130 7/16 130 10/16 130")
print("  Table 1 lists the prefill block first; CMA-ES wins 0, 3, 3, 2, 0, 0 of 16 on prefill")
print("  and 16, 16, 16, 16, 7, 10 of 16 on decode (81 of 96).")

print("\n2. Base-LLM generalization: App. E.3 text (p. 24) versus Table 12 (p. 28)")
quote(doc, 24, "Final latencies are within 5% of the default on every workload; the largest single deviation is "
               "GPT-4o on Llama3-8B prefill (+2.1% TTFT).")
quote(doc, 28, "Llama2-13B GPT-5.4-mini (default) 633.5 41 18.29 13 — — GPT-4o 633.5 57 14.07 15 0% −23% "
               "GPT-4o-mini 633.5 50 14.07 14 0% −23%")
quote(doc, 28, "DSv2-236B GPT-5.4-mini (default) 8701.1 41 156.89 15 — — GPT-4o 8933.0 60 156.89 15 +2.7% 0% "
               "GPT-4o-mini 8920.6 64 156.89 15 +2.5% 0%")
print(f"  Llama2-13B TPOT: 14.07 / 18.29 - 1 = {14.07 / 18.29 - 1:+.1%} for both GPT-4o and GPT-4o-mini")
print(f"  DSv2-236B TTFT:  8933.0 / 8701.1 - 1 = {8933.0 / 8701.1 - 1:+.1%} (GPT-4o), "
      f"8920.6 / 8701.1 - 1 = {8920.6 / 8701.1 - 1:+.1%} (GPT-4o-mini)")

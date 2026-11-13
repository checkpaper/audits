"""Reproduce the check on InfraRSI, arXiv:2611.11558v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.11558", "v1", "d6f235002e94b2b84a0bcc45bb36538d08e4b3c029cf244bb665a039b08445c2")

print("Qwen3.5-9B (8xH100): Section 4.1 and Section 6.1 versus Table 5")
quote(doc, 8, "In our Qwen3.5-9B (8×H100) run, the experience-seeded first start reaches 1.55× on Trial 1 "
              "before subsequent search advances to 1.73×.")
quote(doc, 13, "lifts final speedups to 1.55× (45.4% MFU) and 1.73× (43.8% MFU), respectively")
quote(doc, 14, "Qwen3.5-9B (8×H100) Cold start (no prior packs) 1.22× (Trial 2) 1.70×")
quote(doc, 14, "Qwen3.5-9B (8×H100) All eligible packs 1.24× (Trial 1) 1.70×")
quote(doc, 14, "Qwen3.5-9B (8×H100) Cross-SKU transfer 1.23× (Trial 1) 1.82×")
quote(doc, 14, "Cold start Cross-SKU packs All eligible packs All packs")
first = {"cold start": 1.22, "all eligible packs": 1.24, "cross-SKU transfer": 1.23}
final = {"cold start": 1.70, "all eligible packs": 1.70, "cross-SKU transfer": 1.82}
print(f"  Table 5 first trial: {first}; the text gives 1.55 (Trial 1), {1.55 / max(first.values()):.2f}x the highest")
print(f"  Table 5 final: {final}; the text gives 1.73, which matches none of them")
print("  Figure 4(a) lists a fourth condition, 'All packs', that Table 5 does not report.")

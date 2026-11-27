"""Reproduce the checks on Future-OPSD, arXiv:2611.26954v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.26954", "v1", "669b3edd1c49ee9c4e12e86967bfc938041375c4de087fac1bebe302ea28068a")

print("1. Table 6 (p. 8), Score column for Qwen3-VL-8B")
quote(doc, 8, "EgoPlan-IT SFT 4.0 63.4 0.62 44.3 Naive OPSD 9.4 53.6 3.28 48.9 Future-OPSD 11.2 54.0 3.77 53.6")
quote(doc, 8, "Future-L1 SFT 1.4 68.4 0.20 57.3 Naive OPSD 4.3 43.0 1.60 61.2 Future-OPSD 5.7 42.5 1.73 66.9")
print("Table 1 (p. 5), Qwen3-VL-8B trained on Future-L1: TwiFF-Bench CoT / Ans. / Avg")
quote(doc, 5, "SFT [55] ✓ 61.3 55.7 58.5 33.8 35.1 33.4")
quote(doc, 5, "Naive OPSD [63] – 66.0 56.4 61.2 45.9 47.3 38.7")
quote(doc, 5, "Future-OPSD – 71.9 63.5 67.8 46.1 48.3 40.0")
print("Table 2 (p. 5), Qwen3-VL-8B trained on EgoPlan-IT: SEED-Bench-R1 L1 / L2 / L3")
quote(doc, 5, "SFT [55] ✓ 47.4 48.6 42.9 50.0 45.7 47.8")
quote(doc, 5, "Naive OPSD [63] – 50.1 51.7 44.9 60.9 47.7 54.3")
quote(doc, 5, "Future-OPSD – 54.3 55.8 50.6 63.8 53.1 58.5")
t2 = {"SFT": (47.4, 48.6, 42.9), "Naive OPSD": (50.1, 51.7, 44.9), "Future-OPSD": (54.3, 55.8, 50.6)}
t1 = {"SFT": 58.5, "Naive OPSD": 61.2, "Future-OPSD": 67.8}
t6 = {"EgoPlan-IT": {"SFT": 44.3, "Naive OPSD": 48.9, "Future-OPSD": 53.6},
      "Future-L1": {"SFT": 57.3, "Naive OPSD": 61.2, "Future-OPSD": 66.9}}
print()
for m, v in t2.items():
    main = sum(v) / 3
    print(f"  EgoPlan-IT {m:12s} Table 6 {t6['EgoPlan-IT'][m]:5.1f}  Table 2 SEED L1-L3 mean {main:.2f}"
          f"  {'match' if abs(main - t6['EgoPlan-IT'][m]) < 0.06 else 'DIFFERENT'}")
for m, v in t1.items():
    print(f"  Future-L1  {m:12s} Table 6 {t6['Future-L1'][m]:5.1f}  Table 1 TwiFF Avg {v:5.1f}"
          f"  {'match' if v == t6['Future-L1'][m] else 'DIFFERENT'}")

print()
print("2. Table 1 (p. 5), Qwen3.5-9B Future-OPSD, General Video Understanding Avg")
quote(doc, 5, "Future-OPSD – 70.4 66.1 68.2 45.4 47.1 38.0 79.3 21.5 63.1 65.9 57.2")
quote(doc, 5, "Qwen3.5-9B Base – 62.4 54.5 58.5 44.3 44.9 37.9 79.9 21.4 61.2 65.6 57.0")
fo, base = (79.3, 21.5, 63.1, 65.9), (79.9, 21.4, 61.2, 65.6)
print(f"  mean of Temp./T-B./V-M./MVB: Future-OPSD {sum(fo) / 4:.3f} (printed 57.2), Base {sum(base) / 4:.3f} (printed 57.0)")

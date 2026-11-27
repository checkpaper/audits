"""Reproduce the checks on BLIP-Live, arXiv:2611.21553v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.21553", "v1", "060f1cc674bee668ee646aafdf10880ad8e36560432a295f3b5ee1c88244a0de")

print("1. Table A.10 (p. 22), human preference study, WEB split")
quote(doc, 22, "WEB v1 0 0 1 0 0 4 3 0 2 2 12 6.0 v2 20 20 19 20 16 17 18 20 18 18 188 94.0")
v1 = [0, 0, 1, 0, 0, 4, 3, 0, 2, 2]
v2 = [20, 20, 19, 20, 16, 17, 18, 20, 18, 18]
print(f"  sum of v1 cells {sum(v1)} (printed 12), sum of v2 cells {sum(v2)} (printed 188)")
print(f"  per-rater v1 + v2: {[a + b for a, b in zip(v1, v2)]} (10 raters x 20 videos would give 20 each)")
print(f"  v2 share from the cells: {sum(v2)}/{sum(v1) + sum(v2)} = {100 * sum(v2) / (sum(v1) + sum(v2)):.2f}%")

print()
print("2. Table 9 (p. 9), StreamingBench PO, which says it follows the official leaderboard")
quote(doc, 9, "Table 9: StreamingBench Proactive Split (PO) time accuracy (follow official leaderboard)")
quote(doc, 9, "Gemini 1.5 Pro 45.10 – GPT-4o 39.22 – Claude 3.5 Sonnet 35.29 – VideoLLM-Online 1.96 – VITA-1.5 25.49")
quote(doc, 9, "Gemma4-A4B 36.80 38.9 Qwen3.5-A3B 25.20 15.1 BLIP-Live-Gemma 44.00 48.6 BLIP-Live-Qwen 47.60 54.6")


def fits(v, n):
    """k/n for some integer k that rounds to v at two decimals, or None."""
    k = round(v * n / 100)
    return k if f"{100 * k / n:.2f}" == f"{v:.2f}" else None


rows = {"Gemini 1.5 Pro": 45.10, "GPT-4o": 39.22, "Claude 3.5 Sonnet": 35.29, "VideoLLM-Online": 1.96,
        "VITA-1.5": 25.49, "MiniCPM-o 2.6": 29.41, "VideoChat3": 9.80,
        "Gemma4-A4B": 36.80, "Qwen3.5-A3B": 25.20, "BLIP-Live-Gemma": 44.00, "BLIP-Live-Qwen": 47.60}
for name, v in rows.items():
    k51, k250 = fits(v, 51), fits(v, 250)
    print(f"  {name:18s} {v:6.2f}  k/51: {f'{k51}/51' if k51 is not None else 'none':6s}  k/250: {f'{k250}/250' if k250 is not None else 'none'}")

"""Reproduce the check on uni-robot-agent (Democratizing Robot-Use Agents), arXiv:2611.01560v2.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.01560", "v2", "ffbc3556590a22c177d27461283dc3609fd482c4d5525dea960459208609e92d")

print("Section 5.1 (p. 16): how much of its score does GPT-6 Astra keep without depth?")
quote(doc, 16, "one seed and one layout per task for Astra due to limited evaluation costs")
quote(doc, 16, "Astra’s score changes from 55.83 to 55.04, and Qwen’s score changes from 35.89 to 31.39, "
               "retaining 98.6% and 87.5% of their depth-enabled scores")
quote(doc, 10, "GPT-6 Astra uni-robot-agent 31.94/37.15 20.83/28.75 39.58/50.31 80.56/80.56 60.42/62.71 46.67/51.90")
quote(doc, 10, "GPT-6 Astra uni-robot-agent + depth 43.06/47.85 29.17/36.04 52.08/60.31 75.00/75.42 62.50/64.17 52.36/56.76")
quote(doc, 18, "Astra, Qwen, and DeepSeek each use 252 episodes.")
print(f"  Section 5.1, 42 episodes: Astra {55.04 / 55.83:.1%}, Qwen {31.39 / 35.89:.1%}")
print(f"  Table 1, 252 episodes:    Astra {51.90 / 56.76:.1%} (drop {56.76 - 51.90:.2f}), Qwen {31.39 / 35.89:.1%} (drop {35.89 - 31.39:.2f})")

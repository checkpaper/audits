"""Reproduce the checks on Coding4Games: Can Modern Coding Agents Play Modern Video Games?, arXiv:2611.31974v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.31974", "v1", "158def233591b7b32972ae7bcf35cf029121022fb61706491cd843b710daffe4")

print("1. Table 4 (p. 7): G0-G4 are percentages of final programs, so each row should sum to 100")
quote(doc, 7, "G0–G4 show the percentage of final programs at each grounding level.")
rows = {
    "GPT-6-Astra": "GPT-6-Astra 13.3 0.0 26.7 60.0 0.0",
    "GPT-5.6-Sol": "GPT-5.6-Sol 9.1 63.6 27.3 0.0 0.0",
    "GPT-5.6-Terra": "GPT-5.6-Terra 18.2 63.6 9.1 9.1 0.0",
    "Claude-Opus-5.5": "Claude-Opus-5.5 20.0 0.0 13.3 46.7 20.0",
    "Claude-Opus-5": "Claude-Opus-5 0.0 10.0 20.0 20.0 50.0",
    "Claude-Sonnet-5": "Claude-Sonnet-5 0.0 18.2 36.4 27.3 18.2",
    "Gemini-3.8-flash": "Gemini-3.8-flash 9.1 18.2 18.2 36.4 18.2",
    "Qwen3.8-flash": "Qwen3.8-flash 20.0 0.0 10.0 20.0 50.0",
    "Qwen3.8-27B": "Qwen3.8-27B 0.0 0.0 20.0 50.0 30.0",
    "GLM-5.3-Flash": "GLM-5.3-Flash 30.0 30.0 10.0 30.0 0.0",
    "deepseek-v4.1-flash": "deepseek-v4.1-flash 0.0 0.0 10.0 50.0 30.0",
    "Kimi-K3": "Kimi-K3 9.1 9.1 27.3 18.2 36.4",
}
for name, q in rows.items():
    quote(doc, 7, q)
    total = sum(float(x) for x in q.split()[-5:])
    print(f"  {name:20s} G0-G4 sum {total:6.1f}{'   <-- not 100' if abs(total - 100) > 0.2 else ''}")

print("\n2. Table 1 (p. 3): Mode column vs caption")
quote(doc, 3, "with low-level GUI inputs and stepped execution throughout development and evaluation.")
quote(doc, 3, "Coding4Games (ours) Coding agents Modern 15 Program ✓ GUI Live ✓ ✓")

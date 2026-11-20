"""Reproduce the check on AnyS1 (Thinking Fast, Anywhere), arXiv:2611.23751v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.23751", "v1", "40ba052a368ace0f9e0118ca20403679674cb5ea865602469f7a0e11191adc90")

print("1. 'more than fourfold' (Sec. 4.3, p. 7) vs Table 5 (p. 15)")
quote(doc, 7, "equal-rate random delegation multiplies System-2")
quote(doc, 7, "more than fourfold (Appendix C)")
quote(doc, 15, "SOPBench 0.014 0.086 98.0% 92.7 / 7.1 91.4 / 8.4")
quote(doc, 15, "ALFWorld 0.100 0.318 50.4% 92.4 / 3.8 68.2 / 16.0")
quote(doc, 15, "WebShop 0.156 0.302 41.4% 84.3 / 6.5 69.8 / 12.5")
for name, gate, rand in [("SOPBench", 7.1, 8.4), ("ALFWorld", 3.8, 16.0), ("WebShop", 6.5, 12.5)]:
    print(f"  {name}: random / gate disagreements = {rand} / {gate} = {rand / gate:.2f}x")

print("\n2. Table 4 bold in the Dev column (p. 15)")
quote(doc, 15, "Bold: column best.")
quote(doc, 15, "Qwen3.5-27B 85.9 93.8 77.2 56.8")
quote(doc, 15, "Option-interaction head (System-1) 83.8 93.5 68.9 41.5")
for b in doc[14].get_text("dict")["blocks"]:
    for line in b.get("lines", []):
        for s in line["spans"]:
            if s["text"].strip() in ("85.9", "83.8"):
                bold = s["font"].endswith("Medi") or bool(s["flags"] & 16)
                print(f"  {s['text'].strip()}: font {s['font']}, bold = {bold}")
print("  The Dev maximum is 85.9 (zero-shot Qwen3.5-27B), but 83.8 is the bolded cell.")

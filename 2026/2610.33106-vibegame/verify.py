"""Reproduce the check on VibeGame, arXiv:2610.33106v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.33106", "v1", "63631951dcd077e35b896025354417b8562a686166ae0f0048ac3f0b5ffb6512")

print("Section 4.2 (p. 8) versus Table 1 (p. 6): GPT-5.6-Luna, P2G versus PA2G")
quote(doc, 8, "GPT-5.6-Luna [35] does not turn image generation into a visual advantage in the P2G setting")
rows = {
    "Qwen Code": ("Qwen Code [28] GPT-5.6-Luna PA2G 46.38 32.18 27.88 37.15 35.45", "Qwen Code GPT-5.6-Luna P2G 48.68 34.44 35.51 38.72 38.29"),
    "Kimi Code": ("Kimi Code GPT-5.6-Luna PA2G 47.54 31.86 29.67 38.46 36.22", "Kimi Code [29] GPT-5.6-Luna P2G 45.26 32.13 31.00 38.34 36.14"),
    "Codex": ("Codex [7] GPT-5.6-Luna PA2G 50.72 33.32 28.33 36.87 36.47", "Codex GPT-5.6-Luna P2G 45.22 34.47 31.54 37.65 36.77"),
}
for harness, (pa2g, p2g) in rows.items():
    quote(doc, 6, pa2g)
    quote(doc, 6, p2g)
    v_pa, a_pa = float(pa2g.split()[-3]), float(pa2g.split()[-2])
    v_p, a_p = float(p2g.split()[-3]), float(p2g.split()[-2])
    print(f"  {harness:9} Functional Visuals P2G - PA2G = {v_p - v_pa:+.2f}; Art & Presentation {a_p - a_pa:+.2f}")

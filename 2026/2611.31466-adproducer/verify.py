"""Reproduce the checks on AdProducer: Towards Agentic Advertising Video Generation, arXiv:2611.31466v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.31466", "v1", "eb5ef1a880e9af4979566c18b56a8bcd68e7384ee86836d6802df7dbc024e06b")

print("1. Table 1 (p. 7): Overall vs the count-weighted mean of Recent (122), Long-tail (130), Evergreen (53)")
quote(doc, 6, "evergreen (53), focusing on lesser-known component-level details")
quote(doc, 7, "Recent Long-tail Evergreen PG-Score Overall")
rows = [
    ("Veo 3.1 Lite", "Veo 3.1 Lite [12] 5.2 15.3 58.4 53.7 54.6 24.9 28.7 30.8 27.8"),
    ("Veo 3.1 Fast", "Veo 3.1 Fast [12] 5.1 16.9 56.2 57.9 57.9 26.5 29.8 28.6 28.4"),
    ("Veo 3.1", "Veo 3.1 [12] 6.3 15.1 56.1 55.6 55.6 24.2 29.5 31.3 28.0"),
    ("CogVideoX1.5-5B", "CogVideoX1.5-5B [67] 0.7 0.0 4.5 2.0 1.0 0.8 2.5 0.8 1.5"),
    ("HunyuanVideo-13B", "HunyuanVideo-13B [28] 0.8 0.0 3.2 4.4 35.2 4.5 5.0 6.6 5.1"),
    ("LTX-2-19B", "LTX-2-19B [15] 0.5 0.0 6.5 7.2 16.9 3.2 4.8 4.0 4.0"),
    ("Mochi-1-10B", "Mochi-1-10B [11] 1.2 0.0 8.8 5.2 12.1 3.2 4.3 5.5 4.1"),
    ("Wan2.2-T2V-A14B", "Wan2.2-T2V-A14B [55] 1.8 0.1 12.7 6.6 36.6 6.6 8.4 9.0 7.8"),
    ("MiniMax H3", "MiniMax H3 [43] 3.5 1.3 34.1 39.7 44.9 16.7 17.5 18.3 17.3"),
    ("AdProducer + Veo 3.1", "AdProducer + Veo 3.1 25.7 15.2 55.4 50.0 61.2 34.6 36.5 37.4 35.9"),
    ("AdProducer + MiniMax H3", "AdProducer + MiniMax H3 36.5 40.4 71.6 64.9 76.2 56.8 46.7 49.6 51.3"),
]
for name, q in rows:
    quote(doc, 7, q)
    r, l, e, overall = (float(x) for x in q.split()[-4:])
    w = (122 * r + 130 * l + 53 * e) / 305
    # each regime value is rounded to 0.1, so the weighted mean can move by at most 0.05
    flag = "   <-- outside rounding" if abs(w - overall) > 0.05 + 0.05 else ""
    print(f"  {name:24s} weighted {w:6.2f}   reported {overall:5.1f}{flag}")

print("\n2. Earliest year: Fig. 5 caption vs Sec. 5.1")
quote(doc, 5, "covering a broad time span from 1836 to 2026.")
quote(doc, 6, "widely recognized products released from 1876 to 2022.")

"""Reproduce the checks on Playfulness as Feedback for Agentic Game Development (Play2Evolve), arXiv:2611.33457v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.33457", "v1", "11d7e9098418874a4d0f70266c4133c55568d454b5c74a8a0625d342cc75203a")

print("1. Table 8 (15 games) versus Table 4 (10 games)")
quote(doc, 8, "Table 4. GameCraft-Bench means from a 10-game successive-evolution study.")
t4 = {"V0": "66.25 53.46 61.80 42.33 52.74", "V1": "73.80 57.18 65.34 44.87 56.59", "V2": "74.05 57.32 68.57 47.88 58.21"}
quote(doc, 8, "V0 " + t4["V0"] + " V1 " + t4["V1"] + " V2 " + t4["V2"])
quote(doc, 18, "Table 8. GameCraft-Bench scores for continued Refinement and Evolution on 15 games")
quote(doc, 18, "V0 " + t4["V0"] + " V1 " + t4["V1"] + " V1 + Refinement 73.75 57.24 65.20 45.02 56.63 V1 + Evolution (V2) " + t4["V2"])
print("  The V0, V1 and V2 rows of Table 8 (15 games) repeat Table 4 (10 games) in all 15 cells.")

print("\n2. GameASG-Bench strict task success (Table 2, p. 7) on 47 tasks")
quote(doc, 27, "all 47 GameASG-Bench tasks across 12 categories")
quote(doc, 7, "Initialization (V0) 35.7% 92.7 89.3")
quote(doc, 7, "Refinement (V1) 57.4% 95.1 94.5")
for pct in (35.7, 57.4):
    ks = [k for k in range(48) if round(100 * k / 47, 1) == pct]
    near = sorted(range(48), key=lambda k: abs(100 * k / 47 - pct))[:2]
    print(f"  {pct}%: k/47 matches {ks or 'none'}; nearest " + ", ".join(f"{k}/47 = {100 * k / 47:.2f}%" for k in sorted(near)))

print("\n3. Overall = 0.15 M + 0.35 D + 0.15 V + 0.35 A (weights stated on p. 18), Table 1 (p. 7)")
quote(doc, 18, "weights of 0.15, 0.35, 0.15, and 0.35 for M, D, V, and A")
rows = {"Initialization (V0)": "68.70 48.83 51.63 44.76 50.81", "Play2Code": "69.84 50.07 51.95 51.77 52.46",
        "Refinement (V1)": "72.97 52.38 52.50 49.35 54.45", "Evolution (V2)": "78.02 56.39 57.51 57.03 60.05"}
for name, r in rows.items():
    quote(doc, 7, f"{name} {r}")
    m, d, v, a, o = map(float, r.split())
    calc = 0.15 * m + 0.35 * d + 0.15 * v + 0.35 * a
    flag = "" if abs(calc - o) < 0.05 else "   <-- differs"
    print(f"  {name:20s} printed {o:.2f}, recomputed {calc:.2f}{flag}")

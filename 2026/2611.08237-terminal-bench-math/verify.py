"""Reproduce the checks on Terminal-style Mathematical Modeling Bench, arXiv:2611.08237v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.08237", "v1", "6e9a9bfe49ea09e4a345e0618483e6c24d6aec828bf431b7d9b3eaf23517ff55")

# Table 6 (p. 16): per-task multi-reference O-EVAL (%), tasks in table order.
TASKS = ["heliostat", "multibeam", "vegetable", "dragon", "production", "crop", "smoke", "sic", "nipt",
         "plant", "maasai", "wordle", "lamprey", "submersible", "tennis", "stair", "juneau", "olympic"]
T6 = {
    "GPT-6 Astra": [86.2, 94.0, 64.3, 83.4, 95.7, 88.2, 100.0, 88.2, 46.4, 21.3, 34.5, 46.1, 47.1, 100.0, 36.4, 21.4, 42.9, 66.4],
    "Fable 5.1": [80.7, 80.5, 64.3, 83.4, 80.5, 83.5, 100.0, 86.7, 77.0, 24.6, 35.1, 49.6, 43.8, 100.0, 36.4, 13.1, 42.9, 54.1],
    "GPT-5.5 xhigh": [80.5, 91.7, 64.3, 83.4, 87.2, 99.7, 100.0, 80.3, 29.7, 27.7, 43.1, 40.9, 10.7, 100.0, 9.1, 12.9, 42.9, 71.2],
    "DeepSeek-Flash": [80.2, 59.3, 64.3, 83.4, 87.2, 63.8, 100.0, 78.7, 76.4, 27.7, 43.1, 56.4, 60.9, 100.0, 9.1, 12.8, 42.9, 30.1],
}
TABLE2 = {"GPT-6 Astra": (64.58, 1.132), "Fable 5.1": (63.11, 1.081), "GPT-5.5 xhigh": (59.75, 0.998), "DeepSeek-Flash": (59.81, 1.000)}

quote(doc, 16, "Each column’s mean equals that entry’s main-table O-EVAL")
quote(doc, 16, "mcm-2024-c-tennis 36.4 36.4 9.1 9.1")
quote(doc, 16, "Average 64.58 63.11 59.75 59.81")

print("\n1. The literature-split tennis task and the headline board")
quote(doc, 6, "We mark such literature-split tasks explicitly and exclude them from any headline ranking")
quote(doc, 10, "we mark the task literature-split and keep it out of headline rankings")
quote(doc, 8, "Main results: the seven multimodal entries, 18 tasks, sorted by O-EVAL")
t = TASKS.index("tennis")
for name, v in T6.items():
    print(f"  {name}: 18-task mean {sum(v) / 18:.2f} (Table 2: {TABLE2[name][0]}), without tennis {(sum(v) - v[t]) / 17:.2f}")

print("\n2. The gap between GPT-5.5 and DeepSeek-Flash")
quote(doc, 7, "the ∼1.5 pp separation between the two leaders and between GPT-5.5 and Flash sits inside one standard deviation")
quote(doc, 8, "DeepSeek-Flash + opencode 18 59.81 ± 1.25 1.000 2.54 GPT-5.5 xhigh + codex 18 59.75 ± 1.55 0.998 ± 0.01")
print(f"  Leaders: 64.58 - 63.11 = {64.58 - 63.11:.2f} pp; GPT-5.5 vs Flash: 59.81 - 59.75 = {59.81 - 59.75:.2f} pp")

print("\n3. MULTI-BO recomputed from Table 6 with Eq. (2)")
quote(doc, 6, "when the remaining headroom 1 −ft is below 0.10 we fall back to 1 + clip(Ot − ft, ±0.10)")
f = [x / 100 for x in T6["DeepSeek-Flash"]]
for name, v in T6.items():
    s = []
    for o, ft in zip((x / 100 for x in v), f):
        g = max(-0.10, min(0.10, o - ft)) if 1 - ft < 0.10 else max(-1, min(1, (o - ft) / (1 - ft)))
        s.append(1 + g)
    print(f"  {name}: {sum(s) / len(s):.3f} (Table 2: {TABLE2[name][1]:.3f})")
quote(doc, 8, "claude-code 59.83 ± 1.13 1.081 ± 0.05")
quote(doc, 8, "Fable 5.1 + claude-code 18 63.11 ± 1.33 1.081 ± 0.05")
print("  Table 3: DeepSeek-Flash under claude-code is 0.02 pp above opencode in O-EVAL, with the same MULTI-BO (1.081 ± 0.05) as Fable 5.1.")

print("\n4. Smaller slips")
quote(doc, 4, "21 unique figures across 6 tasks are load-bearing")
fig = {"heliostat": 2, "multibeam": 8, "dragon": 5, "production": 1, "sic": 2, "wordle": 2, "stair": 1}
quote(doc, 15, "Total 21 60†")
print(f"  Table 5 #Fig. is non-zero for {len(fig)} tasks ({', '.join(fig)}), total {sum(fig.values())}")
quote(doc, 17, "the paper’s isolated value 1.406276 m/s (with ratio 1.422195) implies 2.2568 m/s at a handle")
quote(doc, 19, "1.406276 × 1.604793 = 2.2568 m/s")
print(f"  1.406276 x 1.422195 = {1.406276 * 1.422195:.4f}; 1.406276 x 1.604793 = {1.406276 * 1.604793:.4f}")

"""Reproduce the check on The Surprising Effectiveness of Deleting Weights in LLM Post-Training, arXiv:2611.10866v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.10866", "v1", "7611c5008fd0f42ee97933257573735a987598449a89720e23edee60a4225a04")


def on_grid(x, n):
    """True if x (a percentage with 2 decimals) equals 100 k / n for some integer k."""
    k = round(x * n / 100)
    return any(round(100 * j / n, 2) == x for j in (k - 1, k, k + 1))


print("Protocol")
quote(doc, 6, "Evaluation uses greedy decoding, and we report the best validation accuracy across saved checkpoints.")

print("\n1. Table 1 (p. 7), Llama on GSM8K (test set: 1,319 problems)")
quote(doc, 7, "Base 1.21 0 53.53 0 60.27 0")
rows = {
    "Base": "Base 1.21 0 53.53 0 60.27 0",
    "FFT": "FFT 60.50 4714 82.49 12256 83.24 30633",
    "LoRA r=1": "LoRA r=1 59.29 2.7 82.39 5.8 83.38 10.0",
    "LoRA r=4": "LoRA r=4 60.58 10.8 82.44 23.2 82.87 40.0",
    "MTH 99%": "MTH 99% 60.73 68.2 80.53 177.4 83.31 443.6",
    "MTH 99.95%": "MTH 99.95% 58.61 4.1 82.17 10.7 83.07 26.6",
    "Deletion Tuning": "Deletion Tuning 54.44 1.0 81.49 3.1 83.55 8.4",
}
off = []
for name, q in rows.items():
    quote(doc, 7, q)
    nums = [float(x) for x in q.split()[-6:]]
    for size, acc in zip(("1B", "3B", "8B"), nums[0::2]):
        if not on_grid(acc, 1319):
            off.append(f"{name} {size} {acc:.2f}")
print(f"  not k / 1319: {len(off)} of 21 -> " + "; ".join(off))

print("\n2. Table 8 (p. 18), OlympiadBench column (SimpleRL-Zoo test set: 675 problems)")
olympiad = [7.73, 8.92, 10.55, 9.36, 7.28, 6.98, 26.45, 31.35, 28.68, 29.68, 27.93, 25.78,
            39.92, 39.52, 39.97, 39.82, 38.78, 40.29]
for q in ["FFT 48.07 36.00 4.78 7.73 0.00 17.50", "Deletion Tuning 44.12 33.40 5.51 6.98 3.33 12.50",
          "FFT 91.43 78.20 33.46 39.92 13.33 55.00", "Deletion Tuning 91.28 78.80 32.72 40.29 23.33 47.50"]:
    quote(doc, 18, q)
print(f"  on the k / 675 grid: {sum(on_grid(x, 675) for x in olympiad)} of 18")
best = max(range(50, 3001), key=lambda n: sum(on_grid(x, n) for x in olympiad))
print(f"  no n in 50-3000 fits all 18; best n = {best} fits {sum(on_grid(x, best) for x in olympiad)}")
for name, n, col in [("GSM8K", 1319, [48.07, 49.20, 52.46, 50.34, 49.73, 44.12, 83.62, 86.81, 85.60, 86.28, 85.37, 83.78,
                                       91.43, 92.65, 91.66, 91.21, 92.04, 91.28]),
                     ("Minerva", 272, [4.78, 7.35, 8.82, 10.29, 6.25, 5.51, 23.16, 21.69, 22.79, 22.43, 22.79, 22.79,
                                       33.46, 27.21, 29.04, 29.78, 31.62, 32.72])]:
    print(f"  for comparison, Table 8 {name} on k / {n}: {sum(on_grid(x, n) for x in col)} of 18")

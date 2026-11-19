"""Reproduce the check on HINT-WAM, arXiv:2611.24789v1.

Run: python verify.py
"""
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.24789", "v1", "2ff80709c9cf93cadbf4fae5606d20f95dc8ce9625db9d60e7c7e3a576f9e859")

print("Table 6 (p. 13): paired statistics over 90 LIBERO-90 tasks")
rows = [("HINT-WAM vs. SFT", 6.30, 1.76, 3.58, 36, 22, "0.087"),
        ("HINT-WAM vs. self-imitation", 5.56, 1.88, 2.96, 47, 23, "0.0056"),
        ("HINT-WAM vs. shuffled hindsight", 4.90, 1.78, 2.76, 45, 25, "0.022"),
        ("HINT-WAM vs. velocity matching", 6.16, 1.59, 3.62, 48, 17, "0.00042"),
        ("Velocity matching vs. SFT", 0.14, 1.52, 0.09, 30, 37, "0.46")]
for name, d, se, t, w, l, p in rows:
    quote(doc, 13, f"{name} +{d:.2f} {se:.2f} {t:.2f} {w} / {l} /")
print("Sec. 4.3 (p. 8)")
quote(doc, 8, "6.16% above velocity matching (paired t = 3.62, 48 wins vs. 17 losses, sign-test p = 0.0004)")

print("\n  comparison                        diff/SE  range allowed by rounding   reported t")
for name, d, se, t, w, l, p in rows:
    lo, hi = (d - 0.005) / (se + 0.005), (d + 0.005) / (se - 0.005)
    ok = "" if lo <= t + 0.005 and t - 0.005 <= hi else "   <- outside"
    print(f"  {name:32s} {d / se:6.3f}   [{lo:.3f}, {hi:.3f}]          {t:.2f}{ok}")
print(f"  SE implied by t = 3.62: {6.16 / 3.62:.2f}")
print("\n  comparison                        wins/losses  exact two-sided sign test  reported p")
for name, d, se, t, w, l, p in rows:
    n, k = w + l, min(w, l)
    exact = min(1, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n)
    print(f"  {name:32s} {w:3d} / {l:<3d}     {exact:.5f}                  {p}")

print("\nLIBERO-90 success rates: 90 tasks x 50 trials, so every rate is k/4500 (Sec. 4.1 p. 6, App. D p. 12)")
quote(doc, 6, "evaluate each task with 50 trials from the fixed initial states of LIBERO")
quote(doc, 12, "All LIBERO-90 numbers in the paper, including the released Fast-WAM and the BC control, use 50 trials per task.")
quote(doc, 7, "With replay SFT 76.70")
quote(doc, 8, "reaches 80.63%")
quote(doc, 15, "noised demonstrations instead reach only 80.74%")
for label, v in [("SFT + replay (Table 2)", 76.70), ("MMD (Sec. 4.3)", 80.63), ("noised demonstrations (Fig. 7 text)", 80.74),
                 ("HINT-WAM (Table 1)", 85.18), ("velocity matching (Sec. 4.3)", 79.02)]:
    k = math.floor(v * 45)
    near = [100 * j / 4500 for j in (k, k + 1)]
    fits = any(round(x, 2) == v or math.floor(x * 100) / 100 == v for x in near)
    print(f"  {label:38s} {v:6.2f}  nearest k/4500: {near[0]:.3f}, {near[1]:.3f}  {'fits' if fits else 'not attainable'}")

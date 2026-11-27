"""Reproduce the check on EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models, arXiv:2611.06748v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.06748", "v1", "9342ca252eb8dbdec9f7563367023ef59162268fd606488afbbfe56f6cba2a32")

N = 120
print("Protocol (App. A, pp. 15-16)")
quote(doc, 15, "Event and revisit success are binary; the remaining perceptual and behavioral criteria use the three-level scale {0, 0.5, 1}.")
quote(doc, 16, "Subject Consistency compares the opening subject with the revisited subject")
quote(doc, 16, "Unless otherwise stated, three-level metrics are averaged over all 120 benchmark cases and reported as percentages.")


def attainable(v, step):
    """Is v (one decimal) a rounding of some k * step?"""
    k = round(v / step)
    return any(abs((k + d) * step - v) <= 0.05 + 1e-9 for d in (-1, 0, 1))


BIN, TRI = 100 / N, 100 / (2 * N)  # binary: k/120, three-level: k/240
COLS = [("Core", BIN), ("Revisit", BIN), ("Event", BIN), ("Causal", TRI), ("React.", TRI), ("Visual", TRI), ("Subj. Cons.", TRI)]

print("\nTable 1 (p. 7)")
t = page_text(doc, 7)
t = t[t.index("Subj. Cons. Bg. Cons. Motion") + len("Subj. Cons. Bg. Cons. Motion"):]
rows = re.findall(r"([A-Z][\w\-. ]*?(?: \([^)]*\))?) ((?:\d+\.\d ){7})", t)
bad = []
for name, vals in rows:
    vs = [float(x) for x in vals.split()]
    for (col, step), v in zip(COLS, vs):
        if not attainable(v, step):
            bad.append((name.strip(), col, v))
print(f"  rows parsed: {len(rows)}")

print("\nTable 2 (p. 8)")
quote(doc, 8, "Stage 1 + IAA 84.2 99.2 98.3 88.7 83.9")
for col, step, v in [("Causal", TRI, 88.7), ("React.", TRI, 83.9)]:
    if not attainable(v, step):
        bad.append(("Stage 1 + IAA (Table 2)", col, v))

print(f"\nValues that are not k/{N} (binary) or k/{2 * N} (three-level) after rounding to one decimal:")
for name, col, v in bad:
    k = v * 2 * N / 100
    print(f"  {name:35s} {col:11s} {v:5.1f}  (would need {k:.2f} of {2 * N} half-points; nearest {int(k)}/{2 * N} = {100 * int(k) / (2 * N):.2f}, {int(k) + 1}/{2 * N} = {100 * (int(k) + 1) / (2 * N):.2f})")

"""Reproduce the check on Interpreting Coding Agents Through Their Behavioral Trajectories, arXiv:2611.17440v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.17440", "v1", "e89b62397c67ca202743e053910309294940ef93a444679a0814e2a32a103b6b")
N = 500

print("Table 1 (p. 5): parser agreement with the six-model consensus on 500 actions")
quote(doc, 12, "achieves 82.4% agreement on primary operations (88.8% Macro-F1), 77.0% on target file roles, 68.8% on mutation types, and 96.6% on read modes")
quote(doc, 12, "the exact-match rate, which requires all four core fields to agree, is 77.5%")
t = page_text(doc, 5)
rows = {}
for name in ["Primary operation", "Target file role", "Mutation type", "Read mode",
             "Ordered operations", r"Exact match \(all 4 shared fields\)"]:
    c, a = re.search(name + r" (\d+\.\d)% (\d+\.\d)%", t).groups()
    rows[name.split(" \\(")[0]] = (float(c), float(a))


def counts(pct, n):
    """All integers k with round(100 k / n, 1) == pct."""
    return [k for k in range(n + 1) if round(100 * k / n, 1) == pct]


print("\n1. Agreement counts implied by the stated rates")
res = {}
for name, (c, a) in rows.items():
    n = counts(c, N)
    assert len(n) == 1, (name, n)
    n = n[0]
    k = counts(a, n)
    res[name] = (n, k)
    shown = f"{k[0]}/{n}" if k else f"none: nearest {(a * n / 100):.1f}/{n} is shown as " \
        f"{100 * int(a * n / 100) / n:.1f}% or {100 * (int(a * n / 100) + 1) / n:.1f}%"
    print(f"  {name:20s} consensus {c}% = {n}/500, agreement {a}% -> {shown}")

print("\n2. Exact match cannot exceed mutation-type agreement")
n_mut, (k_mut,) = res["Mutation type"]
n_ex, (k_ex,) = res["Exact match"]
outside = n_mut - n_ex
inside = (n_mut - k_mut) - outside
print(f"  Mutation type: {n_mut - k_mut} disagreements among {n_mut} resolved actions")
print(f"  At most {n_mut} - {n_ex} = {outside} of them can lie outside the {n_ex} actions resolved on all four fields")
print(f"  So at least {inside} of the {n_ex} disagree on mutation type,")
print(f"  and exact match is at most {n_ex - inside}/{n_ex} = {100 * (n_ex - inside) / n_ex:.1f}%; Table 1 gives {k_ex}/{n_ex} = 77.5%")

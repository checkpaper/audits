"""Reproduce the check on Module-Aware Optimization for Graph Neural Networks (GraphMuon), arXiv:2611.08379v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.08379", "v1", "4f08301a5245756f398d1f21b4a83c02ffe264453814370a49bd7adf7bf0ddc8")

print("Training budgets (Table 7, p. 22) versus epochs to target (Table 1, p. 8; Table 14, p. 28)")
quote(doc, 22, "Time-to-target is computed only within these benchmark budgets; runs that do not reach the target within the corresponding budget are marked as not reaching the target")
t7 = page_text(doc, 22)
budget = {m.group(1): int(m.group(2)) for m in re.finditer(
    r"(OGBN-ARXIV|OGBN-PRODUCTS|OGBN-MAG|QUESTIONS) (?:OGB official \[14\]|Platonov et al\. benchmark \[24\]) (\d+) epochs", t7)}
print("  Table 7 budgets:", budget)

t14 = page_text(doc, 28)
row = r"(ogbn-arxiv|ogbn-mag|ogbn-products|questions) (\w+\+*) (\d\.\d+) (\d+) / [\d.]+ (?:(\d+) / [\d.]+ [\d.]+|– –) (\d+) / [\d.]+ [\d.]+"
for m in re.finditer(row, t14):
    ds, arch, _, a, mu, g = m.groups()
    b = budget[ds.upper()]
    eps = {"AdamW": int(a), "Muon": int(mu) if mu else None, "GraphMuon": int(g)}
    over = [f"{k} {v}" for k, v in eps.items() if v and v > b]
    print(f"  {ds:13s} {arch:8s} budget {b:3d}: " + ", ".join(f"{k} {v}" for k, v in eps.items() if v)
          + (f"  <- over budget: {', '.join(over)}" if over else ""))

quote(doc, 8, "QUESTIONS GAT 0.1217 481 / 15.2 320 / 10.2 167 / 7.1 2.14×")

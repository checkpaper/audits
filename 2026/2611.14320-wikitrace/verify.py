"""Reproduce the check on WikiTrace (Don't Just Trust Your Memory), arXiv:2611.14320v1.

Run: python verify.py
"""
import collections
import csv
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, quote  # noqa: E402

doc = fetch("2611.14320", "v1", "0f434777c9a3220be87bbc4a5f0c9f952300a9ba55fdcf8788b37c3f525ba8cd")
COMMIT = "9ee357fbb95db9caae09808f3472a9fce6409c90"
results = download(
    f"https://raw.githubusercontent.com/yukyeongleee/wikitrace/{COMMIT}/tests/analysis/fixtures/paper_per_sample.csv",
    "wikitrace_paper_per_sample.csv",
    "231bf3c3bcf7fb702a44d6cb627360a463b96f473643895e77c085edfa619bc2",
)

print("Claims")
quote(doc, 1, "showing that it consistently outperforms existing memory approaches")
quote(doc, 2, "WikiTrace achieves the best performance on every suite")
quote(doc, 5, "WikiTrace (ours) 98.7±0.5 98.8±0.7 96.1±1.4 93.3±3.4 81.3±8.5 88.2±3.9 89.5±1.5 75.8±2.2 90.2±1.6")

print("\nReleased per-sample results (repo tests/analysis/fixtures/paper_per_sample.csv), mean over 3 trials, %")
scores = collections.defaultdict(list)
for row in csv.DictReader(open(results)):
    scores[(row["benchmark"], row["suite"], row["method"])].append(float(row["outcome"]))


def mean(benchmark, suite, method):
    values = scores[(benchmark, suite, method)]
    return 100 * sum(values) / len(values)


# RCI-traverse is WikiTrace: its suite means equal the WikiTrace row of Table 1.
# ScienceWorld is left out: Table 1 reports a graded score, the file stores pass or fail.
suites = [("alfworld", "valid-seen"), ("alfworld", "valid-unseen"), ("plancraft", "plancraft-seen"),
          ("plancraft", "plancraft-unseen"), ("tau3", "retail"), ("appworld", "test-normal"),
          ("appworld", "test-challenge")]
print(f"  {'suite':28} {'WikiTrace':>9} {'ACE':>6}")
for b, s in suites:
    w, a = mean(b, s, "RCI-traverse"), mean(b, s, "ace")
    flag = "  ACE higher" if a > w + 1e-9 else ("  tie" if abs(a - w) < 1e-9 else "")
    print(f"  {b + '/' + s:28} {w:9.1f} {a:6.1f}{flag}")
print("  ACE is in the released results for all suites but not in Table 1.")

"""Reproduce the check on EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades
of Satellite Imagery, arXiv:2611.12934v1.

Run: python verify.py
"""
import collections
import gzip
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, quote  # noqa: E402

doc = fetch("2611.12934", "v1", "cb8464bf8bcbdf3f8386ab44969431373a36f758ce8d0e936a9f7df954d01e5e")
COMMIT = "d4b724d76a909e01e3b7f406356dde0dbd34b4dc"
runs_path = download(
    f"https://github.com/ranranrannervous/EarthRecord/raw/{COMMIT}/results/runs.jsonl.gz",
    "earthrecord_d4b724d_runs.jsonl.gz",
    "2d61154838c4e2c18feae02603ce13cb4510e75237963b4b64aa121c57bdc471",
)

print("Paper")
quote(doc, 3, "every field accepts insufficient evidence.")
quote(doc, 17, "Claude Opus 5.5 4.2 12 11 0.0 35 11")
quote(doc, 17, "Runs per model that answer insufficient evidence, out of 219 recognition, 459 computable, and 36 insufficientevidence runs.")
quote(doc, 15, "Claude Opus 5.5 68.6 62.1 91.1 87.6 68.9 65.8 84.0 80.8 97.2 91.7")

print(f"\nReleased runs (results/runs.jsonl.gz, commit {COMMIT[:7]})")
runs = [json.loads(line) for line in gzip.open(runs_path, "rt")]
total, abstain = collections.Counter(), collections.Counter()
for r in runs:
    total[r["model"]] += 1
    if "insufficient_evidence" in json.dumps(r["answer"]):
        abstain[r["model"]] += 1
print(f"  {len(runs)} runs; runs whose answer contains insufficient_evidence, per model:")
for m in sorted(total):
    print(f"    {m:24s} {abstain[m]:5d} of {total[m]}")

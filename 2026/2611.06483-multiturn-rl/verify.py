"""Reproduce the checks on "What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?", arXiv:2611.06483v1.

Run: python verify.py
"""
import pathlib
import re
import sys
import tarfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, quote  # noqa: E402

pdf = fetch("2611.06483", "v1", "246a6568987e4c3b37fc2f029977202b5b6404eb463d3a6dac62131c8518010d")
src = download("https://arxiv.org/e-print/2611.06483v1", "2611.06483v1-source.tar.gz",
               "b4a08acddcbed390991f415206b3de4edd29c9aa58247ad9d4d18b026cf31d1b")
with tarfile.open(src) as tar:
    tex = tar.extractfile("iclr2027_conference.tex").read().decode("utf-8").splitlines()

print("LaTeX source of v1 (iclr2027_conference.tex): figure environments for Figures 2, 3 and 6")
for label, page, caption in [
    ("fig:passk", 3, "Figure 2: Pass@K across sampling breadth."),
    ("fig:passt", 4, "Figure 3: Pass@T at fixed k=8."),
    ("fig:depth", 6, "Figure 6: Action quality versus normalized trajectory depth"),
]:
    end = next(i for i, line in enumerate(tex) if line.strip() == rf"\label{{{label}}}")
    start = max(i for i in range(end) if tex[i].startswith(r"\begin{figure}"))
    print(f"\n  lines {start + 1}-{end + 1}:")
    for i in range(start, end + 1):
        print(f"  {i + 1:4d}  {tex[i]}")
    block = "\n".join(tex[start:end + 1])
    if "PREVIEW FIXTURE" not in block or "replace with measured results" not in block:
        sys.exit(f"{label}: comment not found")
    if not any(re.match(r"\s*\\includegraphics", line) for line in tex[start:end + 1]):
        sys.exit(f"{label}: figure is not included")
    quote(pdf, page, caption)

print("\nAll three figures are compiled into the v1 PDF, and each figure environment carries")
print("the comment that its values are synthetic design previews to be replaced with measured results.")

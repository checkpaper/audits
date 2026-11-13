"""Reproduce the check on Switch-SWE, arXiv:2611.02017v1.

Run: python verify.py
"""
import io
import pathlib
import re
import sys
import tarfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, page_text, quote  # noqa: E402

doc = fetch("2611.02017", "v1", "1671456fd3dd60a5aa5f38559b51477141736c5fd2b63a1cafd9d9131bb9787c")
src = download("https://arxiv.org/e-print/2611.02017v1", "2611.02017v1-src.tgz",
               "6129a68a4a30cbbf9bd66dd47348fab25b82a1b92a1ad8fb7a4c1d69a0a97adc")

print("Section 4.3 (p. 8): switched versus uninterrupted sessions")
quote(doc, 8, "Full switched sessions consume 4.5-11.1 times as many tokens as uninterrupted sessions, "
              "compared with 2.4-4.3 times as many model calls.")


def ratios(rows):
    tok = [r[1] / r[0] for r in rows]
    calls = [r[4] / r[3] for r in rows]
    return f"tokens {min(tok):.2f}-{max(tok):.2f}x, model calls {min(calls):.2f}-{max(calls):.2f}x"


# Printed Table 2 (p. 7): per model, tokens Unint/All/Focus, model calls Unint/All/Focus, tool calls Unint/All/Focus.
text = page_text(doc, 7)
table = text[text.index("Model Harness Tokens"):text.index("4.1 FOCUS-TASK RESOLUTION")]
printed = [[float(x) for x in m] for m in re.findall(r"(\d+\.\d{3}) (\d+\.\d{3}) \d+\.\d{3} (\d+\.\d) (\d+\.\d) (\d+\.\d)", table)]
printed = [[r[0], r[1], 0, r[2], r[3]] for r in printed]
if len(printed) != 7:
    sys.exit(f"expected 7 rows in the printed Table 2, found {len(printed)}")
print(f"  Printed Table 2 (p. 7), 7 configurations: {ratios(printed)}")

# The LaTeX source keeps an earlier Table 2, commented out, in sec/4_experiment.tex.
with tarfile.open(src) as tar:
    tex = tar.extractfile("sec/4_experiment.tex").read().decode()
block = tex[tex.index("% \\label{tab:resumption_resources}"):]
old = [[float(x) for x in m] for m in
       re.findall(r"^% & ([\d.]+) & ([\d.]+) & [\d.]+\s*\n% & ([\d.]+) & ([\d.]+) & [\d.]+", block, re.M)[:7]]
old = [[r[0], r[1], 0, r[2], r[3]] for r in old]
print(f"  Commented-out Table 2 in sec/4_experiment.tex: {ratios(old)}")

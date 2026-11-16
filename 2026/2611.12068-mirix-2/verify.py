"""Reproduce the check on MIRIX-2.0, arXiv:2611.12068v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.12068", "v1", "f37c020d5a668b5f790c767b16e63e3ae991502870dbf8e86333a2a1c934617a")

print("LongMemEval-S, Table 7: one run, majority-of-3 judge, 300 questions")
quote(doc, 10, "LoCoMo and LongMemEval-S use a gpt-4o-mini judge with majority-of-3 voting")
quote(doc, 10, "with mean and standard deviation over three runs")  # interactive agents only
quote(doc, 27, "Table 7 LongMemEval-S accuracy (%) on the evaluated 300 questions")
text = page_text(doc, 27)
table = text[text.index("Table 7"):text.index("Table 8")]
rows = re.findall(r"([A-Za-z][\w\-\.\(\), +]*?) (\d+\.\d)(?= |$)", table.split("Accuracy", 1)[1])


def fits(x, n):
    return any(abs(round(k / n * 100, 1) - x) < 1e-9 for k in range(n + 1))


for name, v in rows:
    x = float(v)
    near = sorted({round(k / 300 * 100, 2) for k in (int(x * 3), int(x * 3) + 1)})
    print(f"  {name.strip():32s} {x:5.1f}  k/300: {'yes' if fits(x, 300) else 'no, nearest ' + str(near)}"
          f"   k/900: {'yes' if fits(x, 900) else 'no'}")
print("  Abstract: 72.6% on LongMemEval-S, leading the strongest baseline by 14.3 points")
quote(doc, 1, "72.6% on LongMemEval-S, where it leads the strongest baseline by 14.3 points")

"""Reproduce the check on Termination Lag, arXiv:2611.14960v1.

Run: python verify.py
"""
import io
import pathlib
import sys
import tarfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, quote  # noqa: E402

doc = fetch("2611.14960", "v1", "2c7586e6b2354008fc319c121d4a1bbf810f07a544d09432a0acf3480ea80f26")

print("Table 1 caption (p. 4)")
quote(doc, 4, "All rows below Solved are medians over solved runs")
quote(doc, 4, "Context growth (%) +30 +28 +78 +55")

red = [s["text"].strip() for b in doc[3].get_text("dict")["blocks"] for l in b.get("lines", [])
       for s in l["spans"] if s["color"] == 0xFF0000]
print(f"\n  red text on p. 4: {red}")
if red != ["+30", "+28", "+78", "+55"]:
    sys.exit("unexpected red spans")

src = download("https://arxiv.org/e-print/2611.14960v1", "2611.14960v1-src.tgz",
               "2f5fab9ad1fa1c397d63c3e7863ca2c656ad38e05a5f8e330813d226fb5a0f4b")
with tarfile.open(fileobj=io.BytesIO(src.read_bytes())) as tar:
    tex = tar.extractfile("arxiv.tex").read().decode()
line = next(l for l in tex.splitlines() if l.startswith("Context growth"))
print(f"\narXiv source, arxiv.tex:\n  {line}")
if "TODO: these are MEANS; replace with medians" not in line:
    sys.exit("TODO comment not found")

code = download("https://raw.githubusercontent.com/musacim/termination-lag/"
                "eafa4199b3d9abdf0b4f8e5d0365a85215d3ec00/code/analysis/ctx_growth.py", "termination-lag-ctx_growth.py",
                "b1fc8d002471ccfa78519d909364d293d392b909825f9761da8c7573365ea5b9").read_text()
print("\nReleased code/analysis/ctx_growth.py (commit eafa419):")
for want in ["context at the end = prompt + output tokens of the run's last call",
             "Prints median and p90 per column.",
             "--all: every solved run (final patch resolves, has F), as the paper's main table; default: tab:post tasks."]:
    if want not in code:
        sys.exit(f"not found in ctx_growth.py: {want}")
    print(f'  "{want}"')

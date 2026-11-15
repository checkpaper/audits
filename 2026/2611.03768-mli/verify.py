"""Reproduce the checks on Multi-layer Indexer (MLI), arXiv:2611.03768v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.03768", "v1", "1d9d589f03f3e6f502bf77fc340091ae73b318ac6a9853c08734e62ca89aa52b")

print("Equal-retention speed gaps: Appendix J versus Table 9")
quote(doc, 18, "the equal-retention gaps carry 95% intervals of about ±0.1 percentage point (DeepSeek-V3.2 at 128K: 1/4 +4.70 ± 0.11, 1/8 +2.36 ± 0.14; GLM-5 at 195K: 1/4 +4.12 ± 0.06, 1/8 +2.61 ± 0.06)")
quote(doc, 18, "by up to 0.5 and 0.2 percentage point on the equal-retention gaps")
quote(doc, 6, "GLM-5 uses the deferred-stream realization")
cells = [  # model, retention, IndexCache decode, IndexCache+MLI decode, Appendix J gap
    ("DeepSeek-V3.2, 128K", "1/4", "IndexCache 1/4 +22.7", "IndexCache+MLI 1/4 +32.3", 4.70),
    ("DeepSeek-V3.2, 128K", "1/8", "IndexCache 1/8 +28.0", "IndexCache+MLI 1/8 +33.7", 2.36),
    ("GLM-5, 195K", "1/4", "IndexCache 1/4 +17.7", "IndexCache+MLI 1/4 +23.7", 4.12),
    ("GLM-5, 195K", "1/8", "IndexCache 1/8 +21.3", "IndexCache+MLI 1/8 +25.0", 2.61),
]
for model, r, ic, mli, appj in cells:
    quote(doc, 17, ic)
    quote(doc, 17, mli)
    gap = float(mli.split("+")[-1]) - float(ic.split("+")[-1])
    print(f"  {model} {r}: Table 9 gap {gap:.1f} pp, Appendix J {appj:.2f} pp, difference {gap - appj:.2f} pp")
print("  Appendix J bounds the between-cell difference on these gaps at 0.5 pp (DeepSeek) and 0.2 pp (GLM).")

"""Reproduce the check on PGPO (Prototype-Guided Progressive Obfuscation for Privacy-Preserving LLM-Enhanced Recommendation), arXiv:2611.23236v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.23236", "v1", "431c56c7420b56df5832eff614d66aebc0be8d48ceff7e1e79b8deca07573b0e")

print("Sec. 5.2 (iii) (p. 8)")
quote(doc, 8, "all obfuscation methods cut attack suc")

print("\nTable 4 (p. 8): EM, Precision, Recall, F1, Jaccard on MovieLens-1M then Amazon-Book")
rows = {
    "Description": "Description 0.0641 0.2413 0.3638 0.2720 0.2116 0.0988 0.1829 0.1836 0.1832 0.1551",
    "InferDPT": "InferDPT 0.0309 0.0676 0.0848 0.0703 0.0583 0.0480 0.0950 0.0955 0.0952 0.0795",
    "Text2Text": "Text2Text 0.0276 0.0593 0.0808 0.0646 0.0523 0.0324 0.0727 0.0730 0.0728 0.0594",
    "SanText+": "SanText+ 0.0276 0.0839 0.1252 0.0941 0.0711 0.0226 0.0599 0.0605 0.0601 0.0477",
    "TOF": "TOF 0.0301 0.0672 0.0912 0.0722 0.0586 0.0384 0.0887 0.0896 0.0890 0.0722",
    "Ours": "Ours 0.0309 0.0662 0.0913 0.0721 0.0593 0.0314 0.0925 0.0933 0.0928 0.0724",
}
for s in rows.values():
    quote(doc, 8, s)
vals = {k: [float(x) for x in v.split()[1:]] for k, v in rows.items()}
cols = [f"{d} {m}" for d in ("ML-1M", "Amazon") for m in ("EM", "P", "R", "F1", "J")]

base = vals["Description"]
for name in ("InferDPT", "Text2Text", "SanText+", "TOF", "Ours"):
    for j, c in enumerate(cols):
        cut = (1 - vals[name][j] / base[j]) * 100
        if cut <= 50:
            print(f"  {name:9s} {c:10s} {vals[name][j]:.4f} vs {base[j]:.4f}: cut {cut:.1f}%")
print("Seven Amazon-Book cells are cut by less than 50%, three of them for PGPO itself.")

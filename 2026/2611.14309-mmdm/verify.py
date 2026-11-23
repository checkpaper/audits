"""Reproduce the checks on MMDM, arXiv:2611.14309v1.

Run: python verify.py
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from common import fetch, page_text, quote  # noqa: E402

doc = fetch("2611.14309", "v1", "0fa6ef2df054a8817679c96be6d12ce87ee7950ea0b2c34ce2f69f4c0f94787c")

# selection.json from the Hugging Face dataset shenjunhao/mmdm at commit 016dacdf (MIT licence).
# Source: https://huggingface.co/datasets/shenjunhao/mmdm/resolve/016dacdfd56c47128990539cc3c106a4a0b794ce/selection.json
SEL_SHA = "2cf1a99117ef7d692c3f719cb778b0ee337799db8057ef996be3f2a1165f510f"
raw = (HERE / "selection.json").read_bytes()
if hashlib.sha256(raw).hexdigest() != SEL_SHA:
    sys.exit("selection.json differs from the file checked")
sel = json.loads(raw)
r = sel["recipe"]

print("1. Final filtering step recorded in the released selection.json")
print(f"  model: {sel['model']}")
print(f"  rule: {r['decision']}")
print(f"  entropy: {r['entropy']}")
print(f"  pool {r['input_rows']}, removed {sel['removed']} (correct {r['removed_correct']}, "
      f"incorrect {r['removed_incorrect']}), retained {sel['retained_from_pool']}")
before = r["original_correct"] / r["input_rows"]
after = (r["original_correct"] - r["removed_correct"]) / r["retained_rows"]
print(f"  {sel['model']} accuracy on the pool: {before:.2%} before, {after:.2%} after the filter")
print(f"  final release: {sel['retained_from_pool']} retained + {sel['preserved_outside_pool']} outside the pool "
      f"= {sel['retained_from_pool'] + sel['preserved_outside_pool']} (paper: 5,448)")
quote(doc, 1, "a benchmark of 5,448 high-quality questions across 16 task categories")
quote(doc, 5, "Fivemodel majority screening is followed by independent human expert review of borderline cases")
for word in ["entropy", "Jev 1.13"]:
    pages = [p for p in range(1, len(doc) + 1) if word.lower() in page_text(doc, p).lower()]
    print(f'  "{word}" in the paper: {"pages " + str(pages) if pages else "not found on any of the " + str(len(doc)) + " pages"}')
quote(doc, 6, "Closed-source decision models Jev 1.14.0 67.17")

print("\n2. OpenJev 4B")
quote(doc, 1, "Perplexity V1.2 Jev 1.14.0 Microsoft Decision-1 Intern-Decision 4B OpenJev 4B Figure 1: MMDM capability profiles for five representative decision models")
quote(doc, 2, "OpenJev learns a shared decision head over request-defined options, using supervised learning followed by reinforcement learning (Shen, 2026)")
quote(doc, 1, "Junhao Shen1")
print("  The model is hosted at huggingface.co/shenjunhao/OpenJev-4B, the account that hosts the MMDM dataset.")

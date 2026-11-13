"""Reproduce the checks on Video-Coder, arXiv:2611.09894v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.09894", "v1", "1111598b2efe60d0fcf8d2eeb334bee2af877158dfa3e1495c314756ce202100")

print("1. Section 4.2 (p. 7): the OmniWeaving gain")
quote(doc, 7, "it improves OmniWeaving from 0.48 to 0.51 (an increase of 16.28 points)")
print(f"  0.51 - 0.48 = {0.51 - 0.48:.2f} absolute, {(0.51 - 0.48) / 0.48:.2%} relative")

print("\n2. Table 1 (p. 7): two baseline rows")
quote(doc, 7, "LTX-Video-2B [61] 0.51 0.58 0.48 0.45 0.51 Video-CoCo [36] 0.51 0.58 0.48 0.45 0.51")
print("  The LTX-Video-2B and Video-CoCo rows are identical in all five columns.")

print("\n3. Dataset sizes")
for page, phrase in ((1, "Video-Coder-SFT-6k and Video-Coder-RL-2k"),
                     (5, "we perform supervised finetuning on Video-Coder-SFT-6k"),
                     (6, "We first perform supervised fine-tuning on Video-Coder-SFT-10k, and then further conduct "
                         "agentic RL training on Video-Coder-RL-4k.")):
    quote(doc, page, phrase)

"""Reproduce the check on CaPtain, arXiv:2610.40799v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.40799", "v1", "3a046c9198a2211285baa0badd61be595916f869292380e86b1b11dcc75b5410")

print("Are the evaluation perturbations absent from training?")
quote(doc, 8, "We train only on the 40 original LIBERO tasks [44] and evaluate on LIBERO and three perturbation suites "
              "built on them, whose perturbations never appear in training.")
quote(doc, 7, "mostly wide-layout scenes with randomized lighting, camera pose and materials, plus official initial states")
quote(doc, 22, "5,600 wide-layout starts with light, camera and material perturbations")
quote(doc, 24, "randomize lighting, camera pose and materials during RL")
print("  RL training randomizes lighting, camera pose and materials, which are also perturbation types in the evaluation suites.")

"""Reproduce the checks on HDM (The Value of Thinking), arXiv:2611.16961v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.16961", "v1", "936847cd436fa6e20fec305f9d52e6ae71be57981095d7644ca4eab0d32a3f7e")

print("JevBench P50: routed HDM-4B versus fast-only HDM-4B (Table 2)")
quote(doc, 1, "at a median 0.179 s against 0.652 (−72.5%)")
quote(doc, 2, "Routing occurs once: the model either returns the cached fast answer or decodes autoregressively with the same backbone")
quote(doc, 3, "reads representations the fast pass has already computed, so the choice costs no forward pass and no token")
quote(doc, 6, "P50 the median wall-clock seconds per item")
quote(doc, 6, "HDM-4B, fast only 0% 0.762 0.226")
quote(doc, 6, "HDM-4B, routed λ = 0 30% 0.857 0.179")
fast, routed = 0.226, 0.179
print("  Every routed item runs the fast pass; 70% stop there and 30% also decode.")
print("  So each item's routed time is at least its fast-only time, and so is the median.")
print(f"  Table 2: routed P50 {routed} s is {(fast - routed) / fast:.1%} below fast-only P50 {fast} s.")
print(f"  A routed P50 of at least {fast} s would put the reduction against Jev's 0.652 s at most {(0.652 - fast) / 0.652:.1%}, against the 72.5% claimed.")

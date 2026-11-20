"""Reproduce the check on Prompt2Echo (P2Echo), arXiv:2611.13425v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.13425", "v1", "2987dafecd615bc5246506aa06a952c75a6e481a81609ffa0c3077eca9c1e647")

print("Inference-efficiency text (p. 7) and Discussion (p. 8)")
quote(doc, 7, "1.51× faster than CENet and 4.28–159.36× faster than the evaluated promptable methods")
quote(doc, 8, "4–160× more efficient than the promptable baselines")
print("\nTable VII latencies, s/image (p. 9)")
rows = {"SAMUS": 0.06620, "SAM3 (Zero-shot)": 0.19694, "SAM3 (Fine-tuned)": 0.08203,
        "MedCLIP-SAMv2": 2.46376, "Grounding DINO-US-SAM": 2.59870, "EchoONE": 0.08649}
for name, v in rows.items():
    quote(doc, 9, f"{name} {v:.5f}")
quote(doc, 9, "P2Echo (Ours) 0.01546")
quote(doc, 9, "CENet 0.02328")
ours = 0.01546
print(f"\n  CENet: {0.02328 / ours:.2f}x")
for name, v in rows.items():
    print(f"  {name}: {v / ours:.2f}x")
print("  The largest promptable ratio is Grounding DINO-US-SAM at 168.09x; 159.36x is MedCLIP-SAMv2.")

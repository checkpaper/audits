"""Reproduce the check on KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware, arXiv:2611.29590v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.29590", "v1", "5c2f85f5ea6702abd09d7d94ccd2592757b77b7b486286ff7fe5ff9b109baf55")

print("Claim (App. E.1, p. 24)")
quote(doc, 24, "The prefill gain persists across prompt lengths and micro-batch sizes (Table 19).")

print("\nTable 19 (p. 24): prefill speedup at 16 threads, Qwen3.5-4B / Llama-3.1-8B")
quote(doc, 24, "Prompt length 512 1.298 1.393 2048 1.281 1.322 4096 1.260 1.255 8192 1.226 1.184")
quote(doc, 24, "Micro-batch size 1 1.053 1.090 2 1.270 1.598 8 1.164 1.479 64 1.061 0.989 512 1.298 1.397")
mb = {1: (1.053, 1.090), 2: (1.270, 1.598), 8: (1.164, 1.479), 64: (1.061, 0.989), 512: (1.298, 1.397)}
for size, (q, l) in mb.items():
    print(f"  micro-batch {size:3d}: Qwen {q:.3f}  Llama {l:.3f}{'   <- below 1' if l < 1 else ''}")

print("\nSame configuration (16 threads, 512-token prompt, micro-batch 512) in three places")
quote(doc, 9, "16 1.298 1.048 1.391 1.102")
print("  Qwen3.5-4B:   Table 6 1.298, Table 19 prompt 512 1.298, Table 19 micro-batch 512 1.298")
print("  Llama-3.1-8B: Table 6 1.391, Table 19 prompt 512 1.393, Table 19 micro-batch 512 1.397")

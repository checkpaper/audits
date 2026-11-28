# KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware (arXiv:2611.29590): consistency check

App. E.1 says the prefill gain persists across prompt lengths and micro-batch sizes, but Table 19 gives Llama-3.1-8B a prefill speedup of 0.989 at micro-batch 64, a slowdown. The same 16-thread configuration also has three slightly different Llama values across Tables 6 and 19.

## Paper

- Title: KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware
- arXiv: [2611.29590v1](https://arxiv.org/abs/2611.29590v1) (the version checked, sha256 `5c2f85f5…af55`)
- Hugging Face: [papers/2611.29590](https://huggingface.co/papers/2611.29590)
- Code: [cmu-l3/kernel-shift](https://github.com/cmu-l3/kernel-shift)
- CheckPaper report: [checkpaper.app/r/72ngeuzu9v](https://checkpaper.app/r/72ngeuzu9v)

## Findings

1. **Micro-batch 64.** App. E.1 (p. 24): "The prefill gain persists across prompt lengths and micro-batch sizes (Table 19)." In Table 19 (16 threads), Llama-3.1-8B prefill speedup by micro-batch size is 1.090 (1), 1.598 (2), 1.479 (8), 0.989 (64) and 1.397 (512). At 64 the agent kernels are slower than the original llama.cpp.
2. **One configuration, three values.** For Qwen3.5-4B, 16 threads appears as 1.298 in Table 6 and in both the prompt-512 and micro-batch-512 rows of Table 19. For Llama-3.1-8B the same three cells read 1.391, 1.393 and 1.397.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.29590v1, checks its hash, and quotes the claim and the Table 6 and Table 19 rows.

## Status

[Asked the authors](https://github.com/cmu-l3/kernel-shift/issues/1) on 2026-11-29.

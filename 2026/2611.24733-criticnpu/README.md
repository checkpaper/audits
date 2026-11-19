# Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration (arXiv:2611.24733): consistency checks

App. E.1 gives CMA-ES a decode win rate of 0–3 of 16, which is its prefill row in Table 1; App. E.3 says all base LLMs stay within 5%, while Table 12 has a −23% TPOT change.

## Paper

- Title: Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration
- arXiv: [2611.24733v1](https://arxiv.org/abs/2611.24733v1) (the version checked, sha256 `1ffdc09a…516d`)
- Hugging Face: [papers/2611.24733](https://huggingface.co/papers/2611.24733)
- Code: [bruno686/CriticNPU](https://github.com/bruno686/CriticNPU)
- CheckPaper report: [checkpaper.app/r/z4tmankc9m](https://checkpaper.app/r/z4tmankc9m)

## Findings

1. **CMA-ES decode win rate.** The App. E.1 caption (p. 23) explains CMA-ES's fast decode convergence as a local-minimum artefact because "its decode win rate in Table 1 is 0–3 of 16". In Table 1 (p. 7) CMA-ES wins 0, 3, 3, 2, 0, 0 of 16 on prefill but 16, 16, 16, 16, 7, 10 of 16 on decode (81 of 96). The quoted range is the prefill row, and the decode row does not support the explanation.
2. **Base-LLM generalization.** App. E.3 (p. 24) says "Final latencies are within 5% of the default on every workload; the largest single deviation is GPT-4o on Llama3-8B prefill (+2.1% TTFT)". In Table 12 (p. 28), Llama2-13B TPOT goes from 18.29 ms with the default GPT-5.4-mini to 14.07 ms with both GPT-4o and GPT-4o-mini (−23%, printed in the table), and DSv2-236B TTFT changes by +2.7% and +2.5%, both larger than +2.1%.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.24733v1, checks its hash, quotes Table 1, Table 12 and the two appendix passages, and recomputes the relative changes.

## Status

Not yet asked.

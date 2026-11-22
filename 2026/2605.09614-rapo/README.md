# RAPO: Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning (arXiv:2605.09614): consistency check

App. G.3 gives RAPO's greedy–stochastic gap as 11.46, but Table 10 gives 43.01 − 31.41 = 11.60. Table 12 (DAPO group, said to be evaluated at temperature 0.6) repeats the Base row of Table 1 (temperature 1.0) exactly.

## Paper

- Title: Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning
- arXiv: [2605.09614v1](https://arxiv.org/abs/2605.09614v1) (the version checked, sha256 `b4399281…70c1`)
- Hugging Face: [papers/2605.09614](https://huggingface.co/papers/2605.09614)
- Code: [coder-gx/RAPO](https://github.com/coder-gx/RAPO)
- CheckPaper report: [checkpaper.app/r/x83ssvdsdt](https://checkpaper.app/r/x83ssvdsdt)

## Findings

1. **Greedy–stochastic gap (App. G.3, p. 32).** "the greedy–stochastic gap is smaller for RAPO, 11.46, than for GRPO, 12.92". Table 10 gives RAPO 31.41 (greedy) and 43.01 (temperature 1), a gap of 11.60. The GRPO gap (40.79 − 27.87 = 12.92) matches. The Base model's gap is 37.16 − 27.24 = 9.92, the smallest of the three.
2. **Base row in Table 12 (App. H.2, p. 33).** The text says the DAPO group is evaluated as in the main experiments "except that the temperature is set to 0.6", while the main evaluation uses temperature 1.0 (App. C, p. 29). The Base row of Table 12 (41.74 / 50.21 / 38.34 / 62.28 / 37.59 / 67.20, avg 49.56) is identical to the Base row of Table 1. Either the Base model was not re-evaluated at 0.6, or the stated temperature does not apply to that row.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2605.09614v1, checks its hash, quotes Table 10, App. G.3, Table 1 and Table 12, and recomputes the gaps.

## Status

[Asked the authors](https://github.com/coder-gx/RAPO/issues/1) on 2026-11-23.

# WorldRuler: Interactive World Modeling under Configurable Rules (arXiv:2611.24869): Table 1 check

The Habitat Full Completion Rates in Table 1 cannot be proportions over at most 300 test tasks with one denominator per method, as Sec. 4.2 and 4.3 describe.

## Paper

- Title: WorldRuler: Interactive World Modeling under Configurable Rules
- arXiv: [2611.24869v1](https://arxiv.org/abs/2611.24869v1) (the version checked, sha256 `a7d7d4d7…7821`)
- Hugging Face: [papers/2611.24869](https://huggingface.co/papers/2611.24869)
- Code: [AlayaLab/WorldRuler](https://github.com/AlayaLab/WorldRuler)
- CheckPaper report: [checkpaper.app/r/7uxsu7zbmu](https://checkpaper.app/r/7uxsu7zbmu)

## Findings

1. **Habitat FCR (Table 1, p. 11; Sec. 4.2, p. 8; Sec. 4.3, p. 10).** The test split has 300 pairs, and uncertain judgments stay in the denominators. A rate over n tasks must be k/n. No n of at most 300 produces all three FCR components (Stages, Order, Goal) of any Habitat row, and no n of at most 3,000 produces all twelve. CWM Order 12.48 alone needs at least 505 tasks. Averaging over runs or per video would explain this, but the paper describes neither.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.24869v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

[Asked the authors](https://github.com/AlayaLab/WorldRuler/issues/1) on 2026-11-23.

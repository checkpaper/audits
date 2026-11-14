# Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents (arXiv:2608.22237): consistency checks

The NanoBot rows of Table 1 do not match any of the 30 NanoBot settings in Figure 6, and the workload behind them is not stated.

## Paper

- Title: Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents
- arXiv: [2608.22237v2](https://arxiv.org/abs/2608.22237v2) (the version checked, sha256 `bba857c4…3f96`)
- Hugging Face: [papers/2608.22237](https://huggingface.co/papers/2608.22237)
- Code: [Liuzedooong/SparseReading](https://github.com/Liuzedooong/SparseReading)
- CheckPaper report: [checkpaper.app/r/xmwemamdzb](https://checkpaper.app/r/xmwemamdzb)

## Findings

1. **DeepSeek-Flash.** Table 1 (p. 7) gives 22.4% token reduction and 25.6% time saving on NanoBot. In Figure 6 (p. 6), DeepSeek-Flash's five scenarios range from 40% to 87% for tokens and 33% to 76% for time, so Table 1 is below every cell and cannot be their average.
2. **DeepSeek-Pro.** Table 1 gives a score change of −0.015. All five DeepSeek-Pro score deltas in Figure 6 are zero or positive (0, +27, +11, +8, +3), and Section 6.2 says the only regression is GLM-5.1 on AI for Science.
3. **Workload.** The Table 1 caption says only "End-to-end SparseRead results across three agent frameworks and six models".

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2608.22237v2, checks its hash, finds the Figure 6 bar labels and the Table 1 rows, and compares them model by model.

## Status

Explained. The authors said on 2026-11-14 that Table 1 aggregates five scenarios from the v1 evaluation, while Figure 6 was updated with the revised v2 suite, so the two are not directly comparable; they will make this clearer in the next revision. Asked in [the SparseReading repository](https://github.com/Liuzedooong/SparseReading/issues/1).

## Author response

2026-11-14, Liuzedooong (repository owner), in [the issue](https://github.com/Liuzedooong/SparseReading/issues/1):

> Thanks for the careful check! Table 1 aggregates results across five scenarios from our earlier evaluation (v1), including the native-fit scenario, where sparsity is low and compression is less effective. Figure 6 was updated with the revised evaluation suite in v2, so the two aren't directly comparable. We'll make this clearer in the next revision!

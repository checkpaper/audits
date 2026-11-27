# Playfulness as Feedback for Agentic Game Development (arXiv:2611.33457): consistency check

The 15-game Refinement-versus-Evolution table repeats the 10-game evolution table cell for cell, one GameASG-Bench success rate does not fit 47 tasks, and the Play2Code Overall score does not follow from its sub-scores.

## Paper

- Title: Playfulness as Feedback for Agentic Game Development
- arXiv: [2611.33457v1](https://arxiv.org/abs/2611.33457v1) (the version checked, sha256 `11d7e909…203a`)
- Hugging Face: [papers/2611.33457](https://huggingface.co/papers/2611.33457)
- Code: [showlab/Play2Evolve](https://github.com/showlab/Play2Evolve)
- CheckPaper report: [checkpaper.app/r/6j3bu6amat](https://checkpaper.app/r/6j3bu6amat)

## Findings

1. **Table 8 versus Table 4.** Table 8 (p. 18) is described three times as a 15-game study. Its V0, V1 and V1 + Evolution (V2) rows are identical in all 15 cells to the V0, V1 and V2 rows of Table 4 (p. 8), the 10-game successive-evolution study (e.g. V0 66.25 / 53.46 / 61.80 / 42.33 / 52.74). Means over 15 and over 10 games would not normally agree to two decimals in every cell.
2. **35.7% on 47 tasks (Table 2, p. 7).** GameASG-Bench has 47 tasks (p. 7 and App. J). V1 and V2 at 57.4% fit 27/47, but V0 at 35.7% fits no k/47; the nearest values are 16/47 = 34.04% and 17/47 = 36.17%.
3. **Play2Code Overall (Table 1, p. 7).** With the weights 0.15 / 0.35 / 0.15 / 0.35 for M / D / V / A stated on p. 18, the V0, V1 and V2 rows reproduce within 0.02. Play2Code (69.84 / 50.07 / 51.95 / 51.77) gives 53.91, not the printed 52.46.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.33457v1, checks its hash, quotes the tables and recomputes the values above.

## Status

[Asked the authors](https://github.com/showlab/Play2Evolve/issues/2) on 2026-11-27.

## Author response

From a collaborator (maobenz), 2026-11-27 10:26 UTC:

> Hi, thanks for flagging these potential inconsistencies and for sharing the checking tool. We'll carefully verify the reported numbers and evaluation settings, and clarify or correct the paper as needed.

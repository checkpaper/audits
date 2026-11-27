# DominoBench (arXiv:2611.20385): consistency check

In the DominoBench-38 leaderboard (Table S4), 11 percentages cannot be a whole number of the stated 38 items or 19 pairs, and every one of them is a multiple of 10.

## Paper

- Title: DominoBench: Evaluating Multi-Step Physical Reasoning from Still Images
- arXiv: [2611.20385v2](https://arxiv.org/abs/2611.20385v2) (the version checked, sha256 `b2ef32b1…99ea`; v1 has the same table)
- CheckPaper report: [checkpaper.app/r/c5mhsbkp58](https://checkpaper.app/r/c5mhsbkp58)

## Findings

1. **Unattainable round values.** Table S4 (p. 15) covers DominoBench-38, 38 items in 19 twin pairs, and lists n = 38 for every model. Exact and deciding-person accuracy are therefore k/38 (…, 58, 61, …, 89, 92, …) and both-twins accuracy is k/19 (5, 11, 16, …). Eleven cells fall outside these sets: Claude Opus 5.5 and Qwen3.8-27B deciding-person H3 = 90 (possible: 89 or 92); Claude Opus 4.1 exact H3 = 60 (58 or 61); Gemma 4 31B exact H3 = 40 (39 or 42); Mistral-Small-3.2-24B and Qwen3-VL-30B-A3B exact H0 = 10 (8 or 11); and both-twins = 10 for five models (5 or 11). All other cells fit. The same values appear in Table S6 for the models listed there.

These are questions for the author, not conclusions: rounding to the nearest 10 by hand, or a different effective n for some runs, would explain the pattern, but the table does not mention either.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.20385v2, checks its hash, parses Table S4 and tests each percentage against k/38 or k/19.

## Status

Emailed the author on 2026-11-28 (address from p. 1).

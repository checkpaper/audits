# Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling (arXiv:2611.08237): consistency checks

The headline board includes the tennis task that the text says is kept out of headline rankings, the MULTI-BO column does not follow from Table 6 and Eq. (2), and the text puts a 0.06 pp gap at about 1.5 pp.

## Paper

- Title: Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling
- arXiv: [2611.08237v1](https://arxiv.org/abs/2611.08237v1) (the version checked, sha256 `6e9a9bfe…ff55`)
- Hugging Face: [papers/2611.08237](https://huggingface.co/papers/2611.08237)
- Code: [wxj630/terminal-bench-math-modeling](https://github.com/wxj630/terminal-bench-math-modeling)
- CheckPaper report: [checkpaper.app/r/dneefqqs7y](https://checkpaper.app/r/dneefqqs7y)

## Findings

1. **Tennis in the headline board.** Section 3.2 (p. 6) and the conclusion (p. 10) say literature-split tasks such as mcm-2024-c-tennis are excluded from any headline ranking. Table 6 (p. 16) says each column mean equals the main-table O-EVAL, and those means are over all 18 tasks including tennis (64.58, 63.12, 59.74, 59.79 against Table 2's 64.58, 63.11, 59.75, 59.81). Without tennis they are 66.24, 64.69, 62.72 and 62.78.
2. **GPT-5.5 versus Flash.** Section 4.2 (p. 7) speaks of a ∼1.5 pp separation between the two leaders and between GPT-5.5 and Flash. The leaders differ by 1.47 pp; GPT-5.5 (59.75) and Flash (59.81) differ by 0.06 pp.
3. **MULTI-BO.** Applying Eq. (2) (p. 6) to the Table 6 per-task scores gives 1.113, 1.047 and 1.006 for GPT-6 Astra, Fable 5.1 and GPT-5.5, against 1.132, 1.081 and 0.998 in Table 2. Table 2 averages over three seeds, which could move these values somewhat; GPT-5.5 is above 1.0 by this computation and below it in Table 2. In Table 3, DeepSeek-Flash under claude-code scores 59.83 against 59.81 under opencode, yet has MULTI-BO 1.081 ± 0.05, the same value and spread as Fable 5.1 in Table 2.
4. **Smaller slips.** The text (p. 4, p. 13) says the 21 figures span 6 tasks; Table 5 (p. 15) lists figures for 7 (heliostat, multibeam, dragon, production, sic, wordle, stair). On p. 17, 1.406276 m/s "with ratio 1.422195" is said to imply 2.2568 m/s, but 1.406276 × 1.422195 = 2.0000; the 2.2568 on p. 19 uses the ratio 1.604793.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.08237v1, checks its hash, finds the quoted passages and table values, and recomputes the Table 6 means with and without tennis, MULTI-BO from Eq. (2), the figure count and the dragon-dance products.

## Status

Contacting the authors, started 2026-11-15. Asked in [the terminal-bench-math-modeling repository](https://github.com/wxj630/terminal-bench-math-modeling/issues/2).

## Author response

None yet.

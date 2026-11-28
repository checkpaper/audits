# G-CAST: Governed Continual Self-Training for E-Commerce Agents (arXiv:2611.17814): consistency check

Two Ungated cells in Table 4 do not follow from the stated evaluation: the cumulative reward is 0.0033 above the mean of its three period rewards, while Static and Gated match exactly, and the skill-selection accuracy 0.6956 is not k / 300 for any k.

## Paper

- Title: G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demand
- arXiv: [2611.17814v1](https://arxiv.org/abs/2611.17814v1) (the version checked, sha256 `09e97c2a…b13a`)
- Hugging Face: [papers/2611.17814](https://huggingface.co/papers/2611.17814)
- Code: none listed
- CheckPaper report: [checkpaper.app/r/u3qkmjfr4t](https://checkpaper.app/r/u3qkmjfr4t)

## Findings

1. **Ungated cumulative reward.** Table 4 (p. 8) evaluates on Periods 1–3, three 100-query slices (pp. 5–6). For Static and Gated the cumulative reward equals the mean of the three period rewards (0.8810 and 0.9288; the Gated value is also Table 2, Iter. 3). For Ungated, (0.9380 + 0.8486 + 0.8812) / 3 = 0.8893, while the table and text give 0.8926.
2. **Ungated skill-selection accuracy.** On the 300-query suite an accuracy is k / 300. Static 0.6867 = 206/300 and Gated 0.8667 = 260/300, but Ungated 0.6956 lies between 208/300 = 0.6933 and 209/300 = 0.6967. The smallest denominator that gives 0.6956 is 427. It would fit if the metric were averaged over a different set of queries, which the paper does not state.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.17814v1, checks its hash, quotes the suite sizes and Table 4, and recomputes both cells.

## Status

No code repository or reachable contact address is listed; asked on the [Hugging Face paper page](https://huggingface.co/papers/2611.17814) on 2026-11-28.

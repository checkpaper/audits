# Let the Fixer Decide: Training a Code Localizer from the Fixer (arXiv:2611.12164): consistency check

The headline end-to-end result, S3r1-soft solving 8 tasks against 6 for its matched control, is not what Table 4 shows for those settings, and two Table 4 rows disagree with their own vs.-base counts.

## Paper

- Title: Let the Fixer Decide: Training a Code Localizer from the Fixer
- arXiv: [2611.12164v1](https://arxiv.org/abs/2611.12164v1) (the version checked, sha256 `4a95d6e5…b295`)
- Hugging Face: [papers/2611.12164](https://huggingface.co/papers/2611.12164)
- Code: [misraj-ai/locfix](https://github.com/misraj-ai/locfix)
- CheckPaper report: [checkpaper.app/r/xdzuratkdj](https://checkpaper.app/r/xdzuratkdj)

## Findings

1. **8 vs. 6 (abstract; Sec. 5.2, p. 9) versus Table 4 (p. 10).** The text says that at temperature 0.7 and 44 calls S3r1-soft solves 8 tasks and S3r1-ctrl 6, with 4 / 2 discordant tasks (a difference of 2). Table 4 gives both runs at those settings 6 solved. The 8 appears in the S3r1-soft row at temperature 0.2.
2. **Solved versus vs. base (Table 4).** The base solves 8, so each system should solve 8 − (base only) + (system only). This holds in 10 of the 12 rows. S3r1-soft at temperature 0.2 (4 / 2) implies 6 but prints 8; S3r1-ctrl (6 / 2) implies 4 but prints 6.
3. **Median calls versus Out of budget (Table 4).** The caption counts every task that used all tool calls as out of budget. In seven rows the median number of calls equals the budget (32 or 44), so at least 39 of 78 tasks used all calls, yet Out of budget is 24 to 38 in those rows.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12164v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

[Asked the authors](https://github.com/misraj-ai/locfix/issues/1) on 2026-11-27.

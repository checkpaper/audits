# Distilling Visual Agents from Limited Interaction Experience (arXiv:2611.28618): consistency check

In Table S3, run 4 of each of the three selectors equals its run 3 plus exactly 6 standard and 12 long-horizon successes.

## Paper

- Title: Distilling Visual Agents from Limited Interaction Experience
- arXiv: [2611.28618v1](https://arxiv.org/abs/2611.28618v1) (the version checked, sha256 `a0911a5b…0213`)
- Hugging Face: [papers/2611.28618](https://huggingface.co/papers/2611.28618)
- Code: [elated-sawyer/visual-agent-distillation](https://github.com/elated-sawyer/visual-agent-distillation)
- CheckPaper report: [checkpaper.app/r/5dwhm86ddh](https://checkpaper.app/r/5dwhm86ddh)

## Findings

1. **Run 3 to run 4 (Table S3, p. 13).** The table lists four separately trained repetitions per selector, each evaluated on 240 episodes per panel. From run 3 to run 4:
   - Complete selector: 199 → 205 standard, 50 → 62 long horizon.
   - Representativeness only: 192 → 198, 43 → 55.
   - Fixed random K4: 187 → 193, 38 → 50.

   All three change by exactly +6 and +12. Between the other consecutive runs the changes vary (for example +1/−12, +1/+4, +2/−8 from run 1 to run 2). For independent training and evaluation runs, three identical pairs of changes would be unusual, so the run 4 rows may have been derived from run 3 rather than measured.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.28618v1, checks its hash, quotes Table S3 and computes the run-to-run changes.

## Status

Confirmed by the authors on 2026-11-27: an aggregation error; corrected counts posted and the next revision will fix the tables. [Asked the authors](https://github.com/elated-sawyer/visual-agent-distillation/issues/1) on 2026-11-27.

## Author response

From the repository owner (elated-sawyer), 2026-11-27 11:46 UTC:

> The identical increments you identified are worth investigating. We will cross-check the original training and evaluation records to verify the independence of these runs and rule out any potential issues in result aggregation or transcription. [...] will update this issue once the verification is complete.

Follow-up from the owner, 2026-11-27 12:10 UTC:

> The identical increments were introduced by an error in our result aggregation: instead of reading each selector's own Run 4 results, we mistakenly applied the complete selector's Run 3→4 increments to the other two selectors.
>
> | Selector | Standard | Long horizon |
> |---|---:|---:|
> | Complete | 205/240 | 62/240 |
> | Representativeness only | 194/240 | 51/240 |
> | Fixed random K4 | 191/240 | 44/240 |
>
> We have corrected these entries and recomputed the affected summary statistics. We will include the corrected tables and corresponding text in the next revision.

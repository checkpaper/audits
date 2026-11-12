# Harness-S (arXiv:2611.04277): consistency checks

Table 1 is described as means over three runs, but its cells take the values a single run would give.

## Paper

- Title: Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training
- arXiv: [2611.04277v1](https://arxiv.org/abs/2611.04277v1) (the version checked, sha256 `4b2a410f…878f`)
- Hugging Face: [papers/2611.04277](https://huggingface.co/papers/2611.04277)
- Code: [DeepExperience/Harness-S](https://github.com/DeepExperience/Harness-S)
- CheckPaper report: [checkpaper.app/r/p3ybsxwtgv](https://checkpaper.app/r/p3ybsxwtgv)

## Findings

1. **Table 1 looks like single runs.** The caption (p. 7) and Appendix C (p. 17) say each score is a mean over three independent runs, each with three rollouts per task. The test sets have 262 (AppWorld), 160 (SWE-Gym) and 300 (DBBench) tasks (Table 6). One run gives Pass@3 = k/N and Avg@3 = k/3N. A mean of three runs lands on those values only when the three counts sum to a multiple of three, about one cell in three. In Table 1, 74 of 75 Pass@3 cells and 75 of 75 Avg@3 cells are exact single-run values, for example 67.56 = 177/262 and 38.75 = 62/160. The one exception, the 4B base model Pass@3 of 42.62, is 335/786, a three-run mean.
2. **Rank-1 margin.** Section 4.6 (p. 11) says the Rank-1 margin over H0 shrinks from 14.21 to 0.76 points in Pass@3. Table 5 gives 56.87 − 42.62 = 14.25 before training. The other three margins in the sentence match.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.04277v1, checks its hash, reads all 150 cells of Table 1, tests each against the single-run grid, and recomputes the Table 5 margins.

## Status

Contacting the authors, started 2026-11-12. Asked in [DeepExperience/Harness-S#1](https://github.com/DeepExperience/Harness-S/issues/1).

## Author response

None yet.

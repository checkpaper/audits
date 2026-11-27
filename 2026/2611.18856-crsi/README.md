# Self-Improvement Memory Enables Continual Recursive Self-Improvement (arXiv:2611.18856): consistency check

In Table 7, every Before and Gemini-After score is an exact count over the stated 220 or 225 TB2.1 rollouts, but none of the four Claude Opus 5.5 After scores is.

## Paper

- Title: Self-Improvement Memory Enables Continual Recursive Self-Improvement
- arXiv: [2611.18856v1](https://arxiv.org/abs/2611.18856v1) (the version checked, sha256 `a8299ba5…ff3d`)
- Code: none linked
- CheckPaper report: [checkpaper.app/r/wuqzd4cvcp](https://checkpaper.app/r/wuqzd4cvcp)

## Findings

1. **Opus-After scores do not fit the rollout counts.** Table 4 (p. 18) gives the TB2.1 evolve split as 44 tasks / 220 rollouts and the held-out split as 45 / 225. In Table 7 (p. 25) the eight Before and Gemini-After scores are exact: 86.82 = 191/220, 90.45 = 199/220, 85.91 = 189/220, 89.09 = 196/220, 85.78 = 193/225, 90.22 = 203/225, 87.56 = 197/225, 91.56 = 206/225. The Opus-After scores 91.23 and 92.21 (evolve) and 91.28 and 91.61 (held-out) are not: the nearest attainable values are 91.36, 92.27, 91.11 and 91.56. One rollout is worth 0.45 or 0.44 points, so the held-out Terminus-2 margin of Opus over Gemini (+0.05) is smaller than a single rollout.

This is a question for the authors, not a conclusion: the Opus rows may use a different allocation or an average over runs that the caption does not mention.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.18856v1, checks its hash, quotes Table 4 and Table 7 and tests every score for k / n.

## Status

Emailed the first and last authors on 2026-11-27 (addresses from p. 1).

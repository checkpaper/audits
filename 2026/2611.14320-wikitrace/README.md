# Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation (arXiv:2611.14320): consistency checks

The released per-sample results include an ACE baseline that is not in Table 1 and scores above WikiTrace on two suites.

## Paper

- Title: Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation
- arXiv: [2611.14320v1](https://arxiv.org/abs/2611.14320v1) (the version checked, sha256 `0f434777…a8cd`)
- Hugging Face: [papers/2611.14320](https://huggingface.co/papers/2611.14320)
- Code: [yukyeongleee/wikitrace](https://github.com/yukyeongleee/wikitrace)
- CheckPaper report: [checkpaper.app/r/xnzf533rfn](https://checkpaper.app/r/xnzf533rfn)

## Findings

1. **ACE baseline.** The abstract says WikiTrace consistently outperforms existing memory approaches, and Section 1 (p. 2) says it achieves the best performance on every suite. The repository file `tests/analysis/fixtures/paper_per_sample.csv` (commit `9ee357f`) holds three trials per suite for seven methods. One of them, `RCI-traverse`, reproduces the WikiTrace row of Table 1. Another, `ace`, does not appear in the paper. ACE scores 94.0 and 92.7 on PlanCraft seen and unseen, against 93.3 and 81.3 for WikiTrace, and ties it on AppWorld challenge (75.8).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.14320v1 and the results file at a fixed commit, checks both hashes, and recomputes the suite means for WikiTrace and ACE.

## Status

Explained by the authors on 2026-11-13: ACE was left out on purpose because its memory build costs far more than WikiTrace's, and the ACE rows in the fixture were not meant to be released. The fixture has been replaced with a synthetic test. Asked in [the WikiTrace repository](https://github.com/yukyeongleee/wikitrace/issues/2).

## Author response

2026-11-13, yukyeongleee, in [the issue](https://github.com/yukyeongleee/wikitrace/issues/2), with a figure of cumulative build cost:

> We left ACE out of the comparison on purpose. Under our protocol its memory build is far more expensive than WikiTrace's and grows faster with the number of past runs: after 38 training runs its cumulative build cost is about 4.3x WikiTrace's, and each additional run costs it more than the last (figure below; cost as multiples of No Memory's test cost per sample, geometric mean over benchmarks). We therefore did not treat it as a like-for-like baseline for the setting the paper studies, where memory must be built cheaply from a fixed set of past runs.
>
> The ACE rows came along when we assembled a test fixture from our internal result files; they were not meant to be part of the release. The fixture only checked that the analysis code reproduces the paper's Gain/Regression numbers, and we have replaced it with a small synthetic test.

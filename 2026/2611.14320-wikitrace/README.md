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

Contacting the authors, started 2026-11-12. Asked in [yukyeongleee/wikitrace#2](https://github.com/yukyeongleee/wikitrace/issues/2).

## Author response

None yet.

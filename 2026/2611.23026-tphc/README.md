# TPHC: Improving Hyper-Connections with Tensor-Parallel Grouped Updates (arXiv:2611.23026): consistency check

Sec. 4.1 says TPHC's train and val losses are "0.4–1.7% below mHC-TFA"; Table 1 gives 0.41–0.73% at N = 4, 8 and 16, so the upper end of the range is not in the table.

## Paper

- Title: TPHC: Improving Hyper-Connections with Tensor-Parallel Grouped Updates
- arXiv: [2611.23026v1](https://arxiv.org/abs/2611.23026v1) (the version checked, sha256 `9a6b87f1…3c47`)
- Hugging Face: [papers/2611.23026](https://huggingface.co/papers/2611.23026)
- Code: [wuyou2002/TPHC](https://github.com/wuyou2002/TPHC)
- CheckPaper report: [checkpaper.app/r/u98qett6bq](https://checkpaper.app/r/u98qett6bq)

## Findings

1. **Loss gap to mHC-TFA (Sec. 4.1, p. 6).** "TPHC achieves the lowest training and validation loss at every N, 0.7–1.0% below mHC and 0.4–1.7% below mHC-TFA on both." From Table 1 the relative gaps to mHC-TFA are 0.41/0.41% (N = 4), 0.73/0.73% (N = 8) and 0.71/0.71% (N = 16) for train/val. The range against mHC (0.70–1.04%) matches the text, so 1.7 may be a typo for 0.7.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.23026v1, checks its hash, quotes Sec. 4.1 and Table 1, and recomputes the relative gaps.

## Status

Answered. [Asked the authors](https://github.com/wuyou2002/TPHC/issues/2) on 2026-11-22.

The first author replied on 2026-11-22: the range should read 0.4–0.7 0.000000or both training and validation loss; the 1.7% upper bound is a typo, to be fixed in a future revision.

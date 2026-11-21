# How Far Can Untrained Neural Networks Go in Anomaly Detection? From Tables to Pixels (arXiv:2611.08136): consistency check

Proposition 1 splits the score gap exactly into a covariance part and a mean part, ∆ = ∆cov + ∆mean, and Table 7 reports their means over 47 datasets. Means are additive, yet ∆cov + ∆mean is 89.91 for PRISM-T against ∆ = 91.50 (and 114.73 against 114.82 for w/o Act.), while the standardized G rows add up.

## Paper

- Title: How Far Can Untrained Neural Networks Go in Anomaly Detection? From Tables to Pixels
- arXiv: [2611.08136v1](https://arxiv.org/abs/2611.08136v1) (the version checked, sha256 `013e0ac8…b264`)
- Hugging Face: [papers/2611.08136](https://huggingface.co/papers/2611.08136)
- Code: [ideal-lab-sejong/PRISM_T](https://github.com/ideal-lab-sejong/PRISM_T)
- CheckPaper report: [checkpaper.app/r/7wnavjnd8p](https://checkpaper.app/r/7wnavjnd8p)

## Findings

1. **Table 7 (p. 11) does not add up.** Proposition 1 (Eq. 7, p. 4) gives ∆ = ∆cov + ∆mean for each dataset, so the means over the 47 datasets must add too. In units of 10³:

   | | ∆cov | ∆mean | sum | ∆ in Table 7 |
   |---|---|---|---|---|
   | Raw | 45.18 | 1.69 | 46.87 | 46.88 |
   | w/o Act. | 110.56 | 4.17 | 114.73 | 114.82 |
   | PRISM-T | 60.58 | 29.33 | 89.91 | 91.50 |

   The G, Gcov and Gmean rows add up to within 0.01 in all three columns, so the gap is in the ∆ rows only. The linked report reran the released code and got ∆mean 4.26 and 30.91 for the last two columns, which would close both gaps.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.08136v1, checks its hash, quotes Proposition 1 and Table 7, and adds up the rows.

## Status

[Asked the authors](https://github.com/ideal-lab-sejong/PRISM_T/issues/2) on 2026-11-21.

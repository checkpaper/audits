# Scaling Mathematical Proof Supervision from Structured Textbooks (arXiv:2610.40394): consistency check

The two panels of the human-calibration table give different overall numbers: Panel A's Overall row is the plain mean of the six subject rows (human accept 47.9, H–L agreement 85.9), while weighting Panel B by its own population shares gives 48.85 and 86.09.

## Paper

- Title: Scaling Mathematical Proof Supervision from Structured Textbooks (TOME-Math)
- arXiv: [2610.40394v1](https://arxiv.org/abs/2610.40394v1) (the version checked, sha256 `dbac1073…7b18`)
- Code: none linked
- CheckPaper report: [checkpaper.app/r/rrjxqyakhf](https://checkpaper.app/r/rrjxqyakhf)

## Findings

1. **Panel A Overall is an unweighted mean.** Table 8 (p. 30) gives six subject rows with n = 100 each. Their plain means are 47.900, 8.700, 18.133 and 85.917, which round to the Overall row (47.9, 8.7, 18.1, 85.9). The caption and App. D.4 (p. 29) say the entries are inverse-probability weighted estimates. With equal 50-problem subjects an equal subject weight can be reasonable, so this alone is not an error.
2. **Panel B gives a different overall.** The four vote strata in Panel B have population shares 42.3, 7.8, 18.1 and 31.8 (summing to 100) and human-accept rates 91.3, 68.4, 22.1 and 2.8. Weighted by those shares, overall human accept is 48.85 and H–L agreement 86.09, against 47.9 and 85.9 in Panel A. Rounding of the inputs moves these by about ±0.1, not by 0.95.

These are questions for the authors, not conclusions.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.40394v1, checks its hash, quotes all Table 8 rows and recomputes both overall figures.

## Status

Emailed the corresponding authors on 2026-11-27 (addresses from their earlier papers).

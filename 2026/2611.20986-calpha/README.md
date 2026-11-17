# Calpha: Toward Native Biomolecular Intelligence in a General-Purpose Language Model (arXiv:2611.20986): consistency checks

The Sec. 4.4 split of BioMatrix-4B's CAMEO-2025 score (0.96 on 15 targets, 0.28 on 185) averages 0.331, while Table 4 gives 0.311.

## Paper

- Title: Calpha: Toward Native Biomolecular Intelligence in a General-Purpose Language Model
- arXiv: [2611.20986v1](https://arxiv.org/abs/2611.20986v1) (the version checked, sha256 `3ea168a3…7645`)
- Hugging Face: [papers/2611.20986](https://huggingface.co/papers/2611.20986)
- Code: [yliust/Calpha](https://github.com/yliust/Calpha)
- CheckPaper report: [checkpaper.app/r/6a2pjqgu5d](https://checkpaper.app/r/6a2pjqgu5d)

## Findings

1. **BioMatrix-4B on CAMEO-2025.** Table 4 (p. 6) gives BioMatrix-4B a mean TM-score of 0.311 on all 200 CAMEO-2025 targets. Sec. 4.4 (p. 7) says 15 of these sequences occur verbatim in the BioMatrix training set and the model scores 0.96 on them and 0.28 on the other 185. That split averages (15 × 0.96 + 185 × 0.28) / 200 = 0.331. Even at the bottom of the rounding ranges (0.955 and 0.275) the mean is 0.326. With a mean of 0.311 and 15 targets at 0.96, the other 185 would average 0.258.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.20986v1, checks its hash, quotes Table 4 and Sec. 4.4, and recomputes the mean.

## Status

[Asked the authors](https://github.com/yliust/Calpha/issues/1) on 2026-11-18.

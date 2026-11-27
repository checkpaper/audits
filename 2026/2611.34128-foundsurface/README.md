# FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images (arXiv:2611.34128): consistency check

Table 12 reports identical standard deviations, in all five metrics, for two pairs of methods whose means in Table 1 differ widely.

## Paper

- Title: FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images
- arXiv: [2611.34128v1](https://arxiv.org/abs/2611.34128v1) (the version checked, sha256 `248a5337…3008`)
- Hugging Face: [papers/2611.34128](https://huggingface.co/papers/2611.34128)
- Code: [vLAR-group/FoundSurface](https://github.com/vLAR-group/FoundSurface)
- CheckPaper report: [checkpaper.app/r/nkrptfa7y7](https://checkpaper.app/r/nkrptfa7y7)

## Findings

1. **ScanNet++ (Table 12, p. 18).** Projection and PriorDA both have ±0.129 / ±0.170 / ±0.103 / ±0.134 / ±0.127 (ADE / RMSE / Abs-Rel / Sq-Rel / δ). Their Table 1 means are 0.580 / 0.959 / 0.360 / 0.554 / 0.636 and 0.198 / 0.290 / 0.123 / 0.101 / 0.868.
2. **7Scenes (Table 12, p. 18).** CUT3R and RayletDF both have ±0.045 / ±0.092 / ±0.025 / ±0.028 / ±0.040. Their Table 1 means are 0.197 / 0.305 / 0.105 / 0.054 / 0.878 and 0.158 / 0.295 / 0.084 / 0.049 / 0.907.

Two methods with different per-scene errors would not normally share all five standard deviations to three decimals, so one row in each pair is probably a copy of the other. Table 12 is the evidence for "our method achieves the most robust performance".

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.34128v1, checks its hash, quotes the rows above and compares them.

## Status

Not yet sent.

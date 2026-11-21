# Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU (arXiv:2611.25279): consistency check

App. D says the Hilti-Oxford IMU noise was set to the setting with the lowest mean control-point error in Table 13, namely the walks at three times their bounds (0.159 m, bold). Table 13 lists a lower value for the walks at their bounds, ×1: 0.154 m.

## Paper

- Title: Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU
- arXiv: [2611.25279v1](https://arxiv.org/abs/2611.25279v1) (the version checked, sha256 `51746acc…84c3`)
- Hugging Face: [papers/2611.25279](https://huggingface.co/papers/2611.25279)
- Code: [be2rlab/ACCORD](https://github.com/be2rlab/ACCORD)
- CheckPaper report: [checkpaper.app/r/jgxzd8bv57](https://checkpaper.app/r/jgxzd8bv57)

## Findings

1. **The chosen IMU noise is not the lowest in Table 13 (pp. 15, 17).** App. D: "the setting with the lowest mean error at the control points was taken (Tab. 13): the densities as measured and the walks at three times their bounds." Table 13 gives, for the walks at ×1 / 3 / 10 their bounds, 0.154 / 0.159 / 0.173 m, with 0.159 in bold. By the stated rule the ×1 walks (0.154) would be chosen. The densities row (×1 = 0.167) does not equal either walk cell either, so it is unclear which walk setting it was run with.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.25279v1, checks its hash, quotes App. D and Table 13, and finds the lowest cell and the bold one.

## Status

[Asked the authors](https://github.com/be2rlab/ACCORD/issues/3) on 2026-11-22.

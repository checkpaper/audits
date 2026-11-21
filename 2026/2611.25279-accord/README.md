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

Answered. [Asked the authors](https://github.com/be2rlab/ACCORD/issues/3) on 2026-11-22.

The first author replied on 2026-11-21: App. D omits the full rule, under which a difference within 5 mm counts as a tie that goes to the larger noise. Unrounded, walks ×1 give 0.1545 m and ×3 0.1589 m (4.4 mm apart), so ×3 was taken. Their per-sequence values (exp14, exp05, exp11, exp07, exp15) reproduce the three means. We asked which walk setting the densities row (×1 = 0.167 m) uses.

Follow-up reply on 2026-11-21: the densities row was run with the dataset's first-configuration walks (1e-3 and 5e-5), so its ×1 cell (0.167 m) matches none of the walk cells; the walks row was then run with the chosen densities. The released `config/hilti/kalibr_imu_chain.yaml` uses densities 1.42e-3 / 2.44e-4 and walks 5.58e-4 / 1.26e-5. The authors plan to fix the App. D wording and the Tab. 13 caption in the next arXiv version.

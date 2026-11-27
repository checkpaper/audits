# MotionGraphicsBench (arXiv:2611.10592): consistency check

The iteration curve in Table 10 reports means of three agreement rates over 180 animations, but only the Final value (93.33%) is a possible mean of that kind; the five intermediate values are not, and "Iterations 5–7" (93.32%) differs from Final although finished instances keep their final results.

## Paper

- Title: MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic Verification
- arXiv: [2611.10592v2](https://arxiv.org/abs/2611.10592v2) (the version checked, sha256 `b141875b…4034`)
- Data: [figma-ai/motion-graphics-bench](https://huggingface.co/datasets/figma-ai/motion-graphics-bench)
- CheckPaper report: [checkpaper.app/r/v8t6hbb3yd](https://checkpaper.app/r/v8t6hbb3yd)

## Findings

1. **Intermediate means are not k / 540.** Sec. 5.2 and App. C.4 say Table 10 reports mean agreement across the three Full runs on the 180-animation test set. Each run's agreement is a count out of 180, so a three-run mean is a multiple of 1/540 (0.185 points). Final 93.33% fits (168 + 167 + 169 = 504 of 540, matching Table 9). Iterations 1–4 and 5–7 (61.79, 88.32, 91.28, 92.02, 93.32%) do not; the nearest possible values are 61.85, 88.33, 91.30, 92.04 and 93.33%.
2. **Iterations 5–7 vs Final.** App. C.4 says instances that finish earlier keep their final program results in later iteration summaries, so the last iteration row should equal Final. It is 0.01 points lower, less than one animation in one run.

The trend (largest gain after the first revision) is not affected. A different aggregation for the intermediate rows, such as a per-instance average, would explain both points; the paper does not mention one.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.10592v2, checks its hash, quotes Tables 9 and 10 and tests each value for k / 540.

## Status

Emailed the first author on 2026-11-28.

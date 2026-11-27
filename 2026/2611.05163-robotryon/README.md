# RoboTryOn: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On (arXiv:2611.05163): consistency check

In the per-task component ablation (Table 13), removing the autoregressive reference lowers 10 of the 11 tasks by exactly 2 of 28 trials.

## Paper

- Title: Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On
- arXiv: [2611.05163v1](https://arxiv.org/abs/2611.05163v1) (the version checked, sha256 `6b41a148…3be`)
- Hugging Face: [papers/2611.05163](https://huggingface.co/papers/2611.05163)
- Code: [ryan-seungyong-lee/RoboTryOn](https://github.com/ryan-seungyong-lee/RoboTryOn)
- CheckPaper report: [checkpaper.app/r/8vzgpzdkcd](https://checkpaper.app/r/8vzgpzdkcd)

## Findings

1. **Table 13 (p. 26).** Success rates are over 28 trials per task (Table 11 caption, p. 25). Converted to successes, the full model and the variant without the autoregressive reference are:

   | Task | Full | w/o AR reference |
   |---|---|---|
   | PnP Bottle / Doll / Box / Ball | 26 / 20 / 20 / 19 | 24 / 18 / 18 / 17 |
   | Coffee Pot / Bottle to Shelf / Pouring / Brushing | 18 / 25 / 24 / 23 | 16 / 23 / 22 / 21 |
   | Box Convey / Air Fryer / Ball in Cup | 22 / 17 / 14 | 20 / 15 / 13 |

   Ten tasks drop by exactly 2 and the eleventh by 1. The other ablated variants in the same table change by widely different amounts per task. Independently evaluated policies would not normally differ by the same count on 10 of 11 tasks, so the w/o-reference row may have been derived from the full model's row rather than measured.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.05163v1, checks its hash, quotes Table 13 and converts it to trial counts.

## Status

[Asked the authors](https://github.com/ryan-seungyong-lee/RoboTryOn/issues/2) on 2026-11-27.

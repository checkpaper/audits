# Non-penetrating World Models (arXiv:2611.27963): consistency check

Sec. 4.4 gives 31.1% as the share of safe inputs that the better mode alters on Hy-Nomas, but in Table 3 the better mode on Hy-Nomas (collision mode, Score 76.7) alters 49.4%; 31.1% is the prediction mode's rate.

## Paper

- Title: Non-penetrating World Models
- arXiv: [2611.27963v1](https://arxiv.org/abs/2611.27963v1) (the version checked, sha256 `6b97b3ab…f96e`)
- Hugging Face: [papers/2611.27963](https://huggingface.co/papers/2611.27963)
- Code: [yuhangdai427/NoPeWorld](https://github.com/yuhangdai427/NoPeWorld)
- CheckPaper report: [checkpaper.app/r/wfkgknzhyp](https://checkpaper.app/r/wfkgknzhyp)

## Findings

1. **Task 1 summary (p. 7) versus Table 3 (p. 5).** Sec. 4.4 says "The better mode alters 4–15% of safe inputs, 31.1% on Hy-Nomas." Taking the mode with the higher Score in Table 3, the False rates on the other five generators are 7.0, 9.2, 12.7, 4.4 and 14.6%, which fits 4–15%. On Hy-Nomas the higher-Score mode is collision (76.7 vs. 72.7), whose False rate is 49.4%. The 31.1% is the False rate of prediction mode, which scores lower. Table S3 (p. 15) gives the same 49.4 / 31.1.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.27963v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

[Asked the authors](https://github.com/yuhangdai427/NoPeWorld/issues/1) on 2026-11-27.

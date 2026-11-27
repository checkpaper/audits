# Learning Heterogeneous Tactile Representation for General Dexterous Manipulation (LingBot-Touch, arXiv:2611.12806): consistency check

The abstract's "14 to 26 percentage points" exceeds the largest gain the paper reports (24.8), and Table 2, described as success rates over 20 trials, contains values that 20 trials cannot produce.

## Paper

- Title: Learning Heterogeneous Tactile Representation for General Dexterous Manipulation
- arXiv: [2611.12806v1](https://arxiv.org/abs/2611.12806v1) (the version checked, sha256 `5f0c52f4…ba3`)
- Hugging Face: [papers/2611.12806](https://huggingface.co/papers/2611.12806)
- Code: [Robbyant/lingbot-touch](https://github.com/Robbyant/lingbot-touch)
- CheckPaper report: [checkpaper.app/r/8js6wyqfge](https://checkpaper.app/r/8js6wyqfge)

## Findings

1. **Abstract range (p. 2) versus Sec. 5.2 (p. 15).** The abstract says the encoder raises the four policies' success rates by 14 to 26 percentage points. Sec. 5.2 gives the 26-task means (DP 21.6 → 35.6, π0.5 48.1 → 69.9, LingBot-VLA 48.3 → 73.1, T-Rex 45.4 → 68.6) and the gains 13.9, 21.8, 24.8 and 23.2. The upper end is 24.8, not 26.
2. **"Success rates ... over 20 trials per task" (Table 2, p. 16).** A success rate over 20 trials is a multiple of 5. Only 85 of the 336 two-decimal values on the page are; most, such as 46.25 or 63.75, match the partial-credit point rubrics in App. B instead. The Deformable cup transport row has 93.30 and 96.70 for LingBot-VLA, which fit neither 20 trials (18.66 / 19.34 successes) nor 4- or 5-point partial credit over 20 trials (multiples of 1.25 or 1.0).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12806v1, checks its hash, quotes the passages above and recomputes the values.

## Status

Not yet sent.

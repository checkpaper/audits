# RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models (arXiv:2611.24098): consistency checks

Six of the eight RM→R success rates in Table 3 are not attainable as k/191, and three speech F1 values do not follow from the precision and recall in the same row.

## Paper

- Title: RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models
- arXiv: [2611.24098v1](https://arxiv.org/abs/2611.24098v1) (the version checked, sha256 `2318e200…b3dd`)
- Hugging Face: [papers/2611.24098](https://huggingface.co/papers/2611.24098)
- Code: [Whalesong-zrs/RoughCut-Bench](https://github.com/Whalesong-zrs/RoughCut-Bench)
- CheckPaper report: [checkpaper.app/r/m2tb4fjges](https://checkpaper.app/r/m2tb4fjges)

## Findings

1. **RM→R success rates.** Eq. 2 (p. 5) defines RM→R success as successful pairs over annotated pairs, with speech metrics "computed from decision counts aggregated across all cases"; Fig. 1 (p. 3) gives 191 RM→R pairs. Each rate should then be k/191. In Table 3 (p. 7) only Gemini 3.0 Pro (0.497 = 95/191) and GPT-5.5 (0.340 = 65/191) fit. The others fall between two grid points, for example the best rate, GLM-5V-Turbo's 0.537 (102/191 = 0.5340, 103/191 = 0.5393), and Qwen3.5-Plus's 0.535.
2. **F1 versus P and R.** Qwen3.5-Plus: IM P 0.511, R 0.785 give F1 0.619 (reported 0.617); D P 0.732, R 0.444 give F1 0.553 (reported 0.543, the same as GLM-5V-Turbo's D F1). Qwen3.7-Plus: D P 0.828, R 0.448 give 0.581 (reported 0.580). The other 13 F1 values in Table 3 are within rounding.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.24098v1, checks its hash, quotes the definitions, parses Table 3, checks each RM→R rate against the 1/191 grid, and recomputes each F1 range from P and R.

## Status

Answered. [Asked the authors](https://github.com/Whalesong-zrs/RoughCut-Bench/issues/1) on 2026-11-20.

The author (Whalesong-zrs) replied on 2026-11-20 and closed the issue as completed. All metrics pool TP, FP and FN over 10 repeated runs, and RM→R success divides the total successful pairs by the total evaluated pairs, so the denominator is up to 10 × 191 = 1,910, less any unevaluable outputs; v1 does not describe this. The Qwen entries in Table 3 were prepared incorrectly and will be corrected; other last-digit F1 differences come from rounding. The authors will update Table 3, document the protocol and effective denominators, and post the revised arXiv version.

# SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering (arXiv:2611.13410): consistency check

In Table 1, every benchmark score in the Qwen3-8B W4A8 block (30 of 30) and in the Qwen3.5-4B BF16 row (5 of 5) is a multiple of 0.05, while the other blocks have 7 such values out of 130.

## Paper

- Title: SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering
- arXiv: [2611.13410v1](https://arxiv.org/abs/2611.13410v1) (the version checked, sha256 `12145019…e8c1ee8`)
- Hugging Face: [papers/2611.13410](https://huggingface.co/papers/2611.13410)
- Code: [air-embodied-brain/SteerDistill](https://github.com/air-embodied-brain/SteerDistill)
- CheckPaper report: [checkpaper.app/r/c3nvgfddus](https://checkpaper.app/r/c3nvgfddus)

## Findings

1. **Precision of the W4A8 block (Table 1, p. 6).** Scores are success rates or accuracies at two decimals. A second decimal of 0 or 5 should occur about one time in five. Counting the five benchmark columns (Avg. excluded):
   - Qwen3-8B W4A8, all six methods: 30 of 30 (e.g. GPTQ 35.90 / 22.90 / 54.70 / 66.80 / 30.20).
   - Qwen3.5-4B BF16: 5 of 5 (50.40 / 62.80 / 69.80 / 78.60 / 46.80).
   - All other blocks: 7 of 130.

   The W4A8 block looks rounded to 0.05 or produced differently from the rest of the table, and the paper does not say how. The W4A8 comparison is the basis for the claim that SteerDistill beats QeRL by 1.93 points (Sec. 4.2).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.13410v1, checks its hash, parses Table 1 and counts the values per block.

## Status

Not yet sent.

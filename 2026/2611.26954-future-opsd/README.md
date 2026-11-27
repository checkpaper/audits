# Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation (arXiv:2611.26954): consistency check

Three of the six Score values in the training-cost table (Table 6) differ from the same runs in Tables 1 and 2, and one General Video Understanding average in Table 1 does not follow from its four values.

## Paper

- Title: Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation
- arXiv: [2611.26954v1](https://arxiv.org/abs/2611.26954v1) (the version checked, sha256 `669b3edd…068a`)
- Hugging Face: [papers/2611.26954](https://huggingface.co/papers/2611.26954)
- Code: [Jingchensun/future-opsd](https://github.com/Jingchensun/future-opsd)
- CheckPaper report: [checkpaper.app/r/c35qb97xw3](https://checkpaper.app/r/c35qb97xw3)

## Findings

1. **Table 6 Score versus Tables 1 and 2 (p. 8; p. 5).** For Qwen3-VL-8B, Naive OPSD (48.9, 61.2) and Future-OPSD on EgoPlan-IT (53.6) match the main tables (the SEED-Bench-R1 L1–L3 mean in Table 2, the TwiFF-Bench Avg in Table 1). Three do not: SFT on EgoPlan-IT is 44.3 in Table 6 against 46.30 from Table 2 (47.4, 48.6, 42.9); SFT on Future-L1 is 57.3 against 58.5 in Table 1; Future-OPSD on Future-L1 is 66.9 against 67.8 in Table 1.
2. **Table 1, Qwen3.5-9B Future-OPSD, General Video Understanding Avg (p. 5).** The four values (79.3, 21.5, 63.1, 65.9) average to 57.45, but the row prints 57.2 with Δ +0.2 over the base (57.0). From the printed values the gain is +0.4.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.26954v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

Not yet sent.

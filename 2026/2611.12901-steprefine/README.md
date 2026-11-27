# Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding (arXiv:2611.12901): consistency check

The Dream-VL MMHalu baseline in Table 1 differs from the same setting in Table 5, and the reference bars in the motivating Fig. 2(c) carry the StepRefine numbers rather than the baseline.

## Paper

- Title: Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding
- arXiv: [2611.12901v1](https://arxiv.org/abs/2611.12901v1) (the version checked, sha256 `189a6ab9…95b7`)
- Hugging Face: [papers/2611.12901](https://huggingface.co/papers/2611.12901)
- Code: [mdlm-steprefine/mdlm-steprefine](https://github.com/mdlm-steprefine/mdlm-steprefine)
- CheckPaper report: [checkpaper.app/r/6vzmmxhqac](https://checkpaper.app/r/6vzmmxhqac)

## Findings

1. **Dream-VL baseline (Table 1, p. 6 vs Table 5, p. 21).** All main results use L = 256, T = 256 and low-confidence remasking (Sec. 4.1). For Dream-VL-7B on MMHalu, Table 1 gives Base 3.54 and StepRefine 3.68. Table 5(a) (low confidence) and Table 5(b) (L = 256, T = 256) both give Base 3.47 with the same StepRefine 3.68. The 3.54 is the Table 5(b) Base value at T = 128. The gain is +0.14 in Table 1 and +0.21 in Table 5.
2. **Fig. 2(c) reference bars (p. 4).** The figure compares low-confidence remasking with random remasking at 10% of random steps (top) and at entropy-spike steps (bottom), on LLaDA-V. The Low-confidence bars, drawn in both panels, are 58.6 / 59.2 / 56.5 (VStar / RealWorldQA / MathVista). These are the Table 1 LLaDA-V StepRefine values; the low-confidence Base values are 55.5 / 57.5 / 54.7. If the bars are meant to be the baseline, random remasking at spike steps (58.1 / 58.8 / 55.7) would lie above it rather than show "negligible change".

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12901v1, checks its hash, quotes the passages above and compares the values.

## Status

Not yet sent.

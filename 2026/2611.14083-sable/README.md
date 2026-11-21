# Sable: A Small-Field Sumcheck Argument for Bit-Exact Inference of Large Language Models (arXiv:2611.14083): consistency check

The prover section (p. 32) says that without the per-layer reduction the two extra passes took "about 25% of the proving time at every shape", but the per-layer-reduction row of Table 10 saves 8.2%, 11.5% and 12.5% of the time at the three shapes.

## Paper

- Title: Sable: A Small-Field Sumcheck Argument for Bit-Exact Inference of Large Language Models
- arXiv: [2611.14083v1](https://arxiv.org/abs/2611.14083v1) (the version checked, sha256 `44309ee4…ed14`)
- Hugging Face: [papers/2611.14083](https://huggingface.co/papers/2611.14083)
- Code: [moonmath-ai/Sable](https://github.com/moonmath-ai/Sable)
- CheckPaper report: [checkpaper.app/r/4r5664zhgy](https://checkpaper.app/r/4r5664zhgy)

## Findings

1. **Share of proving time (p. 32 vs Table 10, p. 43).** "without it, the global evaluation proof needed two more full passes over every layer, about 25% of the proving time at every shape." Table 10 measures each optimization against the state just before it; the per-layer reduction row goes from 108.2 / 304.7 / 479.1 s to 99.3 / 269.6 / 419.3 s, a saving of 8.2 / 11.5 / 12.5%. From 108.2 / 304.7 / 479.1 s down to the last row of the table (92.4 / 254.0 / 397.1 s), the per-layer reduction and the optimizations after it save 14.6 / 16.6 / 17.1%.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.14083v1, checks its hash, quotes the claim and Table 10, and recomputes the savings.

## Status

[Asked the authors](https://github.com/moonmath-ai/Sable/issues/2) on 2026-11-22.

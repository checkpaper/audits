# DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding (arXiv:2611.21925): consistency checks

The head-ablation gains in Sec. 5.4.2 do not match Table 6, and the +58% Transformers throughput gain at B = 32 is +49% in Table 3.

## Paper

- Title: DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding
- arXiv: [2611.21925v1](https://arxiv.org/abs/2611.21925v1) (the version checked, sha256 `635c8b38…1d8b`)
- Hugging Face: [papers/2611.21925](https://huggingface.co/papers/2611.21925)
- Code: [J-sandler/DNeo](https://github.com/J-sandler/DNeo)
- CheckPaper report: [checkpaper.app/r/e7bfym2tnr](https://checkpaper.app/r/e7bfym2tnr)

## Findings

1. **Head ablation (Sec. 5.4.2, p. 14).** The text says the fused head "exhibits +0.056 τ and +0.141 τ over the DFlash-2 head, and DSpark head alone (respectively)". Table 6 gives DFlash-2 head 2.217, DSpark head 2.273 and DNeo head 2.361, so the gains are +0.144 over the DFlash-2 head and +0.088 over the DSpark head; the table also ranks the DSpark head above the DFlash-2 head. The text's two numbers match the additive ablation of Table 8 (p. 21) instead: 2.646 − 2.590 = +0.056 over the DFlash-2 score head and 2.646 − 2.505 = +0.141 over the DSpark-head step.
2. **Transformers throughput (Sec. 5.3, p. 12).** The text says DNeo achieves "up-to +58% higher throughput (at B=32) than DFlash-2 (Transformers serving)". Table 3 gives 2,201 vs. 1,475 tokens/s at B = 32, i.e. +49.2%. No Transformers column reaches +58% (the largest is +56.0% at B = 16).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.21925v1, checks its hash, quotes Sec. 5.3, Sec. 5.4.2, Table 3, Table 6 and Table 8, and recomputes the differences and ratios.

## Status

Answered. [Asked the authors](https://github.com/J-sandler/DNeo/issues/3) on 2026-11-20.

The author (J-sandler) replied on 2026-11-20: "Hi, thanks for noticing this. We will fix these small typos promptly."

# GlyphAtlas: Disentangling Stroke Detail from Layout for Scene Text Synthesis (arXiv:2611.20192): consistency check

The GlyphAtlas row of Table 1 takes some cells from the Fixed model and some from the Random model of Table S6, and two cells appear in neither.

## Paper

- Title: GlyphAtlas: Disentangling Stroke Detail from Layout for Scene Text Synthesis
- arXiv: [2611.20192v1](https://arxiv.org/abs/2611.20192v1) (the version checked, sha256 `2835d437…e331`)
- Hugging Face: [papers/2611.20192](https://huggingface.co/papers/2611.20192)
- Code: [Fr0zenCrane/GlyphAtlas](https://github.com/Fr0zenCrane/GlyphAtlas)
- CheckPaper report: [checkpaper.app/r/fxbar4dzgw](https://checkpaper.app/r/fxbar4dzgw)

## Findings

1. **Table 1 row versus Table S6 (p. 6; p. 18).** Table 1 gives GlyphAtlas EN 88.68 / 0.9555 / 11.99 / 0.0759 and ZH 77.92 / 0.8806 / 11.50 / 0.0534 (ACC / NED / FID / LPIPS). At 64 px, Table S6 gives Fixed 88.48 / 0.9552 / 12.00 / 0.0759 and 77.77 / 0.8806 / 11.50 / 0.0574, and Random 88.68 / 0.9555 / 12.27 / 0.0756 and 77.92 / 0.8802 / 11.90 / 0.0574. EN ACC, EN NED and ZH ACC match Random; EN LPIPS, ZH NED and ZH FID match Fixed; EN FID 11.99 and ZH LPIPS 0.0534 match neither. With 0.0574, FLUX-Text (0.0541) would be best on ZH LPIPS in Table 1.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.20192v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

[Asked the authors](https://github.com/Fr0zenCrane/GlyphAtlas/issues/1) on 2026-11-23.

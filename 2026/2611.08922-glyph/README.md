# Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data (arXiv:2611.08922): consistency checks

The introduction attaches the supplement's Recent Phecode p-values to the all-history Phecode rates, with a different External Site #1 p-value, and the "33.8% cohort average at External Site #2" is the report-findings row of Figure 2, whose cohort-wide rate is 54.7%.

## Paper

- Title: Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data
- arXiv: [2611.08922v1](https://arxiv.org/abs/2611.08922v1) (the version checked, sha256 `662d3994…af7c`)
- Hugging Face: [papers/2611.08922](https://huggingface.co/papers/2611.08922)
- Code: [StanfordMIMI/Glyph](https://github.com/StanfordMIMI/Glyph)
- CheckPaper report: [checkpaper.app/r/4wfqdtv5ha](https://checkpaper.app/r/4wfqdtv5ha)

## Findings

1. **Glyph vs Phecodes p-values (p. 4 vs p. 38).** The introduction says Glyph associations reproduced more often than Phecodes at Internal Test "(69.3% vs. 49.1%, p = 9.77 × 10−4)" and External Site #1 "(74.3% vs. 63.9%, p = 2.93 × 10−3)". In the supplement, p = 9.77 × 10−4 and p = 1.95 × 10−3 belong to the Recent Phecode arm (47.2% and 59.9%), while 49.1% and 63.9% are the all-history arm, given without p-values. p = 2.93 × 10−3 appears only in the introduction.
2. **External Site #2 average (p. 8 vs Figure 2, p. 7).** The Results call R21 and R3 "well above the 33.8% cohort average at External Site #2". In Figure 2, 33.8% is the report-findings row (290 of 858); all tested associations at External Site #2 reproduce at 1,701 / 3,109 = 54.7%.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.08922v1, checks its hash, quotes the introduction, the supplement, the Results and Figure 2, and recomputes the rates.

## Status

[Asked the authors](https://github.com/StanfordMIMI/Glyph/issues/1) on 2026-11-20.

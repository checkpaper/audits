# Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable Time Series (arXiv:2611.12955): consistency checks

Sec. 4.2 says ConceptTime-Dynamic leads the interpretable methods by margins from 1.5 points upward, but Table 1 gives 0.74 at UCI-HAR 1% and 1.33 at 5% over TOTEM; and "EntroPE loses 4.5–8.5 points across benchmarks" covers only HAR and Epilepsy, while the full-label gaps are 3.03 on Sleep-EDF and 10.76 on UEA.

## Paper

- Title: Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable Time Series
- arXiv: [2611.12955v1](https://arxiv.org/abs/2611.12955v1) (the version checked, sha256 `83d07ccd…97ca`)
- Hugging Face: [papers/2611.12955](https://huggingface.co/papers/2611.12955)
- Code: [Sachithx/ConceptTime](https://github.com/Sachithx/ConceptTime)
- CheckPaper report: [checkpaper.app/r/m4azywy2fg](https://checkpaper.app/r/m4azywy2fg)

## Findings

1. **Margins over interpretable methods (Sec. 4.2, p. 7).** "margins ranging from 1.5 points (Epilepsy full-shot) to over 30 points". Sec. 4.1 lists the interpretable methods as catch22, ProSeNet, VQShape and TOTEM. In Table 1, ConceptTime-Dynamic leads TOTEM by 0.74 points at UCI-HAR 1% (74.60 vs 73.86) and 1.33 at 5% (79.60 vs 78.27), both below 1.5.
2. **EntroPE ablation (p. 7).** "Replacing DP segmentation with discrete categorical entropy (EntroPE) loses 4.5-8.5 points across benchmarks." The full-label gaps in Table 1 are 4.50 (HAR), 8.45 (Epilepsy), 3.03 (Sleep-EDF) and 10.76 (UEA); at Sleep-EDF 1% EntroPE is ahead, 70.95 vs 70.21.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12955v1, checks its hash, quotes Table 1 and Sec. 4.1–4.2, and recomputes the margins.

## Status

Answered. [Asked the authors](https://github.com/Sachithx/ConceptTime/issues/2) on 2026-11-21.

The first author replied on 2026-11-21: both ranges are illustrative comparisons, not bounds over every column. The 1.5 points is Epilepsy full-shot against ProSeNet (98.39 vs. 96.91) and the 30 points is UCI-HAR full-shot against catch22; the 4.5–8.5 points come from the full-shot UCI-HAR and Epilepsy columns against EntroPE. They agree that smaller margins exist at UCI-HAR 1% and 5%; the Table 1 results are unchanged.

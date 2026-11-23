# WorldDraft (arXiv:2611.16217): consistency checks

In Table 2, the WorldDraft-Primer and Text PE rows equal the base-model rows multiplied by a single factor across five or more unrelated metrics. The Primer ablation in Figure 12 shows the same factor.

## Paper

- Title: WorldDraft: If Code Builds the World, Can Video Models Just Render It?
- arXiv: [2611.16217v1](https://arxiv.org/abs/2611.16217v1) (the version checked, sha256 `d07e4fb3…205260c3`)
- Hugging Face: [papers/2611.16217](https://huggingface.co/papers/2611.16217)
- Code: [KevinHuge/WorldDraft](https://github.com/KevinHuge/WorldDraft) (benchmark and evaluation code; no WorldDraft-Primer or Text PE code or outputs)
- CheckPaper report: [checkpaper.app/r/rwmerf73dj](https://checkpaper.app/r/rwmerf73dj)

## Findings

Table 2 (p. 10), rows numbered from the top (1 LynnReal-Omni … 8 MiniMax-H3 + WorldDraft-Primer).

1. **MiniMax-H3 + WorldDraft-Primer (row 8) = MiniMax-H3 (row 6) × 1.050.** Realization 76.38 → 80.21, Quality 64.06 → 67.26, Persistence 70.32 → 73.84, Adherence 76.41 → 80.23, Retention 70.80 → 74.34; Leakage 28.64 → 27.21 (× 0.950). One factor k ∈ [1.0500, 1.0501] fits all six values within rounding.
2. **MiniMax-H3 + Text PE (row 7) = row 6 × 1.020** on the same five columns, and Leakage × 0.980 (k ∈ [1.0199, 1.0201]).
3. **OmniWeaving + WorldDraft-Primer (row 5) = OmniWeaving (row 3) × 1.067** on Quality, Persistence, Appearance, Binding and Retention, and Leakage × (2 − 1.067) (k ∈ [1.0671, 1.0672]).
4. **OmniWeaving + Text PE (row 4) = row 3 × 1.023** on the same columns, and Leakage × (2 − 1.023) (k ∈ [1.0231, 1.0233]).
5. **Figure 12 (App. C.2, p. 23), Primer ablation on MiniMax-H3.** The full-method bars equal the base-model bars × 1.050 on Global Count (28.59 → 30.02), Local Count (43.26 → 45.42), BBox IoU (15.91 → 16.70), RF (76.38 → 80.21) and AP (70.32 → 73.84), and SL × 0.950 (26.83 → 25.49). Bar labels are read from the figure image. The base SL here, 26.83, differs from MiniMax-H3 Leakage in Table 2, 28.64.

For comparison, among the 132 ordered pairs of different models in Table 1 (p. 8), at most 2 of the 5 columns Realization, Quality, Persistence, Adherence and Retention share one ratio within rounding. The metrics come from different pipelines (VLM question answering for Realization and Persistence, image-quality models for Quality), so independent measurements would not be expected to move by one common factor.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.16217v1, checks its hash, finds every quoted row and passage, computes the ratios and the common-factor intervals, and runs the Table 1 comparison.

## Status

[Asked the authors](https://github.com/KevinHuge/WorldDraft/issues/1) on 2026-11-23.

## Author response

None yet.

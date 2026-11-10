# MDMA-assisted therapy for severe PTSD (Nature Medicine 2021, MAPP1): consistency checks

Three effect-size statements in the MAPP1 phase 3 trial report (NCT03537014) that readers can check from the summary statistics printed in the paper.

## Paper

- Title: MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 study
- Authors: Mitchell, Bogenschutz, Lilienstein et al.
- Journal: Nature Medicine 27, 1025–1033 (2021), [doi:10.1038/s41591-021-01336-3](https://doi.org/10.1038/s41591-021-01336-3), open access
- File checked: the PDF from nature.com, sha256 `f412a0d6…8214`
- CheckPaper report: [checkpaper.app/r/8pn84efeb5](https://checkpaper.app/r/8pn84efeb5)

## Findings

All three are in Results, Efficacy (PDF p. 2).

1. **Within-group confidence intervals.** The within-group effect sizes are reported as 2.1 (95% CI −5.6 to 1.4) for MDMA and 1.2 (95% CI −4.9 to 2.5) for placebo. Each interval is centred on the negative of its estimate (midpoints −2.1 and −1.2), and the MDMA interval excludes its own estimate.
2. **CAPS-5 d = 0.91 is labelled de jure.** The paper gives d = 0.91 (95% CI 0.44 to 1.37, pooled s.d. 11.55) for the de jure estimand (n = 89). The completer means in the same paragraph, −24.4 (s.d. 11.6, n = 42) and −13.9 (s.d. 11.5, n = 37), reproduce all four numbers exactly. The primary result itself is robust; this concerns which population the effect size describes.
3. **SDS P value and confidence interval.** The secondary endpoint is reported as P = 0.0116 with effect size 0.43, 95% CI −0.01 to 0.88. An interval that includes zero corresponds to P ≈ 0.058. The completer means for SDS, −3.1 (s.d. 2.6) and −2.0 (s.d. 2.4), reproduce d = 0.44 with CI −0.01 to 0.89, which suggests the P value comes from the MMRM and the interval from the completers.

## Reproduce

```bash
pip install pymupdf
python verify.py
```

The script downloads the PDF from nature.com, checks its hash, finds each quoted number on p. 2, and recomputes the effect sizes and the implied P value.

## Status

Contacting the authors, started 2026-11-10.

## Author response

None yet.

# ReproBridge: Building Reproducibility into ML Research Artifacts (arXiv:2611.08452): consistency check

In the HELIX worked example, both refined-artifact MAE values equal the centre of their compatibility intervals, which by Eq. 1 is the mean of the five reference observations, to five decimals.

## Paper

- Title: ReproBridge: Building Reproducibility into ML Research Artifacts
- arXiv: [2611.08452v1](https://arxiv.org/abs/2611.08452v1) (the version checked, sha256 `abf9ad39…8abb`)
- Code: none linked
- CheckPaper report: [checkpaper.app/r/3cdzs77njc](https://checkpaper.app/r/3cdzs77njc)

## Findings

1. **New measurements equal the reference means.** Eq. 1 (p. 4) defines the compatibility interval as [x̄ − r, x̄ + r], centred on the mean x̄ of the five reference observations. App. D.5 (p. 34) reports that with the refined artifact the HELIX MAE becomes 0.12986 for T004 and 0.41160 for T006, with intervals [0.12524, 0.13448] and [0.38442, 0.43878]. The interval centres are 0.12986 and 0.41160, so both new runs reproduce the reference mean exactly. A new run of a stochastic training job landing on the five-run mean to five decimals, twice, is unlikely; the recorded values may be the reference means, or the intervals may have been built around the reported values.

This is a question for the authors, not a conclusion: the case record would settle it.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.08452v1, checks its hash, quotes Eq. 1 and the HELIX passage and prints each interval centre next to the reported value.

## Status

Emailed the authors on 2026-11-27 (Google authors, addresses from their earlier papers).

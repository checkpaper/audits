# InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure (arXiv:2611.11558): consistency checks

The experience-seeded Qwen3.5-9B run in the text matches none of the experience conditions in Table 5.

## Paper

- Title: InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure
- arXiv: [2611.11558v1](https://arxiv.org/abs/2611.11558v1) (the version checked, sha256 `d6f23500…45c2`)
- Hugging Face: [papers/2611.11558](https://huggingface.co/papers/2611.11558)
- Code: [TokenRhythm/InfraRSI](https://github.com/TokenRhythm/InfraRSI)
- CheckPaper report: [checkpaper.app/r/tywq7h36zq](https://checkpaper.app/r/tywq7h36zq)

## Findings

1. **First-trial and final speedup on Qwen3.5-9B (8×H100).** Section 4.1 (p. 8) says the experience-seeded first start reaches 1.55× on Trial 1 and search then reaches 1.73×; Section 6.1 (p. 13) gives the same 1.73×. Table 5 (p. 14) reports three experience conditions for this workload: cold start 1.22× (Trial 2) to 1.70×, all eligible packs 1.24× (Trial 1) to 1.70×, and cross-SKU transfer 1.23× (Trial 1) to 1.82×. Neither 1.55× nor 1.73× appears. Figure 4(a) also plots an "All packs" condition that Table 5 does not list.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.11558v1, checks its hash, and finds the quoted sentences and the three Table 5 rows.

## Status

Contacting the authors, started 2026-11-12. Asked in [the InfraRSI repository](https://github.com/TokenRhythm/InfraRSI/issues/1).

## Author response

None yet.

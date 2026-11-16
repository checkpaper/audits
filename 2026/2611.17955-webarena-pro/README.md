# WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark (arXiv:2611.17955): consistency checks

The failure count in Appendix C.1 does not match the success rates in Table 5.

## Paper

- Title: WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark
- arXiv: [2611.17955v1](https://arxiv.org/abs/2611.17955v1) (the version checked, sha256 `522f39f2…9d19`)
- Hugging Face: [papers/2611.17955](https://huggingface.co/papers/2611.17955)
- Code: [McGill-NLP/webarena-pro](https://github.com/McGill-NLP/webarena-pro)
- CheckPaper report: [checkpaper.app/r/45u9te2t9r](https://checkpaper.app/r/45u9te2t9r)

## Findings

1. **GenericAgent unsuccessful runs.** Appendix C.1 (p. 16) says that across the 2,400 Test runs of the eight GenericAgent models, 878 of the 1,683 unsuccessful runs reached the 50-step limit, which leaves 717 successes. The eight GenericAgent rows of Table 5 (p. 9), at 300 tasks each, give 15 + 39 + 47 + 67 + 91 + 71 + 91 + 76 = 497 successes, so 1,903 unsuccessful runs. Adding Table 9's Gemini 3.1 Pro (88/300), the ninth configuration in Figure 5, brings the total to 585, still short of 717. Table 13's Claude Opus 4.7 count (224 unsuccessful = 300 − 76) does agree with Table 5, and so do the coding-agent counts in Appendix C.2 (633 unsuccessful of 1,500).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.17955v1, checks its hash, reads the GenericAgent rows of Tables 5 and 9, and compares their success counts with Appendix C.1.

## Status

Contacting the authors, started 2026-11-17.

## Author response

None yet.

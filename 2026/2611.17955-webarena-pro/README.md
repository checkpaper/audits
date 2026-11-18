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

Confirmed by the authors on 2026-11-17 in [the WebArena-Pro repository](https://github.com/McGill-NLP/webarena-pro/issues/4). The C.1 numbers came from an earlier seven-model, 2,100-run analysis. Over the nine configurations in Figure 5 there are 2,700 runs and 585 successes, which matches the 585 computed here from Tables 5 and 9.

## Author response

From the first author (imenelydiaker), 2026-11-16 21:46 UTC:

> Thanks for catching this, you're right. The 1,683 failures and 878 step-limit hits (52.2%) came from an earlier seven-model, 2,100-run analysis. The published Figure 5 includes nine GenericAgent configurations, including non-omni Gemini 3.1 Pro from Table 9. Recomputing from its underlying trajectories gives 2,700 runs, 585 successes, and 2,115 failures, of which 1,154 reached the 50-step limit (54.6%).
>
> C.1 should therefore refer to nine configurations and 1,154 of 2,115 unsuccessful runs (54.6%). Sorry for the inconsistency, and thanks for the careful cross-check.

A maintainer (xhluca) closed the issue as completed on 2026-11-18.

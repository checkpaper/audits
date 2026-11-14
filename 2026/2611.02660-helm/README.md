# HeLM (arXiv:2611.02660): consistency checks

Three of the five HeLM strict-success values in Table 8 (A2 87.8, A4 66.7, A5 55.6) cannot come from the stated 5 trials per variant.

## Paper

- Title: HeLM: Hierarchical Explicit Language Memory for Non-Markovian Robot Manipulation
- arXiv: [2611.02660v1](https://arxiv.org/abs/2611.02660v1) (the version checked, sha256 `462b04e0…10a5ab`)
- Hugging Face: [papers/2611.02660](https://huggingface.co/papers/2611.02660)
- Code: [kimspacehuni/HeLM](https://github.com/kimspacehuni/HeLM)
- CheckPaper report: [checkpaper.app/r/rmx8bupzgn](https://checkpaper.app/r/rmx8bupzgn)

## Findings

1. **Table 8 versus trial counts.** The appendix (p. 22) evaluates each variant over 5 trials, and Appendix E.1 (p. 23) counts a trial as successful only if every subtask is done in order with proper termination. Table 6 (p. 17) gives 3, 6, 6, 4 and 6 variants for A1 to A5, so 15, 30, 30, 20 and 30 trials. HeLM's Table 8 values A2 87.8 (26/30 = 86.7, 27/30 = 90.0), A4 66.7 (13/20 = 65.0, 14/20 = 70.0) and A5 55.6 (16/30 = 53.3, 17/30 = 56.7) fit no count; 66.7 and 55.6 fit 18, 27 or 45 trials. A3 96.6 is 29/30 truncated. All Keyframe-HLP values fit. Averaging per variant first gives the same grid.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.02660v1, checks its hash, finds the quoted passages and values, and tests every Table 8 value against k/n for the stated n.

## Status

Contacting the authors, started 2026-11-15. Asked in [the HeLM repository](https://github.com/kimspacehuni/HeLM/issues/1).

## Author response

None yet.

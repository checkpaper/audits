# Auriga (arXiv:2611.01112): consistency checks

Appendix D counts 3,405 successful Auriga episodes on RoboDojo, while the success rates in Table 4 and the episode counts in Table 16 give about 3,478.

## Paper

- Title: Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation
- arXiv: [2611.01112v1](https://arxiv.org/abs/2611.01112v1) (the version checked, sha256 `c28cb24a…428ef3b`)
- Hugging Face: [papers/2611.01112](https://huggingface.co/papers/2611.01112)
- Code: [lose4578/Auriga](https://github.com/lose4578/Auriga)
- CheckPaper report: [checkpaper.app/r/5kpnmqghqg](https://checkpaper.app/r/5kpnmqghqg)

## Findings

1. **Successful episodes.** Sec. 6.1.1 (p. 16) defines SR over a fixed denominator. Table 4 (p. 18) gives Auriga SRs of 48.89, 38.50, 45.24, 92.99 and 63.08% for the five dimensions, and Table 16 (p. 41) gives 1,800, 1,200, 1,199, 900 and 1,200 episodes (6,299 in all). Together these give 880.0 + 462.0 + 542.4 + 836.9 + 757.0 = 3,478.3 successes (55.2%). Appendix D (p. 41) says 3,405 episodes were successful and 2,894 failed (54.1%), about 73 fewer.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.01112v1, checks its hash, finds the quoted passages and values, and recomputes the success count.

## Status

Contacting the authors, started 2026-11-16. Asked in [the Auriga repository](https://github.com/lose4578/Auriga/issues/3).

## Author response

None yet.

# EvoMemState: Evolving Memory State for Personal Agents (arXiv:2611.03743): consistency checks

One MemTrapBench average in Table 1 does not match its own scenario scores.

## Paper

- Title: EvoMemState: Evolving Memory State for Personal Agents
- arXiv: [2611.03743v1](https://arxiv.org/abs/2611.03743v1) (the version checked, sha256 `8d92f7dd…801a`)
- Hugging Face: [papers/2611.03743](https://huggingface.co/papers/2611.03743)
- Code: [XMUDeepLIT/EvoMemState](https://github.com/XMUDeepLIT/EvoMemState)
- CheckPaper report: [checkpaper.app/r/zdv5skcg4d](https://checkpaper.app/r/zdv5skcg4d)

## Findings

1. **MemTrapBench Avg. for EvoMemState with GPT-4o-mini.** In Table 1 (p. 6), the MemTrapBench Avg. equals the mean of the four scenario columns in 19 of 20 rows. The exception is EvoMemState with GPT-4o-mini: its scenarios are 73.9, 73.9, 88.8 and 90.4, which average 81.75, while the printed Avg. is 78.7. Its CogBias value repeats the Safety value next to it; a CogBias of 61.7 would give 78.7.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.03743v1, checks its hash, reads all 20 rows of Table 1, and compares each MemTrapBench Avg. with the mean of its four scenarios.

## Status

Not yet sent to the authors.

## Author response

None yet.

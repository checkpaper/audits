# Turns Matter: Advancing Streaming Video RL via Turn-Level Credit (TurnWise, arXiv:2611.06728): consistency check

In Table 1, 11 of the 12 StreamingBench Proactive accuracies are multiples of 0.4 (k/250). The exception is the method's own 3B row, 23.00.

## Paper

- Title: Turns Matter: Advancing Streaming Video RL via Turn-Level Credit
- arXiv: [2611.06728v1](https://arxiv.org/abs/2611.06728v1) (the version checked, sha256 `bccb1e9a…8042`)
- Hugging Face: [papers/2611.06728](https://huggingface.co/papers/2611.06728)
- Code: [XD111ds/turn-wise-rl](https://github.com/XD111ds/turn-wise-rl)
- CheckPaper report: [checkpaper.app/r/q8r5dvrdcf](https://checkpaper.app/r/q8r5dvrdcf)

## Findings

1. **StreamingBench Proactive (Table 1, p. 8).** The twelve Proactive accuracies are 22.40, 22.80, 20.40, 16.40, 20.40, **23.00** (Qwen2.5-VL-3B) and 32.80, 35.60, 30.40, 34.80, 32.80, 38.40 (Qwen3-VL-4B). All but 23.00 are exact multiples of 0.4, i.e. k/250 for the 250-question set. 23.00 would need 57.5 correct answers. It is the TurnWise row on the 3B backbone, which the table marks as the best StreamingBench average (49.43, the mean of 75.85 and 23.00).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.06728v1, checks its hash, parses Table 1 and tests each Proactive value.

## Status

[Asked the authors](https://github.com/XD111ds/turn-wise-rl/issues/1) on 2026-11-27.

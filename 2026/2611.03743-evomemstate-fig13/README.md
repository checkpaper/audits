# EvoMemState: Evolving Memory State for Personal Agents (arXiv:2611.03743): Figure 13 check

The six baseline bar pairs of Figure 13 are identical to those of Figure 3, but Figure 3 labels them without vs. with self-reflection and Figure 13 labels them with self-reflection vs. with reasoning state.

## Paper

- Title: EvoMemState: Evolving Memory State for Personal Agents
- arXiv: [2611.03743v1](https://arxiv.org/abs/2611.03743v1) (the version checked, sha256 `8d92f7dd…801a`)
- Hugging Face: [papers/2611.03743](https://huggingface.co/papers/2611.03743)
- Code: [XMUDeepLIT/EvoMemState](https://github.com/XMUDeepLIT/EvoMemState)
- CheckPaper report: [checkpaper.app/r/zdv5skcg4d](https://checkpaper.app/r/zdv5skcg4d)

## Findings

1. **Figure 13 versus Figure 3 (p. 23; p. 3).** Both figures show AMem 40.9 / 40.1, LightMem 71.4 / 71.8, Mem0 50.5 / 48.9, MemGPT 55.6 / 55.5, MemoryBank 55.6 / 55.7 and Supermemory 70.8 / 70.4, with the same arrow deltas. Figure 3 shows the effect of fixed self-reflection; Figure 13 labels the bars "Accuracy@complete w self-reflection" and "Accuracy@complete w/ reasoning state". The App. C.7 reading of reasoning-state effects therefore rests on numbers that Sec. 2.2 attributes to a different comparison.
2. **Average in Sec. 2.2 (p. 3).** The text says self-reflection "lowers average accuracy from 50.5% to 48.9%". Those are the Mem0 bars; the six-system mean goes from 57.47 to 57.07.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.03743v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

Not yet asked.

# AdProducer: Towards Agentic Advertising Video Generation (arXiv:2611.31466): consistency check

In Table 1, the overall PG-Score of all three Veo 3.1 baselines is higher than the count-weighted mean of their Recent, Long-tail and Evergreen scores, while the other eight rows match it.

## Paper

- Title: AdProducer: Towards Agentic Advertising Video Generation
- arXiv: [2611.31466v1](https://arxiv.org/abs/2611.31466v1) (the version checked, sha256 `eb5ef1a8…e06b`)
- Hugging Face: [papers/2611.31466](https://huggingface.co/papers/2611.31466)
- Code: [lky-ang/AdProducer](https://github.com/lky-ang/AdProducer)
- CheckPaper report: [checkpaper.app/r/3v7xz58q2f](https://checkpaper.app/r/3v7xz58q2f)

## Findings

1. **Veo overall scores.** AdCreation-Bench has 122 Recent, 130 Long-tail and 53 Evergreen briefs (Sec. 5.1). For eight rows of Table 1 (p. 7) the overall PG-Score equals (122·R + 130·L + 53·E) / 305 within rounding. The three Veo rows do not: Veo 3.1 gives 27.69 against 28.0 reported, Veo 3.1 Lite 27.54 against 27.8, and Veo 3.1 Fast 28.27 against 28.4. Rounding of the regime scores can move the weighted mean by at most 0.05.
2. **Time span.** The Fig. 5 caption (p. 5) says the benchmark spans 1836 to 2026; Sec. 5.1 (p. 6) gives Evergreen products as released from 1876 to 2022, and the figure's own timeline starts at 1876.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.31466v1, checks its hash, quotes every Table 1 row and recomputes the weighted overall score.

## Status

[Asked the authors](https://github.com/lky-ang/AdProducer/issues/2) on 2026-11-28.

# BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming Video (arXiv:2611.21553): consistency check

The WEB row of the human preference table does not add up to its printed total, and the authors' StreamingBench PO scores do not fit the 51-item split that the leaderboard baselines in the same table fit.

## Paper

- Title: BLIP-Live: Balancing Timeliness & Firing Precision in Proactive Streaming Video
- arXiv: [2611.21553v1](https://arxiv.org/abs/2611.21553v1) (the version checked, sha256 `060f1cc6…a0de`)
- Hugging Face: [papers/2611.21553](https://huggingface.co/papers/2611.21553)
- Code: [SalesforceAIResearch/BLIPLive](https://github.com/SalesforceAIResearch/BLIPLive)
- CheckPaper report: [checkpaper.app/r/8bg8tguvbj](https://checkpaper.app/r/8bg8tguvbj)

## Findings

1. **Table A.10, WEB split (p. 22).** The per-rater v2 counts (20, 20, 19, 20, 16, 17, 18, 20, 18, 18) sum to 186, not the printed 188. With the v1 counts, raters 5, 6 and 7 have 16, 21 and 21 judgements instead of 20, so the row holds 198 judgements rather than 10 × 20 = 200. The share from the printed cells is 186/198 = 93.94%, so the 94% headline is unchanged; the EGO row is consistent.
2. **Table 9, StreamingBench PO (p. 9).** The caption says PO follows the official leaderboard. Seven baseline scores are exact multiples of 1/51 (Gemini 1.5 Pro 45.10 = 23/51, GPT-4o 39.22 = 20/51, Claude 3.5 Sonnet 35.29 = 18/51, and others), but none of the four scores the authors ran (Gemma4-A4B 36.80, Qwen3.5-A3B 25.20, BLIP-Live-Gemma 44.00, BLIP-Live-Qwen 47.60) can be k/51. All four fit k/250. The authors' models therefore appear to be scored on a different item set or with a different scoring rule from the leaderboard rows they are ranked against.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.21553v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

Not yet sent.

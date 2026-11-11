# Axion 1.0 (arXiv:2611.03233): consistency check

The headline BioMysteryBench score of Axion 1.0-122B, 41.7%, does not fit the question count implied by every other BioMysteryBench score in the paper.

## Paper

- Title: Axion 1.0: Open Agent Foundation Models, Simplified
- arXiv: [2611.03233v2](https://arxiv.org/abs/2611.03233v2) (the version checked, sha256 `6704b242…f98c`; v1 has the same numbers)
- Hugging Face: [papers/2611.03233](https://huggingface.co/papers/2611.03233)
- Code: [bytedance/axion1_0](https://github.com/bytedance/axion1_0)
- CheckPaper report: [checkpaper.app/r/f5xg5ds2gf](https://checkpaper.app/r/f5xg5ds2gf)

## Findings

1. **BioMysteryBench 41.7%.** Tables 1 to 3 (pp. 9 to 11) give 16 BioMysteryBench (human-difficult) scores evaluated by the Axion team, including GPT-5.6 Sol and Gemini 3.1 Pro. Thirteen are exact multiples of 1/17, for example 35.3 = 6/17 and 47.1 = 8/17. The three that are not are the same number, 41.7% for Axion 1.0-122B, which is also quoted in the text (pp. 8 and 9) and the repository README. On a 17-question set the nearest scores are 7/17 = 41.2% and 8/17 = 47.1%. Section 4.1 reports the best single run, so every score should be a whole number of questions.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.03233v2, checks its hash, reads the BioMysteryBench column of Tables 1 to 3, and tests each score against k/17.

## Status

Contacting the authors, started 2026-11-11. Asked in [bytedance/axion1_0#5](https://github.com/bytedance/axion1_0/issues/5).

## Author response

None yet.

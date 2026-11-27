# Coding4Games: Can Modern Coding Agents Play Modern Video Games? (arXiv:2611.31974): consistency check

The DeepSeek-V4.1-Flash row of Table 4 sums to 90.0% across the five grounding levels, and Table 1 lists the benchmark's execution mode as Live while its caption says execution is stepped throughout.

## Paper

- Title: Coding4Games: Can Modern Coding Agents Play Modern Video Games?
- arXiv: [2611.31974v1](https://arxiv.org/abs/2611.31974v1) (the version checked, sha256 `158def23…ffe4`)
- Hugging Face: [papers/2611.31974](https://huggingface.co/papers/2611.31974)
- Code: [GVCLab/Coding4Games](https://github.com/GVCLab/Coding4Games)
- CheckPaper report: [checkpaper.app/r/dstjz87aj8](https://checkpaper.app/r/dstjz87aj8)

## Findings

1. **A Table 4 row that does not sum to 100.** G0–G4 are "the percentage of final programs at each grounding level" (p. 7). Eleven rows sum to 100.0 ± 0.1. The deepseek-v4.1-flash row (0.0, 0.0, 10.0, 50.0, 30.0) sums to 90.0, so one of its cells is missing 10 points. Its G3/G4 values equal those of Qwen3.8-27B (50.0, 30.0), which has G2 = 20.0.
2. **Mode in Table 1.** The caption describes "stepped execution throughout development and evaluation", and the agent loop in Sec. 3 pauses the game between actions, but the Coding4Games row lists Mode as Live.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.31974v1, checks its hash, quotes every Table 4 row and sums G0–G4.

## Status

[Asked the authors](https://github.com/GVCLab/Coding4Games/issues/1) on 2026-11-28.

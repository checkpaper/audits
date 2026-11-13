# WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning (arXiv:2611.12527): consistency checks

Table 10 gives the 0.6B model an input width that 16 heads cannot divide, the nMOS intervals in Table 3 are too wide for the stated number of ratings, and the text calls a 29% WER gap slight.

## Paper

- Title: WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning
- arXiv: [2611.12527v1](https://arxiv.org/abs/2611.12527v1) (the version checked, sha256 `74738e45…faae`)
- Hugging Face: [papers/2611.12527](https://huggingface.co/papers/2611.12527)
- Code: [sh-lee-prml/WaveGen](https://github.com/sh-lee-prml/WaveGen)
- CheckPaper report: [checkpaper.app/r/gght689r9s](https://checkpaper.app/r/gght689r9s)

## Findings

1. **Table 10 dimensions.** WaveGen (0.6B) has DiT input dim 1158, hidden dim 4632 (= 4 × 1158) and 16 heads (p. 17). 1158 / 16 = 72.375. The other two models divide evenly (768 / 12 = 64, 1024 / 16 = 64), so 1152 and 4608 may be meant.
2. **nMOS intervals.** The appendix (p. 19) says 20 raters each rated 100 samples per model, 2,000 ratings. As a 95% interval over 2,000 ratings, nMOS ±0.112 to ±0.129 needs a rating SD of 2.56 to 2.94, above the maximum of 2.00 on a 1 to 5 scale; sMOS ±0.037 implies 0.84. Either ± means something else for nMOS, or at most 1,225 ratings remained after the exclusions.
3. **v-prediction.** Section 4.6 (p. 7) says v-prediction gives "slightly better" alignment. In Table 7 with Spectral Forcing its WER is 3.93 against 5.57 for x-prediction, 29.4% lower, and lower than the final x-prediction model's 4.96 (Table 8).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12527v1, checks its hash, finds the quoted passages and table values, and recomputes the head width and the SD implied by each interval.

## Status

Contacting the authors, started 2026-11-14. Asked in [the WaveGen repository](https://github.com/sh-lee-prml/WaveGen/issues/2).

## Author response

None yet.

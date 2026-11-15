# Multi-layer Indexer (arXiv:2611.03768): consistency checks

Appendix J gives equal-retention speed gaps of 4.70, 2.36, 4.12 and 2.61 points, while Table 9 gives 9.6, 5.7, 6.0 and 3.7 points for the same cells.

## Paper

- Title: Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse Attention
- arXiv: [2611.03768v1](https://arxiv.org/abs/2611.03768v1) (the version checked, sha256 `1d9d589f…ca89aa52b`)
- Hugging Face: [papers/2611.03768](https://huggingface.co/papers/2611.03768)
- Code: [ArjunKrishnak/dsa-multi-layer-indexer](https://github.com/ArjunKrishnak/dsa-multi-layer-indexer)
- CheckPaper report: [checkpaper.app/r/uy6trywbxz](https://checkpaper.app/r/uy6trywbxz)

## Findings

1. **Equal-retention gaps.** Appendix J (p. 18) says the equal-retention gaps carry 95% intervals of about ±0.1 point: DeepSeek-V3.2 at 128K, 1/4 +4.70 and 1/8 +2.36; GLM-5 at 195K, 1/4 +4.12 and 1/8 +2.61. It adds that replicate cells differ from sweep cells by up to 0.5 (DeepSeek) and 0.2 (GLM) points on these gaps. Table 9 (p. 17) gives IndexCache and IndexCache+MLI decode gains of +22.7 / +32.3 and +28.0 / +33.7 for DeepSeek, and +17.7 / +23.7 and +21.3 / +25.0 for GLM, so gaps of 9.6, 5.7, 6.0 and 3.7 points. These differ from Appendix J by 4.9, 3.3, 1.9 and 1.1 points. GLM uses the same deferred-stream realization in both places (p. 6). As ratios of throughput the gaps are 7.8, 4.5, 5.1 and 3.0%, which do not match either.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.03768v1, checks its hash, finds the quoted passages and values, and recomputes the four gaps.

## Status

Contacting the authors, started 2026-11-16. Asked in [the MLI repository](https://github.com/ArjunKrishnak/dsa-multi-layer-indexer/issues/1).

## Author response

None yet.

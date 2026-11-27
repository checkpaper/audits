# Plan4D: Generative Plannable 4D Worlds (arXiv:2611.26516): consistency check

In Table 8, Plan4D's depth, reconstruction and camera metrics on RLBench and PointOdyssey agree to within 0.0002 on all seven columns, while the video-quality metrics of the same two rows differ by up to 0.117.

## Paper

- Title: Plan4D: Generative Plannable 4D Worlds
- arXiv: [2611.26516v1](https://arxiv.org/abs/2611.26516v1) (the version checked, sha256 `ed9fe42a…57d3`)
- Hugging Face: [papers/2611.26516](https://huggingface.co/papers/2611.26516)
- Code: [AMAP-ML/plan4d](https://github.com/AMAP-ML/plan4d)
- CheckPaper report: [checkpaper.app/r/7ad9w2zgjd](https://checkpaper.app/r/7ad9w2zgjd)

## Findings

1. **Two benchmarks, one set of geometry numbers.** Table 8 (p. 32) gives Plan4D ("Ours") on PointOdyssey as AbsRel .0822, δ1 .9215, δ2 .9720, Chamfer-L1 .3013, RPE-R .1985, RRA@10 .9965, RRA@5 .9864, and on RLBench as .0822, .9215, .9721, .3012, .1985, .9963, .9864. The largest difference is 0.0002. The video metrics of the same rows differ clearly (IQ .5941 vs .4767, SC .9233 vs .8459), so the two rows are not one run listed twice. RLBench is a robot-manipulation benchmark and PointOdyssey a synthetic long-trajectory benchmark, so matching geometry to four decimals is unexpected.
2. **TesserAct Chamfer-L1** is also exactly .3904 on both PointOdyssey and RLBench in the same table.

These are questions for the authors, not conclusions: a copied evaluation output or a shared ground-truth path would produce the pattern, and so could something we have not thought of.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.26516v1, checks its hash, quotes the two Table 8 rows and prints the column-by-column differences.

## Status

[Asked the authors](https://github.com/AMAP-ML/plan4d/issues/1) on 2026-11-27.

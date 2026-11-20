# TorchCurves: Differentiable Parametric Curves (arXiv:2611.14516): consistency checks

The B-spline coefficient count is given as P = |knots| − degree + 1 and the number of non-zero basis functions as degree + 2; the standard identities, recomputed in the script, are |knots| − degree − 1 and degree + 1. The KAN benchmark is [16, W, W, 1] in the text and [32, W, W, 1] in the Figure 4 caption.

## Paper

- Title: TorchCurves: Differentiable Parametric Curves
- arXiv: [2611.14516v1](https://arxiv.org/abs/2611.14516v1) (the version checked, sha256 `c51b7c23…1167`)
- Hugging Face: [papers/2611.14516](https://huggingface.co/papers/2611.14516)
- Code: [alexshtf/torchcurves](https://github.com/alexshtf/torchcurves)
- CheckPaper report: [checkpaper.app/r/g8pe42sey4](https://checkpaper.app/r/g8pe42sey4)

## Findings

1. **Coefficient count (Sec. 3.1, p. 4).** "P = |knots|−degree+1". For a clamped knot vector the script finds P = |knots| − degree − 1 for degrees 1–5 (e.g. degree 3, 17 knots: 13 coefficients; the paper's formula gives 15).
2. **Non-zero basis functions (Sec. 4, p. 6).** "only degree+2 basis functions are non-zero". The Cox–de Boor recursion in the script gives at most degree + 1 non-zero functions at any point.
3. **KAN architecture (p. 7 vs p. 10).** Sec. 5 says "[16, W, W, 1], meaning, 16 input features"; the Figure 4 caption says "[32, W, W, 1] cubic KANs".

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.14516v1, checks its hash, quotes the passages and tables above, and recomputes the numbers.

## Status

Not yet asked.

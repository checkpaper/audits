# Breath-Dx: A Time Series Classification Benchmark for Disease Screening (arXiv:2611.15348): consistency checks

The 0.05–0.12 AUC drop stated in the abstract is larger than any drop in Table V, and A15 is not within 0.45–0.55 for most methods in Table III.

## Paper

- Title: Breath-Dx: A Time Series Classification Benchmark for Disease Screening
- arXiv: [2611.15348v1](https://arxiv.org/abs/2611.15348v1) (the version checked, sha256 `fbe0a8e8…f19b`)
- Hugging Face: [papers/2611.15348](https://huggingface.co/papers/2611.15348)
- Code: [ivanpodd/Breath-Dx](https://github.com/ivanpodd/Breath-Dx)
- CheckPaper report: [checkpaper.app/r/k8n8hktf7f](https://checkpaper.app/r/k8n8hktf7f)

## Findings

1. **Temporal-validation drop.** The abstract (p. 1), the contributions (p. 2) and Sec. VI-B (p. 8) give a 0.05–0.12 AUC drop from random to temporal splits, and Sec. VI-B calls it the average across all diseases and methods. Table V (p. 8), the only random-versus-temporal comparison in the paper, has four pairs with drops of 0.066 (C34), 0.053 (B18), 0.064 (J44) and 0.074 (Z00): largest 0.074, mean 0.064.
2. **A15 near chance.** Sec. VI-A (p. 6) says A15 stays in the AUC range 0.45–0.55 across all methods. In Table III (p. 7), 10 of 19 rows are outside that range for A15, including logistic regression at 0.688 and HGBoost + LogFit 4 at 0.600.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.15348v1, checks its hash, quotes the abstract, Sec. VI and Tables III and V, and recomputes the drops and the A15 range.

## Status

[Asked the authors](https://github.com/ivanpodd/Breath-Dx/issues/1) on 2026-11-19.

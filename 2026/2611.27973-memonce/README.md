# MemOnce: A Scalable Memory Architecture for Large Language Models (arXiv:2611.27973): consistency check

The claim that MemOnce r = 1 and r = 8 rank first and second among all evaluated architectures does not hold against the paper's own full 400M table, and one average in the scaling table does not follow from its task values.

## Paper

- Title: MemOnce: A Scalable Memory Architecture for Large Language Models
- arXiv: [2611.27973v1](https://arxiv.org/abs/2611.27973v1) (the version checked, sha256 `c20be4e8…6c81`)
- Hugging Face: [papers/2611.27973](https://huggingface.co/papers/2611.27973)
- Code: [Clare-Nie/MemOnce](https://github.com/Clare-Nie/MemOnce)
- CheckPaper report: [checkpaper.app/r/jzbr2ycycx](https://checkpaper.app/r/jzbr2ycycx)

## Findings

1. **"Highest and second-highest" (p. 8) versus the full 400M table (p. 26).** Sec. 5 says MemOnce r = 1 and r = 8 attain the highest and second-highest average zero-shot accuracy across all evaluated architectures, and Table 2 shows r = 8 at 52.35. The full table on p. 26 also lists Kimi-Linear (315M) with Avg 0.5250, above r = 8 (0.5235); its eight task values average to 0.5251. Kimi-Linear is not a row of Table 2.
2. **Scaling table, ~600M MemOnce r = 8 (p. 24).** The eight task values (0.680, 0.437, 0.527, 0.546, 0.299, 0.848, 0.597, 0.355) average to 0.5361, but the row prints 0.5392. Rounding of the inputs allows at most 0.0005. The r = 1 row next to it is consistent (0.5409).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.27973v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

[Asked the authors](https://github.com/Clare-Nie/MemOnce/issues/2) on 2026-11-27.

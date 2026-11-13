# LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression (arXiv:2611.07025): consistency checks

The LowRAM-EQ rows of Table 3 come from a lower-compression setting of Table 10 than every other row.

## Paper

- Title: LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression
- arXiv: [2611.07025v1](https://arxiv.org/abs/2611.07025v1) (the version checked, sha256 `f9c11993…2f77`)
- Hugging Face: [papers/2611.07025](https://huggingface.co/papers/2611.07025)
- Code: [lowram-model/lowram](https://github.com/lowram-model/lowram)
- CheckPaper report: [checkpaper.app/r/ntrkrszzev](https://checkpaper.app/r/ntrkrszzev)

## Findings

1. **Table 3 versus Table 10.** Table 10 (p. 23) is the sweep behind Table 3 (p. 8), with three settings per method. For LowRAM, LowRAM-E and LowRAM-Q, every Table 3 cell is the highest-compression setting. The LowRAM-EQ cells are not: Mistral RULER 6.7× 93.6 and both Llama cells (6.7× 96.4, 8.8× 91.3) are the middle setting. At the highest setting LowRAM-EQ scores Mistral RULER 8.7× 89.1, Llama RULER 8.8× 82.7 and Llama LongBench 10.2× 89.4. Mistral LongBench (10.7× 96.9) is the highest setting.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.07025v1, checks its hash, finds every Table 3 and Table 10 row, and matches each Table 3 cell to its Table 10 setting.

## Status

Contacting the authors, started 2026-11-14. Asked in [the lowram repository](https://github.com/lowram-model/lowram/issues/2).

## Author response

None yet.

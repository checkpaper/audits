# Going Deeper With Memories (arXiv:2611.05255): throughput check

In Table 3 and Table A.1, each DEEPMEM throughput value equals the DEEPMEM (NR) value minus a whole multiple of 1,000, so the last three digits agree in all three columns.

## Paper

- Title: Going Deeper With Memories
- arXiv: [2611.05255v1](https://arxiv.org/abs/2611.05255v1) (the version checked, sha256 `b0dd64ea…1aaf`)
- Hugging Face: [papers/2611.05255](https://huggingface.co/papers/2611.05255)
- Code: [akhadangi/deepmem](https://github.com/akhadangi/deepmem)
- CheckPaper report: [checkpaper.app/r/4fdtwbjjbr](https://checkpaper.app/r/4fdtwbjjbr)

## Findings

1. **Throughput rows (Table 3, p. 9; Table A.1, p. 13).** DEEPMEM (NR) is 137,963 / 136,905 / 139,287 B/s on FineWeb-Edu / PG19 / Stack-smol, and DEEPMEM is 118,963 / 120,905 / 119,287. The differences are exactly 19,000, 16,000 and 20,000. The two variants differ by the shared-state refinement step, and App. A.1 summarises the change as "decreases from approximately 138,052 to 119,718 bytes/s". Independent timing runs would not usually agree in their last three digits in all three columns. Raw timing logs would settle it.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.05255v1, checks its hash, quotes the passages above and recomputes the numbers.

## Status

Not yet asked.

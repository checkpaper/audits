# Going Deeper With Memories (arXiv:2611.05255): consistency checks

Sec. 3.1 and Table 1 report three seeds per model, while App. A.2 says only one training run is available for the same configurations.

## Paper

- Title: Going Deeper With Memories
- arXiv: [2611.05255v1](https://arxiv.org/abs/2611.05255v1) (the version checked, sha256 `b0dd64ea…1aaf`)
- Hugging Face: [papers/2611.05255](https://huggingface.co/papers/2611.05255)
- Code: [akhadangi/deepmem](https://github.com/akhadangi/deepmem)
- CheckPaper report: [checkpaper.app/r/4fdtwbjjbr](https://checkpaper.app/r/4fdtwbjjbr)

## Findings

1. **Seeds versus single runs.** Sec. 3.1 (p. 6) says all runs use three random seeds per model. Table 1 (p. 8) reports FLORES BPB for DEEPMEM as 1.9694 ± 0.020 and for DEEPMEM (NR) as 1.9758 ± 0.017. Table A.2 (p. 14) lists the same two configurations with the same macro values, 1.9694 and 1.9758, and App. A.2 then says the comparisons are exploratory because only one training run is available for each configuration. Both statements cannot hold for these two rows.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.05255v1, checks its hash, and quotes Sec. 3.1, Table 1, Table A.2 and App. A.2.

## Status

Not yet reported.

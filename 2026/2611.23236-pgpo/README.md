# PGPO: Prototype-Guided Progressive Obfuscation for Privacy-Preserving LLM-Enhanced Recommendation (arXiv:2611.23236): consistency check

Sec. 5.2 says every obfuscation method cuts embedding-inversion success "by over 50%" against the raw descriptions, but in Table 4 on Amazon-Book InferDPT and PGPO itself cut Precision, Recall, F1 (and, for InferDPT, Jaccard) by 48–49%.

## Paper

- Title: PGPO: Prototype-Guided Progressive Obfuscation for Privacy-Preserving LLM-Enhanced Recommendation
- arXiv: [2611.23236v1](https://arxiv.org/abs/2611.23236v1) (the version checked, sha256 `431c56c7…3b0e`)
- Hugging Face: [papers/2611.23236](https://huggingface.co/papers/2611.23236)
- Code: [Shengxiang-Lin/PGPO](https://github.com/Shengxiang-Lin/PGPO)
- CheckPaper report: [checkpaper.app/r/z4gv3e5ywx](https://checkpaper.app/r/z4gv3e5ywx)

## Findings

1. **"By over 50%" (Sec. 5.2 (iii), p. 8).** "Table 4 reports that all obfuscation methods cut attack success rates by over 50% relative to the raw Description baseline." On Amazon-Book the Description row has Precision 0.1829, Recall 0.1836, F1 0.1832 and Jaccard 0.1551. InferDPT reaches 0.0950 / 0.0955 / 0.0952 / 0.0795 (cuts of 48.1 / 48.0 / 48.0 / 48.7%), and PGPO reaches 0.0925 / 0.0933 / 0.0928 for the first three (49.4 / 49.2 / 49.3%). All MovieLens-1M cells are cut by more than 50%.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.23236v1, checks its hash, quotes Sec. 5.2 and Table 4, and lists every cell cut by 50% or less.

## Status

[Asked the authors](https://github.com/Shengxiang-Lin/PGPO/issues/12) on 2026-11-22.

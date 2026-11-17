# SIMIT: Self-Improving Vision-Language Models via Imagination at Test-Time (arXiv:2611.00053): consistency checks

The MM-Bench (EN) scores fit a 132-question count, not the 500 evaluation examples stated in Table 4.

## Paper

- Title: SIMIT: Self-Improving Vision-Language Models via Imagination at Test-Time
- arXiv: [2611.00053v1](https://arxiv.org/abs/2611.00053v1) (the version checked, sha256 `8e298376…2506`)
- Hugging Face: [papers/2611.00053](https://huggingface.co/papers/2611.00053)
- Code: [monurcan/simit_paper](https://github.com/monurcan/simit_paper)
- CheckPaper report: [checkpaper.app/r/e4dt6f6haz](https://checkpaper.app/r/e4dt6f6haz)

## Findings

1. **MM-Bench (EN) sample size.** Table 4 (p. 16) gives 500 evaluation examples for every benchmark, and the text says MMBench is scored by multiple-choice accuracy, so each score should be k/500, a multiple of 0.2. MM-Bench (EN) 84.1 (BAGEL-7B zero-shot, Tables 8 and 9) and 58.3 (Lance-3B zero-shot, Table 9) are not. All seven distinct MM-Bench (EN) values (84.1, 86.4, 85.6, 88.6, 89.4, 58.3, 65.2) fit k/132 exactly, for example 84.1 = 111/132 and 58.3 = 77/132. The other accuracy-scored benchmarks in the same tables (GQA, AI2D, ChartQA, MM-Bench (CN), SEED-Bench) all fit k/500.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.00053v1, checks its hash, reads the accuracy rows of Tables 8 and 9, and tests each score against k/500 and k/132.

## Status

Contacting the authors, started 2026-11-17.

## Author response

None yet.

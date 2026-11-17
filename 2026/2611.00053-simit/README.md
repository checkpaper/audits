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

Confirmed by the authors on 2026-11-17 in [the SIMIT repository](https://github.com/monurcan/simit_paper/issues/1). MM-Bench (EN) is effectively scored on 132 questions. The cause is the standard lmms-eval mmbench_en_dev_lite task: its CircularEval scorer counts only the 132 original-order rows of the 500-row Lite split. All methods were scored the same way. The authors will state the effective count in Table 4 and report the issue to the lmms-eval maintainers. MM-Bench (CN) values also all fit k/125, so that split may be affected in the same way.

## Author response

From monurcan, 2026-11-17 03:36 UTC:

> Thank you for the careful check. You are right: MM-Bench (EN) is effectively scored on 132 questions.
>
> This comes from the standard lmms-eval mmbench_en_dev_lite task, which we used unmodified. The full MMBench dev set stores each question in its original option order (index < 1e6) plus rotated copies with shuffled options (index + k·1e6). lmms-eval's CircularEval scorer iterates over the original-order rows and counts a question correct only if all of its rotations are correct. LMMs-Eval-Lite selects 500 rows by embedding-based k-center, which in practice keeps at most one copy of each question: the split contains 500 distinct questions, 132 of them in original order and 368 as rotated copies. Because the full-set scorer is reused unchanged, only the 132 original-order rows are scored, each once, and the rotated rows are run but not counted. The LMMs-Eval paper (arXiv:2407.12772, Table 7) also lists this split as 500 samples, and neither it nor the task config notes that only the original-order rows are scored, so we reported the documented size.
>
> This does not change the paper's findings. The behavior is a property of the shared evaluation harness, not of our method: every method and baseline, including the zero-shot models, was scored with the same task and the same scorer on the same 132 questions, so all MM-Bench (EN) comparisons are like-for-like. MM-Bench (EN) is one of the benchmarks in our suite, and our conclusions rest on consistent gains across the full suite, not on this one row. The one real consequence is that this row rests on a smaller sample and so carries more variance than the others, and readers should know that.
>
> We will state the effective count and its cause in the dataset statistics appendix (Table 4), and we will report the issue to the lmms-eval maintainers. Thanks again for flagging this.

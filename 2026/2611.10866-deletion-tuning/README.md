# The Surprising Effectiveness of Deleting Weights in LLM Post-Training (arXiv:2611.10866): consistency check

Evaluation is greedy, so each accuracy should be k / n on its benchmark. Eight Llama GSM8K accuracies in Table 1 are not k / 1319, and 17 of 18 OlympiadBench accuracies in Table 8 are not k / 675, while the other benchmark columns fit their sizes exactly.

## Paper

- Title: The Surprising Effectiveness of Deleting Weights in LLM Post-Training
- arXiv: [2611.10866v1](https://arxiv.org/abs/2611.10866v1) (the version checked, sha256 `7611c500…5a04`)
- Hugging Face: [papers/2611.10866](https://huggingface.co/papers/2611.10866)
- Code: [agentic-learning-ai-lab/deleting-weights](https://github.com/agentic-learning-ai-lab/deleting-weights)
- CheckPaper report: [checkpaper.app/r/8j6rrze9se](https://checkpaper.app/r/8j6rrze9se)

## Findings

1. **Table 1, Llama on GSM8K (p. 7).** Sec. 4 (p. 6) says evaluation uses greedy decoding. All seven Llama1B cells and the Base and FFT cells at 3B and 8B are k / 1319, the GSM8K test size. Eight are not: LoRA r=1 82.39 (3B) and 83.38 (8B), LoRA r=4 82.44 (3B), MTH 99% 80.53 (3B) and 83.31 (8B), MTH 99.95% 82.17 (3B) and 83.07 (8B), and Deletion Tuning 81.49 (3B). No single n in 1000–3000 fits all eight.
2. **Table 8, OlympiadBench (p. 18).** Only 1 of the 18 values (25.78) is k / 675, the size of the SimpleRL-Zoo OlympiadBench set, and no n between 50 and 3000 fits all 18. In the same table, GSM8K (k / 1319) and Minerva Math (k / 272) fit 18 of 18.

The paper does not state the OlympiadBench size, and an aggregation it does not describe (for example a mean over shards or repeated runs) could explain both.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.10866v1, checks its hash, quotes the protocol and the table rows, and tests each accuracy against the k / n grid.

## Status

[Asked the authors](https://github.com/agentic-learning-ai-lab/deleting-weights/issues/4) on 2026-11-28.

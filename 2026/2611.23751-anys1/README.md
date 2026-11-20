# Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow (arXiv:2611.23751): consistency checks

Random delegation raises System-2 disagreements "more than fourfold" only on ALFWorld (Table 5 gives 1.18× and 1.92× on SOPBench and WebShop), and Table 4 bolds System-1's 83.8 as the Dev best while zero-shot Qwen3.5-27B has 85.9.

## Paper

- Title: Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow
- arXiv: [2611.23751v1](https://arxiv.org/abs/2611.23751v1) (the version checked, sha256 `40ba052a…dc90`)
- Hugging Face: [papers/2611.23751](https://huggingface.co/papers/2611.23751)
- Code: [middle-chunjie/AnyS1](https://github.com/middle-chunjie/AnyS1)
- CheckPaper report: [checkpaper.app/r/h5jecgu92n](https://checkpaper.app/r/h5jecgu92n)

## Findings

1. **"More than fourfold" (Sec. 4.3, p. 7 vs Table 5, p. 15).** The text says equal-rate random delegation "multiplies System-2 disagreements more than fourfold". Table 5 gives disagreements per 100 decisions for the gate vs random: SOPBench 7.1 vs 8.4 (1.18×), ALFWorld 3.8 vs 16.0 (4.21×), WebShop 6.5 vs 12.5 (1.92×). Only ALFWorld exceeds fourfold.
2. **Table 4 bold (p. 15).** The caption says "Bold: column best." In the Dev column, 83.8 (System-1) is set bold, while zero-shot Qwen3.5-27B has 85.9 in regular weight. The script reads the font of each cell.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.23751v1, checks its hash, quotes the passages and tables above, and recomputes the numbers.

## Status

Not yet asked.

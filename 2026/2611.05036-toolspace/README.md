# ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents (arXiv:2611.05036): consistency checks

The headline 38.2-point drop comes from a model row that is not in the figure the text cites.

## Paper

- Title: ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents
- arXiv: [2611.05036v1](https://arxiv.org/abs/2611.05036v1) (the version checked, sha256 `697822d5…20bb`)
- Hugging Face: [papers/2611.05036](https://huggingface.co/papers/2611.05036)
- Code: [dongguanting/ToolSpace](https://github.com/dongguanting/ToolSpace)
- CheckPaper report: [checkpaper.app/r/2weqs6waqg](https://checkpaper.app/r/2weqs6waqg)

## Findings

1. **The 38.2-point drop.** The abstract and Section 1 (p. 3) say seven frontier models drop by up to 38.2 points on AutomationBench Pro, citing Figure 1. The 38.2 comes from the Table 2 row DeepSeek-V4.1-Flash-1017 (60.5 to 22.3, p. 13). Figure 1(d) shows six AutomationBench Pro scores, and 22.3 is not among them. The paper does not say what the -1017 variant is. Without that row the largest drop is 34.8, over six models.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.05036v1, checks its hash, and compares the Table 2 rows with the Figure 1(d) values.

## Status

Contacting the authors, started 2026-11-12. Asked in [the ToolSpace repository](https://github.com/dongguanting/ToolSpace/issues/4).

## Author response

None yet.

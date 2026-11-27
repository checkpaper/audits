# ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents (arXiv:2611.31198): consistency check

The paper says every reported number is the mean of three independent runs. Four accuracies in Tables 2 and 3 cannot be such a mean on the sample counts of Table 8. Separately, the 8B model improves on seven of the ten OOD benchmarks, not eight.

## Paper

- Title: ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents
- arXiv: [2611.31198v1](https://arxiv.org/abs/2611.31198v1) (the version checked, sha256 `774b679c…f20b`)
- Hugging Face: [papers/2611.31198](https://huggingface.co/papers/2611.31198)
- Code: [uclanlp/OpenVLHarness](https://github.com/uclanlp/OpenVLHarness)
- CheckPaper report: [checkpaper.app/r/48wccahu4w](https://checkpaper.app/r/48wccahu4w)

## Findings

1. **Three-run means.** Sec. 4.4 (p. 6): "every reported number is the mean of three independent runs." A mean of three runs over n items is k / (3n) for an integer k. These cells are not on that grid, and stay off it if each run's accuracy is rounded to two decimals before averaging:

   | Cell | Reported | n (Table 8) | Nearest three-run means |
   |---|---|---|---|
   | Table 2, Qwen3-VL-32B + ToolSmith, InfoSeek | 56.99 | 2000 | 56.98, 57.00 |
   | Table 2, GPT-5 + ToolSmith, InfoSeek | 53.04 | 2000 | 53.03, 53.05 |
   | Table 3, Qwen3-VL-8B base tools, MM-BC | 6.00 | 243 | 5.90, 6.04 |
   | Table 3, Qwen3-VL-8B + ToolSmith, VisBrowse | 11.22 | 169 | 11.05, 11.24 |

   Items dropped in some runs (errors, refusals) would change the denominators and could explain this.

2. **8B OOD gains.** Sec. 5 (p. 6) says the 8B model "improves on eight of the ten, with the remaining two essentially flat." The 8B Δ row of Table 3 (p. 7) has seven positive values; HLE-VL is 0.00, RealX-Bench −0.17 and VisBrowse −0.02.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.31198v1, checks its hash, quotes the claim, the Table 8 counts and the table rows, and searches for three-run means that round to each reported value.

## Status

[Asked the authors](https://github.com/uclanlp/OpenVLHarness/issues/9) on 2026-11-28.

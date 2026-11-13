# Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished Tasks? (arXiv:2611.02017): consistency checks

The workload ratios in Section 4.3 match an earlier, commented-out Table 2 in the LaTeX source, not the printed one.

## Paper

- Title: Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished Tasks?
- arXiv: [2611.02017v1](https://arxiv.org/abs/2611.02017v1) (the version checked, sha256 `1671456f…787c`; source `6129a68a…7adc`)
- Hugging Face: [papers/2611.02017](https://huggingface.co/papers/2611.02017)
- Code: [Miraclecsc/Switch-SWE](https://github.com/Miraclecsc/Switch-SWE)
- CheckPaper report: [checkpaper.app/r/f7kjd7gvug](https://checkpaper.app/r/f7kjd7gvug)

## Findings

1. **Section 4.3 versus Table 2.** Section 4.3 (p. 8) says full switched sessions use 4.5 to 11.1 times the tokens and 2.4 to 4.3 times the model calls of uninterrupted sessions. The printed Table 2 (p. 7) gives 3.05 to 11.86 times the tokens and 1.73 to 4.25 times the calls. The arXiv source keeps an earlier Table 2, commented out in `sec/4_experiment.tex`, whose uninterrupted columns differ; it gives 4.50 to 11.12 and 2.37 to 4.25, the ranges in the text. The printed table is consistent with the next sentence (resumed focus stages at 1.41 to 2.95 times the tokens).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads the arXiv 2611.02017v1 PDF and source, checks both hashes, reads the printed Table 2 and the commented-out one, and computes the two ranges from each.

## Status

Not yet sent to the authors.

## Author response

None yet.

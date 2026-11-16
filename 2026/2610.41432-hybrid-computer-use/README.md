# Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface (arXiv:2610.41432): consistency checks

Tables 2 and 4 report the same OSWorld 1.0 runs with costs about five times apart.

## Paper

- Title: Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface
- arXiv: [2610.41432v1](https://arxiv.org/abs/2610.41432v1) (the version checked, sha256 `3b383495…4bf2`)
- Hugging Face: [papers/2610.41432](https://huggingface.co/papers/2610.41432)
- Code: [microsoft/Hybrid-Computer-Use](https://github.com/microsoft/Hybrid-Computer-Use)
- CheckPaper report: [checkpaper.app/r/rrr6dsmbr6](https://checkpaper.app/r/rrr6dsmbr6)

## Findings

1. **Cost in Table 2 versus Table 4.** Both tables report HCU and CUA Driver with GPT-5.4 on OSWorld 1.0, each a mean of three runs (361 tasks in Table 2, 360 in Table 4). Score, steps, input tokens and time agree within about 1.5%, but cost per task is $2.52 and $5.65 in Table 2 against $0.504 and $0.983 in Table 4, 5.0 and 5.75 times apart. Appendix B says cost is at provider list prices. The relative saving of HCU over CUA Driver is 55.4% by Table 2 and 48.7% by Table 4.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.41432v1, checks its hash, finds the rows of Tables 2 and 4, and compares their costs.

## Status

Confirmed and to be corrected. The authors said on 2026-11-17 that Table 2 priced every input token at the uncached rate although about 95% were cache hits, while Table 4 already used cached-input pricing. Recomputed, Table 2 costs about $0.51 (HCU) and $0.98 (CUA Driver) per task, and the saving becomes about 48% instead of 55%; the next version will fix both tables and state the pricing convention in each caption. Asked in [the Hybrid Computer Use repository](https://github.com/microsoft/Hybrid-Computer-Use/issues/3).

## Author response

2026-11-17, in the GitHub issue:

> Table 2 priced every input token at the uncached rate. That is wrong for these runs: about 95% of input tokens were cache hits, and Table 4 already applies the cached-input price, which is why the two tables differ by about 5x.
>
> Recomputing Table 2 with cached-input pricing gives per-task costs close to Table 4 (about $0.51 for HCU and $0.98 for CUA Driver), and HCU's cost saving over CUA Driver becomes about 48%, in line with Table 4, instead of the 55% in the current text. Score, Steps, Input and Time are not affected.
>
> The next version will report Cost computed this way in both tables, update the numbers in the text that depend on it, and state the pricing convention in each caption.

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

Not yet sent to the authors.

## Author response

None yet.

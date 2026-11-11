# CoworkOS (arXiv:2611.03178): consistency check

Several OfficeQA Pro scores cannot come from the 133-question set the paper describes, if each question is scored right or wrong.

## Paper

- Title: CoworkOS: Scaling Agent Coworkers for Real-world Automation
- arXiv: [2611.03178v1](https://arxiv.org/abs/2611.03178v1) (the version checked, sha256 `0db3eb94…cf15`)
- Hugging Face: [papers/2611.03178](https://huggingface.co/papers/2611.03178)
- Code: [RUC-NLPIR/CoworkOS](https://github.com/RUC-NLPIR/CoworkOS)
- CheckPaper report: [checkpaper.app/r/r39rz2bf8n](https://checkpaper.app/r/r39rz2bf8n)

## Findings

1. **OfficeQA Pro scores and the 133 questions.** Appendix A.1 (p. 26) uses the 133-question OfficeQA Pro subset. With right or wrong scoring, every score is k/133.
   - Table 1 (p. 15): OpenHands 66.2 = 88/133, but Codex 66.3, DeepSeek Harness 62.3 and CoworkOS 65.9 are not k/133 at one decimal.
   - Table 2 (p. 33): R0, R1, R2 and R4 are exact (74, 71, 70 and 79 of 133). R3 56.14 and the final round R5 62.11 are not; the nearest values are 56.39 and 61.65 or 62.41.

Partial credit, or questions excluded in some runs, would explain the values. The paper does not say which.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.03178v1, checks its hash, finds the OfficeQA Pro rows of Tables 1 and 2, and tests each score against k/133.

## Status

Not yet sent to the authors.

## Author response

None yet.

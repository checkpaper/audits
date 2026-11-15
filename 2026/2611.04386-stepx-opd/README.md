# StepX-OPD (arXiv:2611.04386): consistency checks

Sec. 5.4 says omitting the velocity-regression term gives an Average of 0.8894, while Table 6 gives 0.8731 for the same row, and its components reproduce 0.8731.

## Paper

- Title: StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Few-Step Diffusion Models
- arXiv: [2611.04386v1](https://arxiv.org/abs/2611.04386v1) (the version checked, sha256 `63db820b…7daf55437`)
- Hugging Face: [papers/2611.04386](https://huggingface.co/papers/2611.04386)
- Code: [WinterCCC/StepX-OPD](https://github.com/WinterCCC/StepX-OPD)
- CheckPaper report: [checkpaper.app/r/a9qyru2m2p](https://checkpaper.app/r/a9qyru2m2p)

## Findings

1. **Velocity-regression ablation.** Sec. 5.4 (p. 10) says omitting the term, applying it from step 0 and from step 500 reach Averages of 0.8894, 0.8895 and 0.8901, so the result is stable. Table 6 (p. 10) gives 0.8731 for "w/o regression" (GenEval 0.9134, OCR 0.8956, DeQA 4.178, PickScore 22.05). With Average = (GenEval + OCR + DeQA/5 + PickScore/26)/4 (App. C, p. 21), every Table 6 row reproduces, including 0.8731. By the table the term adds 0.0170 to the Average; by the text it adds 0.0007. Table 6 also lists "from step 1000" at 0.8652.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.04386v1, checks its hash, finds the quoted passages and values, and recomputes every Table 6 Average.

## Status

Contacting the authors, started 2026-11-16. Asked in [the StepX-OPD repository](https://github.com/WinterCCC/StepX-OPD/issues/3).

## Author response

None yet.

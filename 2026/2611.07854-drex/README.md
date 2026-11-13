# Towards Foundation Decision Models: Drex (arXiv:2611.07854): consistency checks

Three flip rates in Table 7 cannot occur on the stated 173 decisions.

## Paper

- Title: Towards Foundation Decision Models: Drex
- arXiv: [2611.07854v2](https://arxiv.org/abs/2611.07854v2) (the version checked, sha256 `6bff5f00…2bd8`)
- Hugging Face: [papers/2611.07854](https://huggingface.co/papers/2611.07854)
- Code: [nace-ai/drex-decision-models](https://github.com/nace-ai/drex-decision-models)
- CheckPaper report: [checkpaper.app/r/bhm4r2dyen](https://checkpaper.app/r/bhm4r2dyen)

## Findings

1. **Table 7, flip rate for K ≥ 6.** Section 8.5 (p. 21) evaluates option-order flips on 1,591 decisions, 173 of them with six or more options. All four overall flip rates in Table 7 are k/1591 (for example 5.3% = 84/1591). For K ≥ 6, only the released model's 13.3% = 23/173 is attainable; 14.1% (SFT only), 17.8% (without ℓπ, ℓs) and 13.0% (before vision SFT) are not, with nearest values 13.87 or 14.45, 17.34 or 17.92, and 12.72 or 13.29.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.07854v2, checks its hash, finds the Table 7 rows, and tests each flip rate against k/1591 and k/173.

## Status

Not yet sent to the authors.

## Author response

None yet.

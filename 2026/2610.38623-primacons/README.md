# Cross-Primitive Consistency in Jev (arXiv:2610.38623): consistency checks

For JevK5-4B on Axis III, the two disagreement quadrants of Figure 5 hold 29.19% of samples, while Table 3 gives a conflict rate K of 26.69%, although the caption says the dashed lines are the 0.5 decision boundaries.

## Paper

- Title: Cross-Primitive Consistency in Jev
- arXiv: [2610.38623v1](https://arxiv.org/abs/2610.38623v1) (the version checked, sha256 `f536b19f…fd1d`)
- Hugging Face: [papers/2610.38623](https://huggingface.co/papers/2610.38623)
- Code: [67L1/PrimaCons-CRPR](https://github.com/67L1/PrimaCons-CRPR)
- CheckPaper report: [checkpaper.app/r/7wa5csneq6](https://checkpaper.app/r/7wa5csneq6)

## Findings

1. **Figure 5 versus K.** Table 3 (p. 5) gives JevK5-4B K = 26.69%, where K (Eq. 4) is the share of samples whose Choice and Noul abstention decisions differ. Figure 5 (p. 5) splits the same samples by the 0.5 decision boundaries into 33.82%, 4.45%, 24.74% and 36.99%, and the text calls the top-left (24.74%) and bottom-right (4.45%) quadrants the cases where the two primitives disagree. These sum to 29.19%, 2.50 pp above K.
2. **One result, two gains.** Under LODO, JevK5-2B raw-label accuracy rises from 84.90% to 87.42%. The introduction (p. 2) reports this as +2.52%, the absolute change; the abstract (p. 1) and Section 4 (p. 7) report +2.97%, the relative change. The in-domain Axis II gain, 77.67% to 98.48%, is printed as +20.81%, the absolute change.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.38623v1, checks its hash, finds the quoted passages and values, and recomputes both comparisons.

## Status

Contacting the authors, started 2026-11-15. Asked in [the PrimaCons-CRPR repository](https://github.com/67L1/PrimaCons-CRPR/issues/2).

## Author response

None yet.

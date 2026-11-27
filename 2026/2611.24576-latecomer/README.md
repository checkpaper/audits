# Late Entry in Looped Language Models (arXiv:2611.24576): consistency check

The synchronous cache-completion decoder is reported at .853 / .708 in Sec. 2 and at .852 / .684 in Table 14, and the "2× to 16×" rollback reduction includes two rows below 2×.

## Paper

- Title: Late Entry in Looped Language Models
- arXiv: [2611.24576v1](https://arxiv.org/abs/2611.24576v1) (the version checked, sha256 `92186e9f…62b2`)
- Hugging Face: [papers/2611.24576](https://huggingface.co/papers/2611.24576)
- Code: [Xalp/LateComer](https://github.com/Xalp/LateComer)
- CheckPaper report: [checkpaper.app/r/vavc7rt74y](https://checkpaper.app/r/vavc7rt74y)

## Findings

1. **Same decoder, two results.** Sec. 2 (p. 5) and Fig. 2(c) report that running the final two passes per token while synchronously completing each token's four-pass cache before the next step gives .853 on GSM8K and .708 on IFEval. Table 14 (p. 27) lists the same policy, "Synchronous (repair before next step), Sequential", at K = 2 as .852 and .684. On IFEval (n = 541) that is 383 against 370 correct, so the +12.0-point gain quoted in Sec. 2 becomes +9.6 with the Table 14 value.
2. **"Cutting rollbacks 2× to 16×" (p. 18).** In the Ouro-2.6B rows of the same table, margin gating changes the rollback column from 2.02 to 1.26 on GSM8K K = 2 (1.60×), the headline τ = 0.15 row, and from 5.98 to 4.08 on IFEval K = 2 (1.47×).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.24576v1, checks its hash, quotes the passages above and recomputes the ratios.

## Status

Not yet sent.

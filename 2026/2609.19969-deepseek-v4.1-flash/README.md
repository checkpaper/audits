# DeepSeek-V4.1-Flash (arXiv:2609.19969): consistency checks

Two numbers in the DeepSeek-V4.1-Flash technical report that readers can check against the paper's own tables and figures.

## Paper

- Title: DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression
- arXiv: [2609.19969v1](https://arxiv.org/abs/2609.19969v1) (the version checked, sha256 `0cfdda19…4ac0`)
- Hugging Face: [papers/2609.19969](https://huggingface.co/papers/2609.19969)
- CheckPaper report: [checkpaper.app/r/u274f3tdup](https://checkpaper.app/r/u274f3tdup)

## Findings

1. **World knowledge versus V4-Pro-Base.** Page 6 states that V4.1-Flash-Base achieves world knowledge, reasoning and coding abilities comparable to V4-Pro-Base. In Table 1 (p. 24) V4.1-Flash-Base trails V4-Pro-Base on 5 of the 6 World Knowledge rows, including Simple-QA verified (42.3 vs 55.2) and MultiLoKo (45.5 vs 50.9). The code and math rows support the comparison.
2. **The 5% to 10% held-out improvement.** Page 6 reports 5% to 10% improvements on held-out evaluations. The Figure 6 bar labels (p. 25) give these BPB reductions:

   | Held-out set | vs V4-Pro-Base | vs V4-Flash-Base |
   | --- | --- | --- |
   | Internal Docs | 4.4% | 8.6% |
   | Internal Code Repos | 3.4% | 7.6% |
   | Academic Materials | 8.0% | 12.7% |

   Against V4-Pro-Base two of three fall below 5%; against V4-Flash-Base one exceeds 10%. The paper does not say which baseline the range refers to.

## Reproduce

```bash
pip install pymupdf
python verify.py
```

The script downloads arXiv 2609.19969v1, checks its hash, finds the quoted sentences on p. 6 and the Table 1 rows on p. 24, and recomputes the percentages. Figure 6 is a raster image, so its six bar labels are typed into the script.

## Status

Contacting the authors, started 2026-11-10. Asked on the [Hugging Face paper page](https://huggingface.co/papers/2609.19969) on 2026-11-11.

## Author response

None yet.

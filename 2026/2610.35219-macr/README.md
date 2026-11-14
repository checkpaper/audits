# Multi-Agent Relay Thinking (arXiv:2610.35219): consistency checks

On MMStar, MACR uses 4,150 tokens per sample in Table 1 and 312 in the Table 2 ablation on a 500-item MMStar subset, a 13.3× difference at similar accuracy.

## Paper

- Title: Multi-Agent Relay Thinking
- arXiv: [2610.35219v2](https://arxiv.org/abs/2610.35219v2) (the version checked, sha256 `728fa5ac…c48f`)
- Hugging Face: [papers/2610.35219](https://huggingface.co/papers/2610.35219)
- Code: [67L1/MACR](https://github.com/67L1/MACR)
- CheckPaper report: [checkpaper.app/r/455tj89ybj](https://checkpaper.app/r/455tj89ybj)

## Findings

1. **Tokens on MMStar.** Table 1 (p. 6) and Section 3.2 (p. 5) give MACR 4,150 tokens on MMStar at 72.00% accuracy. Table 2 (p. 7), run on 500 randomly sampled MMStar instances, gives MACR 312 tokens at 72.40%, and its ablation variants 322 to 427.
2. **Number at risk.** Section 3.4.2 (p. 7) gives numbers at risk of 3,151 for MiniCPM-V 4.5 and 1,163 and 1,658 for the other two models. The at-risk table in Figure 6b (p. 8) has 1,781, 810 and 585 as its largest cells; none of the three text values appears in it.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.35219v2, checks its hash, finds the quoted passages and values, and compares them.

## Status

Contacting the authors, started 2026-11-15. Asked in [the MACR repository](https://github.com/67L1/MACR/issues/2).

## Author response

None yet.

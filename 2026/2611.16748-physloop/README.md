# PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation (arXiv:2611.16748): consistency checks

Table 1's Win column is described with two different protocols, six of nine Repair rates cannot come from 50 tasks, and PhysLoop is fifth of nine on visual realism although the text says it is highest on every human dimension.

## Paper

- Title: PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation
- arXiv: [2611.16748v1](https://arxiv.org/abs/2611.16748v1) (the version checked, sha256 `85f304f9…3050`)
- Hugging Face: [papers/2611.16748](https://huggingface.co/papers/2611.16748)
- Code: [DAGroup-PKU/PhysLoop](https://github.com/DAGroup-PKU/PhysLoop)
- CheckPaper report: [checkpaper.app/r/nny8f38m7c](https://checkpaper.app/r/nny8f38m7c)

## Findings

1. **Win protocol.** Section 5.2 (p. 9) says each video goes to multiple raters with method identities hidden. The Table 1 caption (p. 7) says Win "is computed from 301 unblinded supplementary pairwise comparisons by one author". Appendix C (p. 18) says each pairwise contrast compares a UE-guided output with the direct output of the same video model, but the nine Win values sum to 450.00 (mean 50.00), the pattern of a round robin among all nine rows.
2. **Repair rates.** PhysLoop-Repair has 50 tasks (p. 8) and each method returns one final result per task. Six of the nine Repair rates are not multiples of 2%: 14.67, 19.33, 78.67, 68.67, 72.67 and 60.67. All nine are multiples of 1/150.
3. **Visual realism.** Section 5.3 (p. 10) says the full PhysLoop configuration "achieves the highest scores across all human-evaluation dimensions". Its Real. score, 3.72, is fifth of nine in Table 1, below Seedance 2.5 (4.29), H3 (4.27), Gemini Omni (3.82) and Claude Opus 5 + Seedance 2.5 (3.82).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.16748v1, checks its hash, finds the quoted passages and Table 1 rows, and recomputes the Win sum, the Repair grid and the realism ranking.

## Status

Contacting the authors, started 2026-11-14.

## Author response

None yet.

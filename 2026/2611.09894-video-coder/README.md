# Video-Coder: Reinforcing Agentic Coding for Video Generation (arXiv:2611.09894): consistency checks

A gain stated as 16.28 points is 3 points, two Table 1 rows are identical, and the dataset sizes differ between sections.

## Paper

- Title: Video-Coder: Reinforcing Agentic Coding for Video Generation
- arXiv: [2611.09894v1](https://arxiv.org/abs/2611.09894v1) (the version checked, sha256 `1111598b…2100`)
- Hugging Face: [papers/2611.09894](https://huggingface.co/papers/2611.09894)
- Code: [CYWang735/Video-Coder](https://github.com/CYWang735/Video-Coder)
- CheckPaper report: [checkpaper.app/r/e392px5th5](https://checkpaper.app/r/e392px5th5)

## Findings

1. **OmniWeaving gain.** Section 4.2 (p. 7) says Video-Coder improves OmniWeaving on PhyGenBench from 0.48 to 0.51, "an increase of 16.28 points". That is 0.03 absolute, or 6.25% relative.
2. **Table 1 rows.** The LTX-Video-2B and Video-CoCo rows are identical in all five columns (0.51, 0.58, 0.48, 0.45, 0.51).
3. **Dataset sizes.** The abstract, Section 1, Section 3.1 and Section 3.3 name Video-Coder-SFT-6k and Video-Coder-RL-2k; the training details in Section 4.1 (p. 6) say SFT on Video-Coder-SFT-10k and RL on Video-Coder-RL-4k.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.09894v1, checks its hash, and finds each quoted passage.

## Status

Contacting the authors, started 2026-11-13. Asked in [the Video-Coder repository](https://github.com/CYWang735/Video-Coder/issues/4).

## Author response

None yet.

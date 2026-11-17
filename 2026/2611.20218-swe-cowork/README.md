# SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations (arXiv:2611.20218): consistency checks

Figure 7(c) counts 979 failed F2P test nodes, while Figure 7(b) and Table 2 leave at most 976. Six Table 2 values do not fit the stated 2,699 F2P and 562 P2P totals.

## Paper

- Title: SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations
- arXiv: [2611.20218v1](https://arxiv.org/abs/2611.20218v1) (the version checked, sha256 `9872017f…b105`)
- Hugging Face: [papers/2611.20218](https://huggingface.co/papers/2611.20218)
- Code: [TokenWave-AI/swe-cowork-bench](https://github.com/TokenWave-AI/swe-cowork-bench)
- CheckPaper report: [checkpaper.app/r/d5eckxgzyv](https://checkpaper.app/r/d5eckxgzyv)

## Findings

1. **Figure 7, panels (b) and (c).** Panel (b) splits Claude-Opus-5.5's F2P nodes into public (n = 453, 73.7% pass), disclosed (n = 1,425, 68.8%) and not disclosed (n = 821, 49.8%). These sum to 2,699 and give 334, 980 or 981, and 409 passed nodes, so 975 or 976 failed. Table 2 (63.84% of 2,699 = 1,723 passed) gives 976 failed. Panel (c) assigns failed F2P nodes with linked requirements to discovery 16, ask 415 and implement 548, a total of 979. Ask (415) also exceeds the 412 failed not-disclosed nodes.
2. **Table 2 denominators.** The caption says F2P and P2P use the release totals of 2,699 and 562 test nodes. F2P 35.70 (Qwen3.8-Max), 30.70 (Qwen3.8-Flash) and 24.40 (GLM 5.2) are not k/2699. P2P 91.80 (Qwen3.8-Max), 93.40 (Qwen3.8-Flash) and 94.30 (DeepSeek V4.1 Flash) are not k/562; all three are k/561 (515, 524 and 529). The other 16 F2P and P2P values fit the stated totals.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.20218v1, checks its hash, quotes Figure 7 and Table 2, and recomputes the node counts and denominators.

## Status

[Asked the authors](https://github.com/TokenWave-AI/swe-cowork-bench/issues/1) on 2026-11-18.

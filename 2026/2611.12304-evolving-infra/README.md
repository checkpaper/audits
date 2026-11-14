# Evolving Infra: Agent-Adaptive LLM Serving at Scale (arXiv:2611.12304): consistency checks

For Claude Code with 126 agents, the main result starting from 6P3D (13.2 s mean E2E) is 16% above the ablation run from the same initial split (11.4 s), although the text says the initial split changes latency by at most 1.8%.

## Paper

- Title: Evolving Infra: Agent-Adaptive LLM Serving at Scale
- arXiv: [2611.12304v2](https://arxiv.org/abs/2611.12304v2) (the version checked, sha256 `84f4d894…c269`)
- Hugging Face: [papers/2611.12304](https://huggingface.co/papers/2611.12304)
- Code: [mit-han-lab/EvolvingInfra](https://github.com/mit-han-lab/EvolvingInfra)
- CheckPaper report: [checkpaper.app/r/xjjtza5w4m](https://checkpaper.app/r/xjjtza5w4m)

## Findings

1. **Two runs of the same setting.** Section 6.2 (p. 12) says Evolving Infra and Dynamo both start from 6P3D. For CC with 126 agents, Table C.3 (p. 29) gives Evolving Infra 13.2 s mean E2E latency and 5.85 req/s. Figure 8a (p. 13) gives 11.4 s for the same workload starting from 6P3D, and Section 6.4 (p. 14) says the initial split changes mean E2E latency by at most 1.8% (11.2 to 11.4 s). 13.2 s is 15.8% above 11.4 s and 17.9% above the 3P6D run. Figure 8b gives 6.25 req/s with adaptation from 4P5D, the split all four Figure 8a runs converge to, against 5.85 req/s in Table C.3.
2. **N_branch.** Appendix C.4 (p. 29) says the two systems keep a similar N_branch, "for example 159 and 161 on CC with 126 concurrent agents". From Table C.3 and X = N_branch / (E2E + pause), Dynamo has 2.14 × (54.4 + 18.6) = 156.2 (155.6 to 156.8 with rounding) and Evolving Infra 5.85 × (13.2 + 14.1) = 159.7 (159.0 to 160.4).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12304v2, checks its hash, finds the quoted passages and table values, and recomputes the latency gaps and N_branch with rounding ranges.

## Status

Contacting the authors, started 2026-11-15. Asked in [the EvolvingInfra repository](https://github.com/mit-han-lab/EvolvingInfra/issues/19).

## Author response

None yet.

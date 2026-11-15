# Authorization Drift / ADB (arXiv:2611.09113): consistency checks

The 25,207 evaluated trajectories are about three quarters of 13 models × 648 samples × 4 rollouts, and the Security row of Table 3 does not satisfy CCSR = CSR / (1 − DR).

## Paper

- Title: Authorization Drift in LLM Agents: Evaluating Boundary Compliance
- arXiv: [2611.09113v1](https://arxiv.org/abs/2611.09113v1) (the version checked, sha256 `dd35ecae…2ef041248`)
- Hugging Face: [papers/2611.09113](https://huggingface.co/papers/2611.09113)
- Code: [ZJR-FZD/AgentDrift](https://github.com/ZJR-FZD/AgentDrift)
- CheckPaper report: [checkpaper.app/r/gyqekay9e4](https://checkpaper.app/r/gyqekay9e4)

## Findings

1. **Trajectory count.** Sec. 1 (p. 2) reports 25,207 evaluated trajectories from 13 LLMs under NORMAL on the 648-sample benchmark, and the Table 2 caption (p. 7) gives rates as mean ± std over 4 rollouts. 13 × 648 × 4 = 33,696, so 25,207 is 74.8% of it; 13 × 648 × 3 = 25,272 is closer. The abstract (p. 1) describes the same 25,207 as covering 13 LLMs and three frameworks.
2. **Table 3 Security row.** Sec. 3.3 (p. 5) defines CCSR = CSR / (1 − DR). For Security, Table 3 (p. 7) gives DR 0.411 and CSR 0.433, so CCSR = 0.735 (0.734 to 0.737 with rounding), against 0.724 printed. The other six domains match.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.09113v1, checks its hash, finds the quoted passages and values, and recomputes both checks.

## Status

Contacting the authors, started 2026-11-16. Asked in [the AgentDrift repository](https://github.com/ZJR-FZD/AgentDrift/issues/2).

## Author response

None yet.

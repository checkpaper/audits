# Interpreting Coding Agents Through Their Behavioral Trajectories (arXiv:2611.17440): consistency checks

The exact-match rate in the parser audit (Table 1) is higher than its mutation-type agreement allows.

## Paper

- Title: Interpreting Coding Agents Through Their Behavioral Trajectories
- arXiv: [2611.17440v1](https://arxiv.org/abs/2611.17440v1) (the version checked, sha256 `e89b6239…b6b`)
- Hugging Face: [papers/2611.17440](https://huggingface.co/papers/2611.17440)
- Code: [SWE-rebench/trajectory-analyzer](https://github.com/SWE-rebench/trajectory-analyzer)
- CheckPaper report: [checkpaper.app/r/d5xr4sq25t](https://checkpaper.app/r/d5xr4sq25t)

## Findings

1. **Exact match above its bound.** Table 1 (p. 5) audits the parser on 500 actions. A field gets a reference label when at least 5 of 6 models agree, and the consensus-rate column gives how many actions that is. Mutation type is resolved on 98.2% = 491 actions, and the parser agrees on 68.8% = 338 of them, so 153 disagree. Exact match, which Appendix A.3 (p. 12) says requires all four core fields (primary operation, target file role, mutation type, read mode) to agree, is resolved on 91.4% = 457 actions. Every one of those is also resolved on mutation type, so at most 491 − 457 = 34 of the 153 disagreements fall outside them. At least 119 of the 457 therefore fail on mutation type, and exact match can be at most 338/457 = 74.0%. Table 1 gives 77.5% (354/457).
2. **Two rates that fit no count.** On the same denominators, primary-operation agreement of 82.4% of 470 and ordered-operations agreement of 86.0% of 439 are not k/n for any whole k (the nearest values are 82.3% or 82.6%, and 85.9% or 86.1%). The other four rows fit exactly.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.17440v1, checks its hash, reads Table 1, recovers the counts behind each rate, and computes the bound on exact match.

## Status

Contacting the authors, started 2026-11-17.

## Author response

None yet.

# “Shall We Approve?” Consequence-Aware Approval for Autonomous Coding Agents (arXiv:2610.40753): consistency checks

The SABER rates are described as over 682 tasks, but the per-category table fits 580, and only 47 of the 84 file-system destruction tasks.

## Paper

- Title: “Shall We Approve?” Consequence-Aware Approval for Autonomous Coding Agents
- arXiv: [2610.40753v1](https://arxiv.org/abs/2610.40753v1) (the version checked, sha256 `0a96187b…2bf3`)
- Hugging Face: [papers/2610.40753](https://huggingface.co/papers/2610.40753)
- Code: [wudaoz/Caper](https://github.com/wudaoz/Caper)
- CheckPaper report: [checkpaper.app/r/c89sdcdp5h](https://checkpaper.app/r/c89sdcdp5h)

## Findings

1. **Per-category denominators.** Table 10 (p. 23) gives each system's harmful rate in eight harm categories. In every category exactly one task count fits all nine rates, and each is below the Table 1 count (p. 7): code tampering 114 of 126, information leak 92 of 104, file-system destruction 47 of 84, unauthorized access 74 of 82, data destruction 77 of 82, privilege escalation 70 of 74, outbound network 52 of 66, persistence 54 of 64. They sum to 580.
2. **Table 3.** Section 5.1 says the evaluation uses SABER's 682 shell-only tasks. Eight of the 36 SABER values in Table 3 (p. 9) for these nine systems cannot be k/682, for example Caper's 48.6 and 67.8; all 36 fit k/580 (Caper harmful 6.7% = 39/580).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.40753v1, checks its hash, finds the Table 1, Table 3 and Table 10 rows, and searches for the task counts that fit each row.

## Status

Contacting the authors, started 2026-11-14. Asked in [the Caper repository](https://github.com/wudaoz/Caper/issues/2).

## Author response

None yet.

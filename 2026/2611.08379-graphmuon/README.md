# Module-Aware Optimization for Graph Neural Networks (arXiv:2611.08379): consistency checks

On Questions/GAT, the epochs to target in Tables 1 and 14 exceed the training budget in Table 7.

## Paper

- Title: Module-Aware Optimization for Graph Neural Networks
- arXiv: [2611.08379v1](https://arxiv.org/abs/2611.08379v1) (the version checked, sha256 `4f08301a…ddc8`)
- Hugging Face: [papers/2611.08379](https://huggingface.co/papers/2611.08379)
- Code: [guy-hadad/GraphMuon](https://github.com/guy-hadad/GraphMuon)
- CheckPaper report: [checkpaper.app/r/p8ut5ehnrw](https://checkpaper.app/r/p8ut5ehnrw)

## Findings

1. **Questions/GAT over budget.** Table 7 (p. 22) sets a 300-epoch budget for Questions, and the text above it says time-to-target is computed only within these budgets, with runs that miss the target marked as not reaching it. Tables 1 (p. 8) and 14 (p. 28) report AdamW reaching the Questions/GAT target at epoch 481 and Muon at epoch 320, both past 300. The target is AdamW's minimum mean validation loss, so it was set from a run longer than the budget, and under the stated rule Muon would be marked as not reaching it. The other seven OGB rows fit their budgets, though AdamW reaches its own target at the last budget epoch on ogbn-mag/GCN (100 of 100) and ogbn-products (300 of 300).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.08379v1, checks its hash, reads the budgets in Table 7 and the epochs in Table 14, and flags rows over budget.

## Status

Contacting the authors, started 2026-11-17.

## Author response

None yet.

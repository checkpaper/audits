# ODE Policy: Robot Learning via Action Dynamics, Not Actions (arXiv:2611.01729): consistency check

Sec. 9.3 compares the gripper-in-ODE variant with a baseline of 79.2 / 95.0 / 92.8 % at epochs 1 / 5 / 10, but 95.0 and 92.8 are the "No offset" row of Table S8; the default ("Component mean (ours)") has 94.8 and 94.3, and Table S7 gives 93.9 at epoch 10. In Table S5, the DDIM-UNet boundary-to-inside ratio is printed as 2.97 while its two rows give 10.9 / 4.02 = 2.71.

## Paper

- Title: ODE Policy: Robot Learning via Action Dynamics, Not Actions
- arXiv: [2611.01729v1](https://arxiv.org/abs/2611.01729v1) (the version checked, sha256 `b4654b6b…5f5a`)
- Hugging Face: [papers/2611.01729](https://huggingface.co/papers/2611.01729)
- Code: [NTUMARS/ODE-POLICY](https://github.com/NTUMARS/ODE-POLICY)
- CheckPaper report: [checkpaper.app/r/an5bxy2dg3](https://checkpaper.app/r/an5bxy2dg3)

## Findings

1. **Baseline of the gripper ablation (Sec. 9.3, p. 21; Tables S7–S8, p. 34).** "the success rate drops from 79.2%, 95.0%, and 92.8% to 74.5%, 91.8%, and 92.2% at epochs 1, 5, and 10". In Table S8, 95.0 and 92.8 are the "No offset" row; "Component mean (ours)" has 94.8 (epoch 5) and 94.3 (epoch 10). Table S7 gives the default ODE-MLP 93.9 at epoch 10. Against the default the drops are 4.7 / 3.0 / 2.1 points rather than 4.7 / 3.2 / 0.6.
2. **Cup-task ratio (Table S5, p. 32).** Boundary to inside ratios are printed as 0.96 / 0.86 / 2.03 / 2.97. From the acceleration rows: 1.04 / 1.09 = 0.95, 0.29 / 0.34 = 0.85, 6.40 / 3.15 = 2.03 and 10.9 / 4.02 = 2.71. The first three agree within rounding; DDIM-UNet does not, unless the ratio is a per-trial mean (its boundary acceleration has a standard deviation of 4.5).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.01729v1, checks its hash, quotes Sec. 9.3 and Tables S5, S7 and S8, and recomputes the drops and ratios.

## Status

[Asked the authors](https://github.com/NTUMARS/ODE-POLICY/issues/4) on 2026-11-23.

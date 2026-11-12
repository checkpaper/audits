# P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter-Space Merging (arXiv:2611.03953): consistency checks

Section 4.3 says 1.7B IM-MOPD did not merge the medical teacher; Table 12 lists Med merges in two of its three seeds.

## Paper

- Title: P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter-Space Merging
- arXiv: [2611.03953v2](https://arxiv.org/abs/2611.03953v2) (the version checked, sha256 `1532a8e9…b483`)
- Hugging Face: [papers/2611.03953](https://huggingface.co/papers/2611.03953)
- Code: [SinuoWang/P2-MOPD](https://github.com/SinuoWang/P2-MOPD)
- CheckPaper report: [checkpaper.app/r/t5jgedff6x](https://checkpaper.app/r/t5jgedff6x)

## Findings

1. **IM-MOPD and the medical teacher.** Section 4.3 (p. 8) uses 1.7B IM-MOPD, "which did not merge the medical teacher", as one of three runs that move at most 0.03 along the medical task vector. Table 12 (p. 16) lists the domains merged at steps 25, 50 and 75. For 1.7B, seed 43 merges Med, Fin, IF and seed 44 merges Med, IF at step 50.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.03953v2, checks its hash, and finds the Section 4.3 sentence and the three 1.7B rows of Table 12.

## Status

Not yet sent to the authors.

## Author response

None yet.

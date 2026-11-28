# LoopedWAM: Looped World Action Models for Elastic Inference (arXiv:2611.25595): consistency check

Table 4 reports 2.05 GB peak GPU memory for LoopedWAM, VAE included. The released code keeps the 584.5M policy parameters in FP32, which take 2.34 GB (2.18 GiB) on their own, so the reported peak seems to come from a lower-precision setup that the paper does not describe.

## Paper

- Title: LoopedWAM: Looped World Action Models for Elastic Inference
- arXiv: [2611.25595v1](https://arxiv.org/abs/2611.25595v1) (the version checked, sha256 `408cc710…311a`)
- Hugging Face: [papers/2611.25595](https://huggingface.co/papers/2611.25595)
- Code: [anhdao69/LoopedWAM](https://github.com/anhdao69/LoopedWAM) (commit `51aac25` checked)
- CheckPaper report: [checkpaper.app/r/gk7d4pmhfx](https://checkpaper.app/r/gk7d4pmhfx)

## Findings

1. **Peak memory vs released precision.** Sec. 4.1 (p. 7) gives 584.5M policy parameters, excluding the frozen VAE and text encoder. Table 4 (p. 9) reports a 2.05 GB peak for LoopedWAM with the VAE included. `build_loopedwam` in `src/loopedwam/models/loopedwam.py` says "Policy weights are FP32; on CUDA the frozen VAE runs in BF16", and inference runs under BF16 autocast, which keeps FP32 weights. In FP32 the policy weights are 584.5M × 4 bytes = 2.34 GB (2.18 GiB), already above 2.05 before the VAE and activations. BF16 weights would be 1.17 GB. The paper does not state the precision used for the Table 4 measurements.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.25595v1 and the code file at the checked commit, checks both hashes, quotes the parameter count, the Table 4 row and the precision note in the code, and computes the weight sizes.

## Status

[Asked the authors](https://github.com/anhdao69/LoopedWAM/issues/3) on 2026-11-28.

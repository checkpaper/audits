# Posterior Matching Distillation (arXiv:2611.26629): consistency checks

The default FLUX.2 PMD model has FID 24.12 on COCO-10k in Table 1 but 17.47 in the Table 5 ablation row that reproduces its Table 2 diversity scores exactly.

## Paper

- Title: Posterior Matching Distillation
- arXiv: [2611.26629v1](https://arxiv.org/abs/2611.26629v1) (the version checked, sha256 `ce7b4026…f94f`)
- Hugging Face: [papers/2611.26629](https://huggingface.co/papers/2611.26629)
- Code: [yesiltepe-hidir/PMD](https://github.com/yesiltepe-hidir/PMD)
- CheckPaper report: [checkpaper.app/r/9479vs46qg](https://checkpaper.app/r/9479vs46qg)

## Findings

1. **FID of the default model (Table 1, p. 7 vs Table 5, p. 20).** The default tilt radius is uniform on [0.25, 0.50] (p. 19). Table 5's U(0.25, 0.5) row gives Vendi 3.370, DreamSim 0.3503, DINOv2 0.3690 and LPIPS 0.5705, the same four values as PMD (FLUX.2) in Table 2, so it is the same model. Its FID COCO-10k is 17.47. Table 1 reports PMD on FLUX.2 at FID 24.12 on 10K MS-COCO 2014 prompts, and the text compares RTDMD's 31.57 against that 24.12. All four Table 5 FIDs (16.40–17.87) are below every FLUX.2 four-step FID in Table 1.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.26629v1, checks its hash, quotes the passages and tables above, and recomputes the numbers.

## Status

Answered. [Asked the authors](https://github.com/yesiltepe-hidir/PMD/issues/1) on 2026-11-21.

The author (yesiltepe-hidir) replied on 2026-11-21 and closed the issue as completed: "The 17.47 score is obtained using the coarse-only tilt direction, whereas the main paper reports results using a combination of coarse and isotropic directions." The authors plan to update the paper within a week and add the coarse-only score to the main table. We noted that the p. 19 hyperparameter table lists coarse tilt probes for FLUX.2, and that Table 2's diversity scores equal the coarse-only row of Table 5.

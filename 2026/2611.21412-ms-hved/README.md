# Flexible Multi-Stack Super-Resolution of Clinical Brain MRI Using Hetero-Orientation Variational Encoding (arXiv:2611.21412): consistency check

The Introduction says that on the paired real cases MS-HVED "improves perceptual quality and structural similarity over the baselines", but in Table 6 the Naive + FOV baseline has the higher SSIM (.841 vs .835), as Sec. 5.2.1 itself states.

## Paper

- Title: Flexible Multi-Stack Super-Resolution of Clinical Brain MRI Using Hetero-Orientation Variational Encoding: Expert Reader Evaluation in a Nigerian Cohort
- arXiv: [2611.21412v1](https://arxiv.org/abs/2611.21412v1) (the version checked, sha256 `a71f4294…5bca`)
- Hugging Face: [papers/2611.21412](https://huggingface.co/papers/2611.21412)
- Code: [cai4cai/ms-hved](https://github.com/cai4cai/ms-hved)
- CheckPaper report: [checkpaper.app/r/mgbegyfr3b](https://checkpaper.app/r/mgbegyfr3b)

## Findings

1. **SSIM on the paired real cohort (pp. 2–3 vs Table 6, p. 14).** Introduction: "On paired real healthy-control data, MS-HVED improves perceptual quality and structural similarity over the baselines." Table 6 gives SSIM .835 for MS-HVED and .841 for Naive + FOV; Sec. 5.2.1 says "the FOV-weighted stack average achieved the highest PSNR, SSIM, and NCC". MS-HVED has the lowest perceptual loss (.244) and beats SegResNet on SSIM (.835 vs .813), but not every baseline.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.21412v1, checks its hash, quotes the Introduction, Sec. 5.2.1 and Table 6, and finds the best SSIM.

## Status

Not yet asked.

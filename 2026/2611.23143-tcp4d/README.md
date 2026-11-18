# TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation (arXiv:2611.23143): consistency checks

The abstract's 41.5% target-robot gain is the ARX-X5 result alone; on UR5-WSG the gain is 7.0 points.

## Paper

- Title: TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation
- arXiv: [2611.23143v1](https://arxiv.org/abs/2611.23143v1) (the version checked, sha256 `85ec653e…06e8d`)
- Hugging Face: [papers/2611.23143](https://huggingface.co/papers/2611.23143)
- Code: [Livioni/TCP4D](https://github.com/Livioni/TCP4D)
- CheckPaper report: [checkpaper.app/r/eytf76qbps](https://checkpaper.app/r/eytf76qbps)

## Findings

1. **Target-robot gain.** The abstract (p. 1) says joint training on source and augmented demonstrations "improves target-robot success by 41.5% over augmented-only training". Sec. 4.3 (p. 9) reports two target robots: ARX-X5 from 30.5% to 72.0% (+41.5 points) and UR5-WSG from 32.0% to 39.0% (+7.0 points). The 41.5 is the ARX-X5 gain in points. Averaged over both target robots, success goes from 31.25% to 55.50%, a gain of 24.25 points.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.23143v1, checks its hash, quotes the abstract and Sec. 4.3, and recomputes the gains.

## Status

[Asked the authors](https://github.com/Livioni/TCP4D/issues/1) on 2026-11-19.

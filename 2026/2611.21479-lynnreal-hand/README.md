# LynnReal-Hand: Unlocking World Interaction with Hand Control (arXiv:2611.21479): consistency checks

In Table 3, StreamRender2's FPS does not follow from its latency per 17 frames, unlike the other six rows.

## Paper

- Title: LynnReal-Hand: Unlocking World Interaction with Hand Control
- arXiv: [2611.21479v1](https://arxiv.org/abs/2611.21479v1) (the version checked, sha256 `551ef9c7…657b`)
- Hugging Face: [papers/2611.21479](https://huggingface.co/papers/2611.21479)
- Code: [LynnReal-AI/LynnReal](https://github.com/LynnReal-AI/LynnReal)
- CheckPaper report: [checkpaper.app/r/q9xwkjzm78](https://checkpaper.app/r/q9xwkjzm78)

## Findings

1. **Table 3, StreamRender2.** Table 3 (p. 11) reports decoding latency for 17 frames and FPS. For six rows FPS × latency is 16.9 to 17.0 frames (e.g. Ultra-Fast-VAE 363.21 FPS × 46.77 ms). StreamRender2 has 157.65 ms and 123.91 FPS, which is 19.5 frames; 17 / 157.65 ms = 107.83 FPS. Either the latency or the FPS of this row is off.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.21479v1, checks its hash, quotes Table 3, and recomputes FPS from latency.

## Status

Answered. [Asked the authors](https://github.com/LynnReal-AI/LynnReal/issues/3) on 2026-11-19.

An author replied on 2026-11-21: the latency column is the median (P50) over 501 timed 17-frame chunks, while FPS is total frames over total decoding time. For StreamRender2 the two-latent streaming schedule makes the work per chunk uneven, so the median (157.65 ms) and mean (137.19 ms) differ; 8,517 frames / 68.733 s = 123.91 FPS, consistent with the mean. They will label the statistic and define FPS in the caption.

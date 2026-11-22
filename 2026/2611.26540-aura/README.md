# AURA: AUdio-dRiven streaming Avatar (arXiv:2611.26540): consistency check

AURA 1.3B is described as generating 576p video in the abstract, introduction and Sec. 3, but Tables 1 and 2 list it at 480p, with a caption saying it "outputs 480p". The dataset is 30,000 clips averaging 4.8 s, which is 40.0 h, not the stated 38.7 h.

## Paper

- Title: AURA: AUdio-dRiven streaming Avatar
- arXiv: [2611.26540v1](https://arxiv.org/abs/2611.26540v1) (the version checked, sha256 `9462f5c0…f822`)
- Hugging Face: [papers/2611.26540](https://huggingface.co/papers/2611.26540)
- Code: [kyutai-labs/aura](https://github.com/kyutai-labs/aura)
- CheckPaper report: [checkpaper.app/r/vbdpgj68wa](https://checkpaper.app/r/vbdpgj68wa)

## Findings

1. **576p or 480p (pp. 1–4, 10, 12, 16, 27).** The abstract, introduction, related work and conclusion say AURA 1.3B streams "576p video", and p. 10 says it "generates 576p video (768×512 or 576×576)". Tables 1 and 2 and the per-offset tables of App. A.5 list the model at 480p, and the Table 1 caption says "AURA 1.3B outputs 480p at 16 Hz". By pixel count, 768×512 (393,216 px) is closer to 480p 16:9 (409,920 px) than to 576p 16:9 (589,824 px).
2. **Dataset duration (p. 10).** "The resulting clips average 4.8 s" and "The final dataset totals 30,000 clips (38.7 h". 30,000 × 4.8 s = 40.0 h; a 4.8 that is rounded allows 39.6–40.4 h. 38.7 h corresponds to a mean of 4.64 s per clip.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.26540v1, checks its hash, quotes the resolution and dataset statements, and recomputes the totals.

## Status

[Asked the authors](https://github.com/kyutai-labs/aura/issues/1) on 2026-11-23.

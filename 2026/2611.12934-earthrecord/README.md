# EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery (arXiv:2611.12934): consistency check

Table 11 reports that Claude Opus 5.5 answers insufficient evidence in 35 of its 36 runs on the insufficient-evidence questions and in 4.2% of its recognition runs. In the released runs, none of Opus 5.5's 1,518 answers contains insufficient_evidence, while every other model has some.

## Paper

- Title: EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery
- arXiv: [2611.12934v1](https://arxiv.org/abs/2611.12934v1) (the version checked, sha256 `cb8464bf…1e5e`)
- Hugging Face: [papers/2611.12934](https://huggingface.co/papers/2611.12934)
- Code: [ranranrannervous/EarthRecord](https://github.com/ranranrannervous/EarthRecord) (commit `d4b724d` checked)
- CheckPaper report: [checkpaper.app/r/brry6umdcm](https://checkpaper.app/r/brry6umdcm)

## Findings

1. **Opus 5.5 abstention.** Sec. 2.2 (p. 3) says every answer field accepts insufficient evidence. Table 11 (p. 17) gives Claude Opus 5.5 4.2% abstention on recognition runs and 35 abstaining runs out of 36 on the 12 insufficient-evidence questions, 11 of them right in all three passes; Table 7 (p. 15) scores it 97.2 / 91.7 on that class. `results/runs.jsonl.gz` has 1,518 runs for each of the 12 models. Opus 5.5 is the only model with no answer containing insufficient_evidence (0 of 1,518); the other models have 12 to 1,167.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12934v1 and the released runs at the checked commit, checks both hashes, quotes the claims and Table 11, and counts abstaining answers per model.

## Status

[Asked the authors](https://github.com/ranranrannervous/EarthRecord/issues/1) on 2026-11-28.

# CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents (arXiv:2610.40799): consistency checks

Section 4 says the evaluation perturbations never appear in training; pages 7, 22 and 24 say RL randomizes lighting, camera pose and materials.

## Paper

- Title: CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents
- arXiv: [2610.40799v1](https://arxiv.org/abs/2610.40799v1) (the version checked, sha256 `3a046c91…5410`)
- Hugging Face: [papers/2610.40799](https://huggingface.co/papers/2610.40799)
- Code: [waltstephen/CaPtain](https://github.com/waltstephen/CaPtain)
- CheckPaper report: [checkpaper.app/r/5mqxqnjkdr](https://checkpaper.app/r/5mqxqnjkdr)

## Findings

1. **Perturbations in training.** Section 4 (p. 8) says the model is trained only on the 40 original LIBERO tasks and evaluated on three perturbation suites "whose perturbations never appear in training". The training distribution (p. 7) samples "mostly wide-layout scenes with randomized lighting, camera pose and materials"; Appendix A (p. 22) lists 5,600 of the 7,360 RL starts as "wide-layout starts with light, camera and material perturbations"; p. 24 says the method randomizes lighting, camera pose and materials during RL. Light, camera and background are among the LIBERO-Plus perturbation dimensions.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.40799v1, checks its hash, and finds the four quoted passages.

## Status

Closed by the authors on 2026-11-14: they found nothing wrong and say it matches the description in the text. Asked whether the RL randomization ranges are disjoint from the LIBERO-Plus perturbations; no answer yet. Asked in [the CaPtain repository](https://github.com/waltstephen/CaPtain/issues/1).

## Author response

2026-11-14, waltstephen (repository owner), in [the issue](https://github.com/waltstephen/CaPtain/issues/1):

> We checked and found nothing wrong; it matches our description in the text.

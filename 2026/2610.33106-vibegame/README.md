# VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team (arXiv:2610.33106): consistency checks

Section 4.2 says GPT-5.6-Luna does not turn image generation into a visual advantage in P2G; Table 1 gives it higher Functional Visuals in P2G for all three harnesses.

## Paper

- Title: VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team
- arXiv: [2610.33106v1](https://arxiv.org/abs/2610.33106v1) (the version checked, sha256 `63631951…6512`)
- Hugging Face: [papers/2610.33106](https://huggingface.co/papers/2610.33106)
- Code: [tettethu/VibeGame](https://github.com/tettethu/VibeGame)
- CheckPaper report: [checkpaper.app/r/6pt9grb8cp](https://checkpaper.app/r/6pt9grb8cp)

## Findings

1. **Functional Visuals, P2G versus PA2G.** Section 4.2 (p. 8) says GPT-5.6-Luna does not turn image generation into a visual advantage in the P2G setting. In Table 1 (p. 6), for each harness run in both settings, Functional Visuals is higher in P2G: Codex 31.54 vs 28.33 (+3.21), Kimi Code 31.00 vs 29.67 (+1.33), Qwen Code 35.51 vs 27.88 (+7.63). Art & Presentation changes little (+0.78, −0.12, +1.57), so the statement holds for A but not for V.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.33106v1, checks its hash, finds the Section 4.2 sentence and the six Table 1 rows, and compares V and A between settings.

## Status

Contacting the authors, started 2026-11-13. Asked in [the VibeGame repository](https://github.com/tettethu/VibeGame/issues/7).

## Author response

None yet.

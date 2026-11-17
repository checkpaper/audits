# Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent (arXiv:2611.18397): consistency checks

The milestone types listed for the Bestial Ferocity side quest do not match the type counts that Table 6 is computed on.

## Paper

- Title: Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent
- arXiv: [2611.18397v1](https://arxiv.org/abs/2611.18397v1) (the version checked, sha256 `c2829b2f…37d5`)
- Hugging Face: [papers/2611.18397](https://huggingface.co/papers/2611.18397)
- Code: [RainBowLuoCS/Gamer](https://github.com/RainBowLuoCS/Gamer)
- CheckPaper report: [checkpaper.app/r/5pgevxwg6z](https://checkpaper.app/r/5pgevxwg6z)

## Findings

1. **Bestial Ferocity milestone types.** The footnote of Table 14 (p. 48) gives the 55 milestones as N: navigation (32), D: dialogue (16), C: combat (2), U: UI interaction (2), P: puzzle (3). The type column of the same table labels 28 rows N and 20 rows D (C, U and P match).
2. **Table 6 uses the footnote counts.** Each task is evaluated three times (Table 6 caption, p. 22), so a Nav. cell is k/96 under 32 navigation milestones and k/84 under 28; a Dialogue cell is k/48 under 16 and k/60 under 20. All 10 rows of Table 6 fit 32/16 (for example Gemini-3.8-Flash 31.2 = 30/96 and 81.2 = 39/48, Gamer-RL 80.2 = 77/96) and none fit 28/20. So four milestones labelled dialogue in Table 14 are scored as navigation in Table 6, or the labels are off.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.18397v1, checks its hash, counts the type column of Table 14, and tests each Bestial Ferocity Nav. and Dialogue cell of Table 6 against both sets of counts.

## Status

Confirmed by the authors on 2026-11-17 in [the Gamer repository](https://github.com/RainBowLuoCS/Gamer/issues/1). The type column of Table 14 was mislabelled; the correct split is 32 navigation and 16 dialogue, Table 6 is unchanged, and the fix will be in the next arXiv version.

## Author response

From RainBowLuoCS, 2026-11-17 01:41 UTC:

> Hi, thanks so much for pointing this out and for the careful check!
>
> You're absolutely right. The correct breakdown is navigation (32), dialogue (16), combat (2), UI (2), and puzzle (3). There was a labeling error in the type column of Table 14, which we have now fixed. The results in Table 6 are correct and remain unchanged.
>
> We'll include this correction in the next arXiv version.
>
> Thanks again for your attention to our work and for helping us improve the paper. We really appreciate it! 😊

# Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models (arXiv:2611.31977): consistency check

The paper says samples stay stable and do not degrade at K = 8 and K = 16, and contrasts this with looped models whose quality drops beyond their trained loop count. In Table 1, the student trained with K = 4 loses on all four metrics from K = 4 to 8 to 16, and its K = 16 average falls below the teacher.

## Paper

- Title: Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models
- arXiv: [2611.31977v1](https://arxiv.org/abs/2611.31977v1) (the version checked, sha256 `96a496f2…1ded`)
- Hugging Face: [papers/2611.31977](https://huggingface.co/papers/2611.31977)
- Code: [WinterCCC/Distill-to-Loop](https://github.com/WinterCCC/Distill-to-Loop)
- CheckPaper report: [checkpaper.app/r/h7wsfn3seq](https://checkpaper.app/r/h7wsfn3seq)

## Findings

1. **More loops than trained.** Sec. 5.2 (p. 7): "As the loops continue to K = 8 and K = 16, the samples stay stable and do not degrade." Sec. 2 (p. 3) and the Conclusion (p. 9) set this against Looped-DiT, whose quality "drops once it runs more loops than it was trained with". The SD3-medium student is trained with K = 4. Its Table 1 rows (p. 7):

   | K | GenEval | ImageReward | PickScore | HPSv2.1 | Avg. |
   |---|---|---|---|---|---|
   | 4 | 0.659 | 0.919 | 22.312 | 0.276 | 100.7 |
   | 8 | 0.648 | 0.889 | 22.278 | 0.275 | 99.3 |
   | 16 | 0.633 | 0.853 | 22.229 | 0.273 | 97.6 |

   Every metric decreases with each step, and the K = 16 average is below the teacher's 100.0.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.31977v1, checks its hash, quotes the claims and the Table 1 rows, and checks the trend from K = 4 to 16.

## Status

[Asked the authors](https://github.com/WinterCCC/Distill-to-Loop/issues/2) on 2026-11-28.

# Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks (arXiv:2611.12875): consistency check

Click3R without clicks is reported with different numbers in different tables on the same pairs: 55.3 / 50.8 mAA@30 on Hard3DBench ID / OOD in Table 2 vs. 55.9 / 49.4 for K = 0 in Table 12, and 36.2 mAA@30 / 17.30° medRRE on the 100 human-click pairs in Table 3 vs. 35.6 / 18.64° in Tables 11 and 12.

## Paper

- Title: Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks
- arXiv: [2611.12875v1](https://arxiv.org/abs/2611.12875v1) (the version checked, sha256 `73ff83e9…3f55`)
- Hugging Face: [papers/2611.12875](https://huggingface.co/papers/2611.12875)
- Code: [UVA-Computer-Vision-Lab/click3r](https://github.com/UVA-Computer-Vision-Lab/click3r)
- CheckPaper report: [checkpaper.app/r/zq4q7rqaq4](https://checkpaper.app/r/zq4q7rqaq4)

## Findings

1. **No-click results differ across tables.**

   | Set | Metric | Table 2 / 3 | Table 11 / 12 |
   |---|---|---|---|
   | Hard3DBench 2-view ID (404 pairs) | mAA@30 | 55.3 (Table 2) | 55.9 (Table 12, K = 0) |
   | Hard3DBench 2-view OOD (300 pairs) | mAA@30 | 50.8 (Table 2) | 49.4 (Table 12, K = 0) |
   | 100 OOD pairs with human clicks | mAA@30 | 36.2 (Table 3) | 35.6 (Tables 11 and 12) |
   | 100 OOD pairs with human clicks | medRRE | 17.30° (Table 3) | 18.64° (Table 11) |

   With no clicks nothing is sampled, so the same model on the same pairs would be expected to give the same numbers. The text of App. E.6 uses the Table 12 values ("from 55.9 to 58.0", "from 49.4 to 59.6", "from 35.6 to 55.0"), while Sec. 4 uses the Table 3 values ("from 36.2 to 56.2").

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12875v1, checks its hash and quotes the four tables.

## Status

[Asked the authors](https://github.com/UVA-Computer-Vision-Lab/click3r/issues/1) on 2026-11-23.

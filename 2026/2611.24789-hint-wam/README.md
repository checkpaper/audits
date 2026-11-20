# HINT-WAM: Hindsight-Informed Training for World Action Models (arXiv:2611.24789): consistency checks

In Table 6, the velocity-matching row's t and sign-test p do not follow from its own difference, SE and win/loss counts; the other four rows do. Three LIBERO-90 rates are not attainable with 90 tasks × 50 trials.

## Paper

- Title: HINT-WAM: Hindsight-Informed Training for World Action Models
- arXiv: [2611.24789v1](https://arxiv.org/abs/2611.24789v1) (the version checked, sha256 `2ff80709…e859`)
- Hugging Face: [papers/2611.24789](https://huggingface.co/papers/2611.24789)
- Code: [tuandattt/hintwam_code](https://github.com/tuandattt/hintwam_code)
- CheckPaper report: [checkpaper.app/r/csy7qe5ga8](https://checkpaper.app/r/csy7qe5ga8)

## Findings

1. **HINT-WAM vs. velocity matching (Table 6, p. 13; Sec. 4.3, p. 8).** The row gives mean difference +6.16, SE 1.59, t 3.62, 48 wins / 17 losses, sign-test p 0.00042. 6.16 / 1.59 = 3.87, and rounding allows only 3.86 to 3.89; t = 3.62 implies SE ≈ 1.70. An exact two-sided sign test on 48 vs. 17 gives p = 0.00015. For the other four rows, diff / SE and the sign test reproduce the reported t and p.
2. **LIBERO-90 rates.** Every LIBERO-90 number uses 90 tasks × 50 trials (Sec. 4.1, App. D), so each rate is a multiple of 1/4500 (0.022 points). Three are not, under rounding or truncation: SFT with replay 76.70 (Table 2; nearest 76.689 / 76.711), MMD 80.63 (Sec. 4.3; 80.622 / 80.644), and noised demonstrations 80.74 (Sec. 6; 80.733 / 80.756). HINT-WAM's 85.18 and velocity matching's 79.02 do fit.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.24789v1, checks its hash, quotes Table 6 and the LIBERO-90 rates, recomputes t and the sign test for each row, and checks the rates against the 1/4500 grid.

## Status

Answered. [Asked the authors](https://github.com/tuandattt/hintwam_code/issues/2) on 2026-11-20.

The author (tuandattt) replied on 2026-11-20 and confirmed both points: the Table 6 row should read t = 3.87 and p = 0.00015, and the three rates were rounding mistakes, correct values 76.69 (Table 2), 80.62 (Sec. 4.3) and 80.73 (Sec. 6), all from 90 tasks × 50 trials. These are 3,451, 3,628 and 3,633 successes out of 4,500. The authors will fix them in the next version.
The author closed the issue as completed on 2026-11-20.

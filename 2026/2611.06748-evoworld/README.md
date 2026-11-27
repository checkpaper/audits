# EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models (arXiv:2611.06748): consistency check

Under the stated protocol (120 cases, three-level scores), every Subject Consistency and Reaction value must be a multiple of 1/240. Seven values in Tables 1 and 2 are not.

## Paper

- Title: EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models
- arXiv: [2611.06748v1](https://arxiv.org/abs/2611.06748v1) (the version checked, sha256 `9342ca25…2a32`)
- Hugging Face: [papers/2611.06748](https://huggingface.co/papers/2611.06748)
- Code: [Tommy-Bie/EvoWorld](https://github.com/Tommy-Bie/EvoWorld)
- CheckPaper report: [checkpaper.app/r/jy6v9gjxdk](https://checkpaper.app/r/jy6v9gjxdk)

## Findings

1. **Attainable values (Tables 1 and 2, pp. 7-8).** App. A says Event and Revisit success are binary, the other criteria (including Reaction Quality and Subject Consistency) use {0, 0.5, 1}, and three-level metrics are averaged over all 120 cases. A three-level mean is then k/240, i.e. a multiple of 0.417 points. All binary columns and most three-level values fit, but these do not:

   | Row | Column | Reported | Nearest attainable |
   |---|---|---|---|
   | LingBot-World | Subj. Cons. | 87.6 | 87.50 / 87.92 |
   | LingBot-World-v2 | Subj. Cons. | 82.6 | 82.50 / 82.92 |
   | SANA-WM | Subj. Cons. | 67.7 | 67.50 / 67.92 |
   | Echo-WM | Subj. Cons. | 97.6 | 97.50 / 97.92 |
   | Evoke | Subj. Cons. | 93.5 | 93.33 / 93.75 |
   | Evoke-Turbo | Subj. Cons. | 97.0 | 96.67 / 97.08 |
   | Stage 1 + IAA (Table 2) | React. | 83.9 | 83.75 / 84.17 |

   These values must come from a different number of cases or a different computation from the one App. A describes. All values in the EvoWorld rows fit.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.06748v1, checks its hash, quotes the protocol and tests every Table 1 value and the Table 2 row.

## Status

[Asked the authors](https://github.com/Tommy-Bie/EvoWorld/issues/1) on 2026-11-27.

# Termination Lag: Coding Agents Solve Early but Stop Late (arXiv:2611.14960): consistency checks

Table 1's Context growth row is printed in red, and the source marks it as means while the caption calls every row a median.

## Paper

- Title: Termination Lag: Coding Agents Solve Early but Stop Late
- arXiv: [2611.14960v1](https://arxiv.org/abs/2611.14960v1) (the version checked, sha256 `2c7586e6…0f26`; source sha256 `2f5fab9a…0f4b`)
- Hugging Face: [papers/2611.14960](https://huggingface.co/papers/2611.14960)
- Code: [musacim/termination-lag](https://github.com/musacim/termination-lag) (commit `eafa419`)
- CheckPaper report: [checkpaper.app/r/esutjs8d96](https://checkpaper.app/r/esutjs8d96)

## Findings

1. **Means or medians.** The Table 1 caption (p. 4) says "All rows below Solved are medians over solved runs". The Context growth cells (+30 / +28 / +78 / +55) are the only red text on the page, and the arXiv source line for that row ends with the comment `% TODO: these are MEANS; replace with medians`.
2. **What is measured.** The caption defines context growth as the relative increase in the model's input context from the first correct patch to the final step. The released `code/analysis/ctx_growth.py` takes the end context as prompt + output tokens of the last call, and by default uses the tab:post tasks rather than every solved run (`--all`). The script prints medians, so it is unclear which numbers the table shows. The trajectory logs needed to recompute them are not public.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads the arXiv PDF and source, and the released ctx_growth.py at a fixed commit, checks their hashes, lists the red text on p. 4, and prints the source comment and the code's definitions.

## Status

[Asked the authors](https://github.com/musacim/termination-lag/issues/1) on 2026-11-19.

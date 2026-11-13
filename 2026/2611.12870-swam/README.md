# SWAM: Scaling World Action Models with Cross-Modal Alignment (arXiv:2611.12870): consistency checks

One ablation success rate cannot occur with 50 tasks and 25 episodes per setting.

## Paper

- Title: SWAM: Scaling World Action Models with Cross-Modal Alignment
- arXiv: [2611.12870v2](https://arxiv.org/abs/2611.12870v2) (the version checked, sha256 `d2c727f1…6577`)
- Hugging Face: [papers/2611.12870](https://huggingface.co/papers/2611.12870)
- Code: [shaaaaron/SWAM](https://github.com/shaaaaron/SWAM)
- CheckPaper report: [checkpaper.app/r/dk2h55eark](https://checkpaper.app/r/dk2h55eark)

## Findings

1. **Table 4, Rephrased, Hard (C2R).** Section 4.1 (p. 11) evaluates the 50 RoboTwin tasks with 25 episodes each for ablations, so every ablation success rate is k/1250, a multiple of 0.08 points. 115 of the 116 values in Tables 3 to 9 are. The exception is 54.76 in Table 4, which would be 684.5 successes; the nearest values are 54.72 and 54.80. The 3.96-point gain over Original (50.80) quoted for this row inherits it.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12870v2, checks its hash, reads Tables 3 to 9, and tests each value against the k/1250 grid.

## Status

Contacting the authors, started 2026-11-13. Asked in [the SWAM repository](https://github.com/shaaaaron/SWAM/issues/2).

## Author response

None yet.

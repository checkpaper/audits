# WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training (arXiv:2610.37161): consistency checks

The abstract says larger models benefit more from additional task data; the paper's own numbers show the smallest model gaining most from 30K to 110K tasks.

## Paper

- Title: WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training
- arXiv: [2610.37161v3](https://arxiv.org/abs/2610.37161v3) (the version checked, sha256 `68b38117…abd4`)
- Hugging Face: [papers/2610.37161](https://huggingface.co/papers/2610.37161)
- Code: [IQuestLab/WorkFactory](https://github.com/IQuestLab/WorkFactory)
- CheckPaper report: [checkpaper.app/r/fr6ywwpbv9](https://checkpaper.app/r/fr6ywwpbv9)

## Findings

1. **Scaling claim.** The abstract says larger models benefit more from additional task data. From Table 2 and Section 4.3 (p. 9): the 4B model goes from 661 to about 1207 Elo at 30K tasks and 1375 at 110K (+168 from 30K to 110K); the 35B-A3B model reaches 88% of its 686-point gain by 30K, so about 1483, and 1565 at 110K (+82); the 27B model reaches 94% of its 637-point gain by 30K, so about 1574, and 1612 at 110K (+38). The additional data from 30K to 110K helps the 4B model most and the 27B model least.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.37161v3, checks its hash, finds the quoted numbers, and computes each model's gain from 30K to 110K tasks.

## Status

Contacting the authors, started 2026-11-13. Asked in [the WorkFactory repository](https://github.com/IQuestLab/WorkFactory/issues/2).

## Author response

None yet.

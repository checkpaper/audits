# MIRIX-2.0: Multi-Agent Memory System (arXiv:2611.12068): consistency checks

Two LongMemEval-S accuracies in Table 7 cannot occur on 300 questions scored right or wrong.

## Paper

- Title: MIRIX-2.0: Multi-Agent Memory System
- arXiv: [2611.12068v1](https://arxiv.org/abs/2611.12068v1) (the version checked, sha256 `f37c020d…617a`)
- Hugging Face: [papers/2611.12068](https://huggingface.co/papers/2611.12068)
- Code: [Mirix-AI/MIRIX](https://github.com/Mirix-AI/MIRIX)
- CheckPaper report: [checkpaper.app/r/dr4kk3v4fs](https://checkpaper.app/r/dr4kk3v4fs)

## Findings

1. **Table 7, LongMemEval-S.** Section 3.1 (p. 10) scores LongMemEval-S with a gpt-4o-mini judge and majority-of-3 voting, so each question is right or wrong; the three-run means are stated for the interactive agents only. Table 7 (p. 27) is "on the evaluated 300 questions", so every accuracy should be k/300. The five baselines and M1 (70.0) are. MIRIX-1.0 (M0) 58.8 and MIRIX-2.0 (M2) 72.6, the abstract's headline number, are not: the nearest values are 58.67 or 59.00, and 72.33 or 72.67. Both fit k/900, which is what averaging the three judge votes, or three runs, would give.
2. **LoCoMo judge in the released code.** `evals/llm_judge.py` at commit `9077e4b` makes a single gpt-4o-mini call at temperature 0 per answer, not three votes.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12068v1, checks its hash, reads Table 7, and tests each value against k/300 and k/900.

## Status

Contacting the authors, started 2026-11-17.

## Author response

None yet.

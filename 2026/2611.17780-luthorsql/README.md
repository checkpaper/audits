# LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent (arXiv:2611.17780): consistency checks

In the App. F handoff paragraph, 279 + 121 questions add up to 400, not the stated 330, and the "18% fewer logged tokens" is the tool-call row of Table 10, whose caption says logged token counts were not lower.

## Paper

- Title: LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent
- arXiv: [2611.17780v1](https://arxiv.org/abs/2611.17780v1) (the version checked, sha256 `9ce78b71…fd55`)
- Hugging Face: [papers/2611.17780](https://huggingface.co/papers/2611.17780)
- Code: [IAMIbrahimmemon/luthorsql](https://github.com/IAMIbrahimmemon/luthorsql)
- CheckPaper report: [checkpaper.app/r/bpdf6ja87f](https://checkpaper.app/r/bpdf6ja87f)

## Findings

1. **Question counts (p. 18).** "Of the 330 questions with candidates it took one on 279 (87% right) and wrote its own query on the other 121 (57% right)." 279 + 121 = 400. With 87% of 279 and 57% of 121, about 312 are right, and 312 / 400 = 78.00%, the accuracy Table 10 reports for the 400-question sample. The counts fit 400 questions, so 330 or the 279 / 121 split is off.
2. **Logged tokens (p. 18).** The same paragraph says the agent does "28% less agent time and 18% fewer logged tokens". In Table 10 the −18% row is tool calls (207 → 169), and the caption says "logged output-token counts were not lower".

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.17780v1, checks its hash, quotes the paragraph and Table 10, and recomputes the counts.

## Status

[Asked the authors](https://github.com/IAMIbrahimmemon/luthorsql/issues/2) on 2026-11-20.

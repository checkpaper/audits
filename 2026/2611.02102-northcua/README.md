# NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience (arXiv:2611.02102): consistency checks

One OSWorld 2.0 binary score is not a possible result on 108 tasks.

## Paper

- Title: NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience
- arXiv: [2611.02102v3](https://arxiv.org/abs/2611.02102v3) (the version checked, sha256 `51413a28…4c57`)
- Hugging Face: [papers/2611.02102](https://huggingface.co/papers/2611.02102)
- Code: [beipo-ai/NorthCUA](https://github.com/beipo-ai/NorthCUA)
- CheckPaper report: [checkpaper.app/r/d4e8wns5st](https://checkpaper.app/r/d4e8wns5st)

## Findings

1. **NorthCUA-Pro after SFT, OSWorld 2.0 binary.** Appendix (p. 57) evaluates OSWorld 2.0 on all 108 tasks with binary completion. Every NorthCUA binary score in Tables 9, 12 and 13 is k/108 (for example 9.3 = 10/108 and 30.6 = 33/108), except Pro after SFT, 27.3, whose nearest values are 26.85 and 27.78. 27.3 is also GPT-5.6 Sol's binary score in Table 9.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.02102v3, checks its hash, finds the quoted rows, and tests each NorthCUA binary score against k/108.

## Status

Not yet sent to the authors.

## Author response

None yet.

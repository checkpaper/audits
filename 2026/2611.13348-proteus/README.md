# ProTEUS: A mutation-resolved world model for closed-loop protein evolution (arXiv:2611.13348): consistency checks

The abstract says both campaigns gave variants with more than 10-fold activity; the aldehyde dehydrogenase campaign reports 6.85-fold, and the speed-up over AlphaFold 3 is 7.81 to 10.81-fold rather than more than 10.

## Paper

- Title: ProTEUS: A mutation-resolved world model for closed-loop protein evolution
- arXiv: [2611.13348v1](https://arxiv.org/abs/2611.13348v1) (the version checked, sha256 `f355287e…1c6c`)
- Hugging Face: [papers/2611.13348](https://huggingface.co/papers/2611.13348)
- Code: [yikunpku/ProTEUS](https://github.com/yikunpku/ProTEUS)
- CheckPaper report: [checkpaper.app/r/tvkevdqjmp](https://checkpaper.app/r/tvkevdqjmp)

## Findings

1. **Activity.** The abstract (p. 2) and introduction (p. 4) say both campaigns, levansucrase and aldehyde dehydrogenase, found variants with more than 10-fold wild-type activity, the introduction within 100 sequences. Levansucrase reaches 14.03-fold (p. 9). The best ALDH variant reaches 6.85-fold in the screen and 7.90-fold after normalizing for enzyme concentration (p. 11), after five rounds of 30 variants (Table S5, p. 54).
2. **Speed.** The abstract says the predictor is more than 10-fold faster than AlphaFold 3. Section results (p. 7) give AlphaFold 3 mean runtimes 7.81 to 10.81 times higher across five atom-count bins.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.13348v1, checks its hash, and finds each quoted passage.

## Status

Contacting the authors, started 2026-11-14. Asked in [the ProTEUS repository](https://github.com/yikunpku/ProTEUS/issues/1).

## Author response

None yet.

# RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild (arXiv:2611.02497): consistency checks

Section 4.2 describes Figure 5 with a score range and a success ceiling that the figure does not show.

## Paper

- Title: RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild
- arXiv: [2611.02497v1](https://arxiv.org/abs/2611.02497v1) (the version checked, sha256 `6a1d567b…265c`)
- Hugging Face: [papers/2611.02497](https://huggingface.co/papers/2611.02497)
- Code: [RoboColosseum/robocolosseum-client](https://github.com/RoboColosseum/robocolosseum-client)
- CheckPaper report: [checkpaper.app/r/zzuwhpk54q](https://checkpaper.app/r/zzuwhpk54q)

## Findings

1. **Figure 5 and Section 4.2.** Section 4.2 (p. 10) says MolmoAct2's expected comparison scores range from 58% to 77%, its success rates from 6% to 13%, and that no evaluated system exceeds 13% success in any category. In Figure 5 (p. 11), MolmoAct2's scores are 58, 59, 70, 69, 59 and 59 (no 77 appears anywhere in panel a), its success rates are 13, 6, 5, 11, 8 and 8, and four cells of panel c are above 13%: 25, 15, 14 and 14.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.02497v1, checks its hash, finds the Section 4.2 sentences, and reads the values printed in Figure 5.

## Status

Contacting the authors, started 2026-11-12. Asked in [the RoboColosseum client repository](https://github.com/RoboColosseum/robocolosseum-client/issues/1).

## Author response

None yet.

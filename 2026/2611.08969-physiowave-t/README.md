# PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals (arXiv:2611.08969): consistency check

The Introduction says RALF raises seizure event sensitivity at 11 false alarms per hour "from 61.4 % to 78.9 %", but the Abstract and Sec. 5.5 give 74.4 % for RALF and attribute 78.9 % to weighted-logit fusion.

## Paper

- Title: PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals
- arXiv: [2611.08969v1](https://arxiv.org/abs/2611.08969v1) (the version checked, sha256 `0e3fbb2b…9d2c`)
- Hugging Face: [papers/2611.08969](https://huggingface.co/papers/2611.08969)
- Code: [ForeverBlue816/PhysioWave](https://github.com/ForeverBlue816/PhysioWave)
- CheckPaper report: [checkpaper.app/r/pqqbtd28er](https://checkpaper.app/r/pqqbtd28er)

## Findings

1. **RALF event sensitivity (pp. 1, 2, 10).** Abstract: "from 61.4 % to 74.4 % with RALF". Introduction: "RALF raises event sensitivity at 11 false alarms per hour from 61.4 % to 78.9 %". Sec. 5.5: "to 74.4 % with RALF and 78.9 % with weighted-logit fusion". The Introduction appears to credit RALF with the weighted-logit number.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.08969v1, checks its hash and quotes the three statements.

## Status

[Asked the authors](https://github.com/ForeverBlue816/PhysioWave/issues/3) on 2026-11-23.

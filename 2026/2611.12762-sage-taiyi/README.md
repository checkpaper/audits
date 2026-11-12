# Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery (arXiv:2611.12762): consistency checks

The metamaterial reward reported for the best design does not follow from Eq. (4) and the reported transmissions.

## Paper

- Title: Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery
- arXiv: [2611.12762v1](https://arxiv.org/abs/2611.12762v1) (the version checked, sha256 `ee522780…e524`)
- Hugging Face: [papers/2611.12762](https://huggingface.co/papers/2611.12762)
- Code: [Alpha-Innovator/Sage-Taiyi](https://github.com/Alpha-Innovator/Sage-Taiyi)
- CheckPaper report: [checkpaper.app/r/txhjk6fqpb](https://checkpaper.app/r/txhjk6fqpb)

## Findings

1. **Metamaterial reward.** Eq. (4) (p. 25) defines the reward as T_pass − 1.5 T_stop. The best design has average passband and stopband transmissions of 94.5% and 6.2% (p. 25, Table 6). Eq. (4) then gives 0.945 − 1.5 × 0.062 = 0.852, and at least 0.8508 after rounding, while the text, Fig. 16f and Table 6 report 0.822.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12762v1, checks its hash, finds the quoted text, and evaluates Eq. (4).

## Status

Not yet sent to the authors.

## Author response

None yet.

# Coda-DaVinci: Reimagining Video Generation with Code2Video (arXiv:2611.26595): consistency checks

Table 2's G1/PE1 row of P1 − P0 changes does not follow from the Table 1 averages, and by Table 1 naturalness drops under P1 for G1/PE1, against the claim that it improves under every comparison.

## Paper

- Title: Coda-DaVinci: Reimagining Video Generation with Code2Video
- arXiv: [2611.26595v1](https://arxiv.org/abs/2611.26595v1) (the version checked, sha256 `7d6bad4f…7ec4`)
- Hugging Face: [papers/2611.26595](https://huggingface.co/papers/2611.26595)
- Code: [FrankYang-17/Coda](https://github.com/FrankYang-17/Coda)
- CheckPaper report: [checkpaper.app/r/xee3f99np4](https://checkpaper.app/r/xee3f99np4)

## Findings

1. **G1/PE1 row (Table 2, p. 8 vs Table 1, p. 7).** Table 2 lists P1 − P0 changes of the three-benchmark averages. From the Table 1 average columns, G1/PE1 gives C +0.253, I +0.284, P +0.005, N −0.018 (mean +0.131); Table 2 gives +0.200, +0.250, +0.062, +0.012 (mean +0.131). The G1/PE2 row, by contrast, matches Table 1 exactly (+0.149, +0.191, +0.223, +0.096).
2. **Naturalness "under every tested P0/P1 comparison" (p. 8).** The text says Table 2 shows improvements in the four-metric mean and the naturalness and realism average under every comparison. By Table 1, N for G1/PE1 falls from 1.968 (P0) to 1.950 (P1).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.26595v1, checks its hash, quotes the passages and tables above, and recomputes the numbers.

## Status

Answered. [Asked the authors](https://github.com/FrankYang-17/Coda/issues/1) on 2026-11-21.

An author replied on 2026-11-24 and closed the issue. Table 1 averages all available ratings (94 cases for G1/P0/PE1, 80 for G1/P1/PE1); Table 2 uses the 80 common complete cases, excluding 14 Principia cases where P1 generation failed, giving +0.200 / +0.250 / +0.062 / +0.012. On that subset P0 naturalness is about 1.938 versus 1.950 for P1, so it does increase. The revision will state the paired sample sizes and qualify the claim to the common complete-case subsets.

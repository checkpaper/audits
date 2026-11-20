# Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus (arXiv:2611.22668): consistency checks

On CelebA, the target-only (single-view) WGA is 84.27 in Tables 4 and 5 but 82.39 in the Discussion, under a setup that keeps the same ERM model and 10 classifier seeds and gives the same CHORD value, 89.06.

## Paper

- Title: Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus
- arXiv: [2611.22668v1](https://arxiv.org/abs/2611.22668v1) (the version checked, sha256 `99a8228f…d9ad`)
- Hugging Face: [papers/2611.22668](https://huggingface.co/papers/2611.22668)
- Code: [davelee-uestc/chord_debiasing_public](https://github.com/davelee-uestc/chord_debiasing_public)
- CheckPaper report: [checkpaper.app/r/ykapgejbk5](https://checkpaper.app/r/ykapgejbk5)

## Findings

1. **Target-only WGA on CelebA (p. 7 vs p. 8).** Table 4 lists "Single View 84.27" and Table 5 starts from "Target Only: 84.27", both against CHORD 89.06, as means over ten seeds. The Discussion keeps "the ERM model and the final transformation fixed, averaging 10 classifier seeds" and reports "Target-only achieves 82.39% WGA", again with CHORD at 89.06. The two target-only values differ by 1.88 points. 84.27 is also the CelebA WGA of the NSF baseline in Table 1.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.22668v1, checks its hash, and quotes Tables 1, 4 and 5 and the Discussion.

## Status

Answered. [Asked the authors](https://github.com/davelee-uestc/chord_debiasing_public/issues/2) on 2026-11-20.

The author (davelee-uestc) replied on 2026-11-20: "82.39% is the target-only result from our released checkpoint, used in the paired Discussion experiment. In Tables 4–5, we use the higher, previously reported NSF result of 84.27% to avoid overstating CHORD's improvement. The two values therefore correspond to different checkpoint settings." The paper does not say this in Tables 4 and 5; we suggested adding it to the captions.
The author closed the issue as completed on 2026-11-20.

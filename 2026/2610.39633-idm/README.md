# Intrinsic Distribution Matching (arXiv:2610.39633): consistency checks

The APEX (Z-Image) numbers behind the headline comparison do not appear in the APEX paper the table cites.

## Paper

- Title: Intrinsic Distribution Matching
- arXiv: [2610.39633v1](https://arxiv.org/abs/2610.39633v1) (the version checked, sha256 `0d7e5a41…ea27`)
- Hugging Face: [papers/2610.39633](https://huggingface.co/papers/2610.39633)
- Code: [inclusionAI/IDM](https://github.com/inclusionAI/IDM)
- CheckPaper report: [checkpaper.app/r/uymda66g7g](https://checkpaper.app/r/uymda66g7g)

## Findings

1. **The APEX row of Table 5.** Section 5.2 (p. 9) says IDM improves over APEX by 3.87 and 1.44 points on LongText-CN and LongText-EN. The Table 5 caption (p. 12) calls row A "the published Z-Image reference" of APEX (Liu et al., 2026a), cited as arXiv:2604.12322. That paper (v1) does not mention Z-Image, OneIG or LongText, and none of the five row-A values (52.60, 77.23, 88.64, 90.38, 88.76) appears in it. The APEX repository README mentions only an experimental Z-Image-Turbo release, without these numbers.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2610.39633v1 and arXiv 2604.12322v1, checks both hashes, finds the quoted passages in IDM, and counts the row-A values in the APEX paper.

## Status

Contacting the authors, started 2026-11-13. Asked in [the IDM repository](https://github.com/inclusionAI/IDM/issues/2).

## Author response

None yet.

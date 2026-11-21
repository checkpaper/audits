# Recurrent Domain Incremental Adaptation of Time-Series Foundation Models (arXiv:2611.24075): consistency checks

App. C.1 says that on WISDM "replay [is] ahead by 1.54 points", but Table 4 puts PACT ahead (0.8775 vs 0.8621, +1.54); and Sec. 4.1 says Table 1 averages three training seeds, while Table 4 lists two seeds for WISDM and UCI-HAR.

## Paper

- Title: Recurrent Domain Incremental Adaptation of Time-Series Foundation Models
- arXiv: [2611.24075v1](https://arxiv.org/abs/2611.24075v1) (the version checked, sha256 `e7a7dd18…35e1`)
- Hugging Face: [papers/2611.24075](https://huggingface.co/papers/2611.24075)
- Code: [Sachithx/PACT](https://github.com/Sachithx/PACT)
- CheckPaper report: [checkpaper.app/r/j9qu7eegth](https://checkpaper.app/r/j9qu7eegth)

## Findings

1. **Sign of the WISDM gap (App. C.1, p. 16).** "The WISDM ordering changed when averaged over two seeds, with replay ahead by 1.54 points." Table 4 gives PACT 0.8775 ± 0.0173 and embedding replay 0.8621 ± 0.0008, so PACT is ahead by 1.54 points.
2. **Seeds behind Table 1 (Sec. 4.1, p. 6).** "Table 1 reports the mean over three training seeds and four fixed streams per dataset." The Seeds column of Table 4 is 3 for FD, HHAR and Sleep-EDF and 2 for WISDM and UCI-HAR.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.24075v1, checks its hash, quotes Sec. 4.1, App. C.1 and Table 4, and redoes the WISDM difference.

## Status

[Asked the authors](https://github.com/Sachithx/PACT/issues/1) on 2026-11-22.

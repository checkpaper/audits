# StreamDuo: A Live Commentator and a Research Agent for Unseen Games (arXiv:2611.01120): consistency checks

The Proact-VL baseline row in Table 2 is the Table 1 run, which leaks 9.9%; Appendix A gives 5.8% for the same recipe under StreamDuo's inference settings.

## Paper

- Title: StreamDuo: A Live Commentator and a Research Agent for Unseen Games
- arXiv: [2611.01120v1](https://arxiv.org/abs/2611.01120v1) (the version checked, sha256 `33d3bf62…82e3c2`)
- Hugging Face: [papers/2611.01120](https://huggingface.co/papers/2611.01120)
- Code: [ZixianGao/StreamDuo-code](https://github.com/ZixianGao/StreamDuo-code)
- CheckPaper report: [checkpaper.app/r/vj75td35e6](https://checkpaper.app/r/vj75td35e6)

## Findings

1. **Which Proact-VL run is the baseline.** Section 4.3 (p. 7) says all Table 2 rows use the same inference settings and that the first row follows the Proact-VL recipe. That row (p. 8) equals the Proact-VL row of Table 1 in all nine columns, and Table 5 (p. 15) gives that run 9.9% leakage, the figure in the abstract ("from 9.9% to 1.0%"). Appendix A (p. 15) says that, run with the same inference settings as StreamDuo, the Proact-VL recipe leaks 5.8%. Both cannot describe the same run.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.01120v1, checks its hash, and finds the quoted rows and sentences.

## Status

Contacting the authors, started 2026-11-13. Asked in [the StreamDuo repository](https://github.com/ZixianGao/StreamDuo-code/issues/1).

## Author response

None yet.

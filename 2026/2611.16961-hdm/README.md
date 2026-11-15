# HDM (arXiv:2611.16961): consistency checks

In Table 2, routed HDM-4B has a lower median latency on JevBench (0.179 s) than fast-only HDM-4B (0.226 s), although the paper says routing always runs the fast pass first.

## Paper

- Title: The Value of Thinking: Learning When to Reason in Hybrid Decision Models
- arXiv: [2611.16961v1](https://arxiv.org/abs/2611.16961v1) (the version checked, sha256 `936847cd…0d32a3f7e`)
- Hugging Face: [papers/2611.16961](https://huggingface.co/papers/2611.16961)
- Code: [zhengxuyu/HDM-code](https://github.com/zhengxuyu/HDM-code)
- CheckPaper report: [checkpaper.app/r/j7cuz33z7g](https://checkpaper.app/r/j7cuz33z7g)

## Findings

1. **Routed versus fast-only latency.** The Figure 2 caption (p. 2) says routing occurs once and the model either returns the cached fast answer or decodes autoregressively, and Sec. 1 (p. 3) says the block reads representations the fast pass has already computed. So every routed item costs at least its fast-only time, and the median does too. Table 2 (p. 6) gives HDM-4B fast only a P50 of 0.226 s and HDM-4B routed (30% escalated) a P50 of 0.179 s, 20.8% lower. The abstract's 0.179 s against Jev's 0.652 s (−72.5%) uses the routed value; a routed P50 of at least 0.226 s would put the reduction at most at 65.3%.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.16961v1, checks its hash, finds the quoted passages and values, and compares the two P50 values.

## Status

Contacting the authors, started 2026-11-16. Asked in [the HDM repository](https://github.com/zhengxuyu/HDM-code/issues/4).

## Author response

None yet.

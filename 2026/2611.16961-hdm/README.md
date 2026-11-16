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

Explained and to be corrected. The authors said on 2026-11-16 that the timing order inflated the fast-only P50: it was always timed first on each item (a cold-start cost on new prompt lengths) and right after a thinking pass. Timed warm, fast only is 0.154 s and routed at λ = 0 is 0.176 s; the next revision will correct the fast-only row and report the mean next to the median. Asked in [the HDM repository](https://github.com/zhengxuyu/HDM-code/issues/4); answered on [the Hugging Face paper page](https://huggingface.co/papers/2611.16961).

## Author response

2026-11-16, on the Hugging Face paper page (excerpt):

> Both rows come from the same run and the same timer. [...] Fast only is always timed first on each item, so it paid this cost on 166 of the 231 items. The routed rows never paid it. [...] A fast pass that comes right after a thinking pass is slower by about 0.03 to 0.04 s [...]
>
> | | P50 as published | P50 with the fast pass timed warm | Mean |
> | --- | --- | --- | --- |
> | Fast only | 0.226 s | 0.154 s | 0.43 s |
> | Routed, λ = 0 | 0.179 s | 0.176 s | 4.8 s |
> | Always thinking | 3.86 s | not remeasured | 9.8 s |
>
> We will correct the fast-only row and report the mean next to the median in the next revision.

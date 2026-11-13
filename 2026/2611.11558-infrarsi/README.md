# InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure (arXiv:2611.11558): consistency checks

The experience-seeded Qwen3.5-9B run in the text matches none of the experience conditions in Table 5.

## Paper

- Title: InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure
- arXiv: [2611.11558v1](https://arxiv.org/abs/2611.11558v1) (the version checked, sha256 `d6f23500…45c2`)
- Hugging Face: [papers/2611.11558](https://huggingface.co/papers/2611.11558)
- Code: [TokenRhythm/InfraRSI](https://github.com/TokenRhythm/InfraRSI)
- CheckPaper report: [checkpaper.app/r/tywq7h36zq](https://checkpaper.app/r/tywq7h36zq)

## Findings

1. **First-trial and final speedup on Qwen3.5-9B (8×H100).** Section 4.1 (p. 8) says the experience-seeded first start reaches 1.55× on Trial 1 and search then reaches 1.73×; Section 6.1 (p. 13) gives the same 1.73×. Table 5 (p. 14) reports three experience conditions for this workload: cold start 1.22× (Trial 2) to 1.70×, all eligible packs 1.24× (Trial 1) to 1.70×, and cross-SKU transfer 1.23× (Trial 1) to 1.82×. Neither 1.55× nor 1.73× appears. Figure 4(a) also plots an "All packs" condition that Table 5 does not list.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.11558v1, checks its hash, and finds the quoted sentences and the three Table 5 rows.

## Status

Resolved. The authors confirmed on 2026-11-13 that 1.55× is a typo for 1.23×, explained the 1.73× as run-to-run variance and a different endpoint metric under the same condition, and will clarify the captions and the Figure 4 label in v2. Asked in [the InfraRSI repository](https://github.com/TokenRhythm/InfraRSI/issues/1).

## Author response

2026-11-13, YuchuanTian, in [the issue](https://github.com/TokenRhythm/InfraRSI/issues/1):

> 1. **Section 4.1 (`1.55×` on Trial 1):** Good catch — `1.55×` is an editing typo. In the Table 4 run, Trial 1 (knob-only warm start) actually reached **`1.23×`** (`1.6165s → 1.3118s`), matching Table 5 (`1.22×–1.24×`), before code search advanced to `1.73×`. We will correct this to `1.23×` in `v2`.
> 2. **Table 4 (`1.73×`) vs. Table 5 (`1.70× / 1.70× / 1.82×`):** Table 4 is **not** a fourth condition — it uses the same *All eligible packs* setting as Table 5 (and Table 6B's default arm at `1.74×`). The difference reflects (a) run-to-run variance across independent suites (`1.73×`, `1.70×`, `1.74×`), and (b) endpoint metric: Table 4 reports best verified screen speedup within the `$10` cutoff (`1.7303×`; paired re-run `1.72×`), whereas Table 5 reports fresh back-to-back paired re-runs. We will clarify both in the `v2` captions.
> 3. **Figure 4 `"All packs"`:** Figure 4(a) plots only three curves; `"All packs"` is just the shortened x-axis label for *All eligible packs* in Figure 4(b) (`get_text()` merges both panels). We will unify the label in `v2`.

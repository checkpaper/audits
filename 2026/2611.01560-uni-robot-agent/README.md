# Democratizing Robot-Use Agents: A Unified Harness with Open Models (arXiv:2611.01560): consistency checks

Section 5.1 reports depth retention for GPT-6 Astra from a 42-episode run; the 252-episode run in Table 1 gives a lower value.

## Paper

- Title: Democratizing Robot-Use Agents: A Unified Harness with Open Models
- arXiv: [2611.01560v2](https://arxiv.org/abs/2611.01560v2) (the version checked, sha256 `ffbc3556…e92d`)
- Hugging Face: [papers/2611.01560](https://huggingface.co/papers/2611.01560)
- Code: [Open-RUA/uni-robot-agent](https://github.com/Open-RUA/uni-robot-agent)
- CheckPaper report: [checkpaper.app/r/gsvcy9x36q](https://checkpaper.app/r/gsvcy9x36q)

## Findings

1. **Depth retention.** Section 5.1 (p. 16) reports that GPT-6 Astra keeps 98.6% of its score without depth (55.83 to 55.04), against 87.5% for Qwen, from one seed and one layout per task for Astra. Table 1 (p. 10) reports the same configuration on 252 episodes as 56.76 with depth and 51.90 without, which is 91.4%, a larger drop (4.86 points) than Qwen's (4.50).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.01560v2, checks its hash, finds the Section 5.1 sentence and the two Table 1 rows, and computes both ratios.

## Status

Contacting the authors, started 2026-11-12. Asked in [the uni-robot-agent repository](https://github.com/Open-RUA/uni-robot-agent/issues/39).

## Author response

None yet.

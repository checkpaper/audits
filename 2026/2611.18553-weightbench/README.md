# WeightBench: Evaluating Language Models as Weight-Space Programmers (arXiv:2611.18553): consistency checks

Two counts do not add up: with two samples per task on 42 tasks the Claude models should have 84 runs each, but Table 1 gives 78, 77 and 77; and 29 cheat scenarios plus 30 honest controls at three trials each make 177 runs, not the 180 stated in App. D.

## Paper

- Title: WeightBench: Evaluating Language Models as Weight-Space Programmers
- arXiv: [2611.18553v1](https://arxiv.org/abs/2611.18553v1) (the version checked, sha256 `53180822…5bf5`)
- Hugging Face: [papers/2611.18553](https://huggingface.co/papers/2611.18553)
- Code: [Aayush-Marasini/WeightBench](https://github.com/Aayush-Marasini/WeightBench)
- CheckPaper report: [checkpaper.app/r/8bupnh7afk](https://checkpaper.app/r/8bupnh7afk)

## Findings

1. **Runs per model (Sec. 5, p. 4; Table 1, p. 5).** "two samples per task for the Claude models and one for DeepSeek and GPT-6.1-sol". Table 1 lists 42 tasks for each Claude model and 78, 77 and 77 runs, against 2 × 42 = 84. The DeepSeek and GPT-6.1-sol columns (42 and 38 runs) match one sample per task.
2. **Red-team runs (App. D, pp. 8–9).** "29 cheat scenarios … and 30 honest controls", "three independent trials per scenario on the cluster (180 total runs)". (29 + 30) × 3 = 177. The 90 honest trials match 30 × 3, so the 180 would need 30 cheat scenarios.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.18553v1, checks its hash, quotes Sec. 5, Table 1 and App. D, and redoes both counts.

## Status

Answered. [Asked the authors](https://github.com/Aayush-Marasini/WeightBench/issues/5) on 2026-11-22.

The first author replied on 2026-11-21: "two samples per task" is imprecise. The 35 CPU tasks have two samples per Claude model (70 runs); the 7 GPU tasks ran once per model, giving 77 for Sonnet and Opus, and Haiku has one extra sample on TR02-LOOP-001 (78). The red-team array has 30 scenarios, 29 cheats plus one non-cheat (elementwise_update), so 30 × 3 + 30 controls × 3 = 180. Both will be reworded in the next version.

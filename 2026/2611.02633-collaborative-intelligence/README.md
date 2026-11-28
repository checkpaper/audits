# Measuring AI Agents as Teammates with Collaborative Intelligence (arXiv:2611.02633): consistency check

The paper says every model runs on all 240 tasks, and Table 2 labels "Solved alone" as out of 240. The released result cards show that some models are scored on fewer tasks because runs blocked by the provider are excluded: Claude Fable 5.1 on 192 of 240, Claude Opus 5.5 on 230. The paper does not mention these exclusions.

## Paper

- Title: Measuring AI Agents as Teammates with Collaborative Intelligence
- arXiv: [2611.02633v1](https://arxiv.org/abs/2611.02633v1) (the version checked, sha256 `8d3f6ba1…0602`)
- Hugging Face: [papers/2611.02633](https://huggingface.co/papers/2611.02633)
- Code: [zou-group/collaborative-intelligence](https://github.com/zou-group/collaborative-intelligence) (commit `6b26899` checked)
- CheckPaper report: [checkpaper.app/r/s7ehj5p5sj](https://checkpaper.app/r/s7ehj5p5sj)

## Findings

1. **Tasks scored per model.** Sec. 3 (p. 5): "Every model runs on all 240 tasks, both public and held-out". Table 2 (p. 5) gives "Solved alone" under the header "of 240 tasks". The released cards match Table 2's scores and solved-alone counts, and also record how many tasks were excluded for provider refusals:

   | Model | Scored tasks | Excluded (public / held-out) | Solved alone | Score |
   |---|---|---|---|---|
   | Claude Fable 5.1 | 192 of 240 | 48 (35 / 13) | 186 | 65.3 |
   | Claude Opus 5.5 | 230 of 240 | 10 (7 / 3) | 227 | 71.0 |
   | Claude Opus 5.5 high | 228 of 240 | 12 (9 / 3) | 227 | 76.8 |

   The paper's text does not mention provider refusals or excluded tasks.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.02633v1 and three result cards at the checked commit, checks their hashes, quotes the claims and Table 2 rows, and prints the scored and excluded task counts.

## Status

[Asked the authors](https://github.com/zou-group/collaborative-intelligence/issues/2) on 2026-11-28.

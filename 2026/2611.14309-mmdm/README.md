# MMDM (arXiv:2611.14309): release check

The released `selection.json` records a final filtering step that the paper does not describe: Jev 1.13.0 scored 5,000 hard single-select items, and the 1,015 items with its lowest-entropy (most confident) answers were removed.

## Paper

- Title: MMDM: Measuring Massive Multitask Decision Making
- arXiv: [2611.14309v1](https://arxiv.org/abs/2611.14309v1) (the version checked, sha256 `0fa6ef2d…0f94787c`)
- Hugging Face: [papers/2611.14309](https://huggingface.co/papers/2611.14309), dataset [shenjunhao/mmdm](https://huggingface.co/datasets/shenjunhao/mmdm)
- Code: [mmdm-benchmark/mmdm](https://github.com/mmdm-benchmark/mmdm)
- CheckPaper report: [checkpaper.app/r/gc48exbwk9](https://checkpaper.app/r/gc48exbwk9)

## Findings

1. **Undescribed filter.** `selection.json` (dataset commit [016dacdf](https://huggingface.co/datasets/shenjunhao/mmdm/blob/016dacdfd56c47128990539cc3c106a4a0b794ce/selection.json), copied here under the dataset's MIT licence) gives model "Jev 1.13.0", a pool of 5,000 hard single-select items, and the rule "Sort all rows per category by entropy … remove affordable prefix". It removed 1,015 items (992 answered correctly by Jev 1.13.0) and kept 3,985; with 1,463 items outside the pool this gives the paper's 5,448. The filter lowers Jev 1.13.0's accuracy on the pool from 72.82% to 66.47%. The paper describes five-model majority screening and expert review (Sec. 3.2, p. 5) but never mentions entropy or Jev 1.13; Jev 1.14.0 is then compared with other models in Table 2 (p. 6).
2. **OpenJev 4B.** One of the five representative models in Figure 1 is cited in the third person as (Shen, 2026) (p. 2). It is hosted at [shenjunhao/OpenJev-4B](https://huggingface.co/shenjunhao/OpenJev-4B), the account that hosts the dataset; the first author is Junhao Shen. The paper does not state the relationship.
3. **Release history.** On 2026-11-13 at 14:10 UTC the dataset was republished as a single commit (`1551e88c`) without `selection.json`. The earlier commit is still reachable by its hash.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.14309v1, checks its hash, checks the hash of the copied `selection.json`, recomputes the counts and accuracies, and searches the paper for the filter.

## Status

Asked the authors by email on 2026-11-13.

## Author response

None yet.

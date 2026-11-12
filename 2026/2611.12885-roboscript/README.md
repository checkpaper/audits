# World In-Context Learning for Agentic Robot Manipulation (arXiv:2611.12885): consistency checks

Three numbers in the rehearsal experiment cannot occur with 11 tasks and 10 episodes per setting.

## Paper

- Title: World In-Context Learning for Agentic Robot Manipulation
- arXiv: [2611.12885v1](https://arxiv.org/abs/2611.12885v1) (the version checked, sha256 `d45eb61a…045c`)
- Hugging Face: [papers/2611.12885](https://huggingface.co/papers/2611.12885)
- Code: [ArcheOne-AI/RoboScript](https://github.com/ArcheOne-AI/RoboScript)
- CheckPaper report: [checkpaper.app/r/873znwdynf](https://checkpaper.app/r/873znwdynf)

## Findings

1. **Rehearsal on the 11 harder tasks.** Section 5.4 (p. 12) reports 46.1% without rehearsal, 54.5% with it, a gain of 8.4 points, and 13.3 points under randomization. Section 5.1 (p. 8) evaluates each task on 10 episodes per setting. Over 11 tasks a one-setting success rate is then k/110 and a two-setting mean is k/220. 54.5% = 120/220 fits. 46.1% does not (nearest 45.91 and 46.36), nor does the 8.4-point gain (8.18 or 8.64), nor the 13.3-point gain in one setting (12.73 or 13.64).

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.12885v1, checks its hash, finds the quoted sentences, and tests each number against the k/110 and k/220 grids.

## Status

Resolved. The authors confirmed the finding on 2026-11-12 and will correct the paper in the next arXiv version. Asked in [the RoboScript repository](https://github.com/ArcheOne-AI/RoboScript/issues/1).

## Author response

2026-11-12, FangHeng (repository collaborator), in [the issue](https://github.com/ArcheOne-AI/RoboScript/issues/1):

> Thanks for checking. Your arithmetic is right, and your first guess is the cause: one cell has 9 episodes instead of 10. In the w/o-rehearsal arm, put_bottles_dustbin (randomized) has one seed whose scene could not be generated: the official expert pre-check fails or the initial scene is unstable. We marked that episode as non-evaluable and excluded it from the paired comparison, so that arm is 101/219, not out of 220.
>
> 101/219 = 46.1%, 120/220 = 54.5% (gain 8.4); randomized 42/109 vs 57/110 (gain 13.3).
>
> Per-task successes (w/o rehearsal → full | clean / randomized, 10 episodes each unless noted):
>
> | Task                  | w/o rehearsal     | full          |
> |-----------------------|-------------------|---------------|
> | hanging_mug           | 1 / 2             | 3 / 1         |
> | stack_bowls_three     | 4 / 3             | 4 / 6         |
> | put_bottles_dustbin   | 8 / 3 (of 9)      | 7 / 7         |
> | place_bread_skillet   | 4 / 5             | 5 / 8         |
> | move_can_pot          | 9 / 3             | 6 / 2         |
> | rotate_qrcode         | 3 / 3             | 5 / 2         |
> | open_microwave        | 10 / 10           | 10 / 10       |
> | place_fan             | 5 / 0             | 3 / 4         |
> | place_dual_shoes      | 6 / 9             | 9 / 8         |
> | pick_dual_bottles     | 1 / 4             | 4 / 2         |
> | put_object_cabinet    | 8 / 0             | 7 / 7         |
> | Total                 | 59/110 / 42/109   | 63/110 / 57/110 |
>
> We will add this to the paper in the next arXiv version.

The per-task counts reproduce all four numbers: 101/219 = 46.12%, 120/220 = 54.55%, a gain of 8.43, and 57/110 − 42/109 = 13.29 points under randomization.

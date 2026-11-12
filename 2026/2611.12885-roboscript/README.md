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

Contacting the authors, started 2026-11-12. Asked in [ArcheOne-AI/RoboScript#1](https://github.com/ArcheOne-AI/RoboScript/issues/1).

## Author response

None yet.

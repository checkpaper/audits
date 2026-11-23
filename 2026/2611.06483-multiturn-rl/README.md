# What Does Multi-Turn RL Really Improve in LLM Agents? (arXiv:2611.06483): source check

In the arXiv LaTeX source, the figure environments of Figures 2, 3 and 6 each carry a comment saying the plotted values are synthetic design previews to be replaced with measured results.

## Paper

- Title: What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?
- arXiv: [2611.06483v1](https://arxiv.org/abs/2611.06483v1) (PDF sha256 `246a6568…8518010d`; source sha256 `b4a08acd…6cf31d1b`)
- Hugging Face: [papers/2611.06483](https://huggingface.co/papers/2611.06483)
- Code: [GaryStack/Rethinking-Agent-RL](https://github.com/GaryStack/Rethinking-Agent-RL)
- CheckPaper report: [checkpaper.app/r/f4syhhg4h9](https://checkpaper.app/r/f4syhhg4h9)

## Findings

1. **Figure 2 (Pass@K, p. 3).** `iclr2027_conference.tex` lines 480–482, directly above `\includegraphics{figures/pass_at_k_grid_4tasks_grpo__red_gray_shaded.pdf}`: "PREVIEW FIXTURE: values are synthetic design previews from report_figures_rlve_rethinking; replace with measured results before submission and keep the CSV provenance in sync."
2. **Figure 3 (Pass@T, p. 4).** Line 504, above `pass_at_t_grid_4tasks__red_gray_shaded.pdf`: "PREVIEW FIXTURE: synthetic design preview; replace with measured results."
3. **Figure 6 (action quality by depth, p. 6).** Lines 594–596, above `quality_by_turn_combined__orig_colors.pdf`: "PREVIEW FIXTURE: values are synthetic design previews from report_figures_rlve_rethinking (figure_5_single_tasks fixtures); replace with measured results before submission."

All three figures appear in the compiled v1 PDF. Figures 2 and 3 support Takeaways 3.1 and 3.2, and Figure 6 supports Takeaway 3.3. The comments may be stale and the figures may have been regenerated from measured runs; the source alone cannot tell.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads the v1 PDF and the v1 source archive, checks both hashes, prints the three figure environments from the LaTeX source, and confirms each caption in the PDF.

## Status

[Asked the authors](https://github.com/GaryStack/Rethinking-Agent-RL/issues/1) on 2026-11-23. Asked the authors by email on 2026-11-11.

## Author response

None yet.

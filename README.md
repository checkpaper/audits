# CheckPaper Audits

Reproducible consistency checks of influential research papers. Each audit lists numbers in a paper that disagree with its own tables, figures or cited sources, and ships a script that recomputes them from the original PDF.

We check papers people are reading right now: Hugging Face Daily Papers, widely covered studies and papers under public discussion. Findings come from [CheckPaper](https://checkpaper.app), an AI paper review tool, and a person verifies every one before it appears here.

## Audits

| Paper | Finding | Status |
| --- | --- | --- |
| [DeepSeek-V4.1-Flash](2026/2609.19969-deepseek-v4.1-flash/) (arXiv:2609.19969) | World knowledge claim versus Table 1; 5% to 10% claim versus Figure 6 | [Asked the authors](https://huggingface.co/papers/2609.19969) |
| [LimiX-2](2026/2609.17488-limix-2/) (arXiv:2609.17488) | Table 7 PATHFINDER results imply 137 to 189 edges; the cited network has 195 | [Explained by the authors](https://github.com/limix-ldm-ai/LimiX/issues/66): constant variable F72 and its 7 edges removed, 188 edges |
| [MDMA-assisted therapy for severe PTSD](2026/s41591-021-01336-3-mdma-ptsd-phase-3/) (Nature Medicine 2021) | Within-group CIs centred on the negative of their estimates; SDS CI includes zero while P = 0.0116 | Contacting the authors |
| [Sugar-rich foods and antibiotic microbiome disruption](2026/s41586-026-11077-3-sugar-antibiotics-microbiome/) (Nature 2026) | Fig. 4 title names E. faecalis, the data are E. faecium; Fig. 3a legend HR 0.72 versus 0.59 in Supplementary Table 4 | Contacting the authors |
| [Axion 1.0](2026/2611.03233-axion-1.0/) (arXiv:2611.03233) | Headline BioMysteryBench 41.7% does not fit the 17-question grid of every other score | [Confirmed by the authors](https://github.com/bytedance/axion1_0/issues/5); 17-question set, corrected in the updated paper |
| [Harness-S](2026/2611.04277-harness-s/) (arXiv:2611.04277) | Table 1 described as three-run means, but 149 of 150 cells are single-run values | [Asked the authors](https://github.com/DeepExperience/Harness-S/issues/1) |
| [CoworkOS](2026/2611.03178-coworkos/) (arXiv:2611.03178) | Several OfficeQA Pro scores are not k/133 for the stated 133 questions | [Asked the authors](https://huggingface.co/papers/2611.03178) |
| [WikiTrace](2026/2611.14320-wikitrace/) (arXiv:2611.14320) | Released results include an ACE baseline missing from Table 1 that beats WikiTrace on two suites | [Explained by the authors](https://github.com/yukyeongleee/wikitrace/issues/2): ACE excluded for its much higher memory-build cost; fixture rows not meant for release |
| [RoboScript (World In-Context Learning)](2026/2611.12885-roboscript/) (arXiv:2611.12885) | Rehearsal results 46.1%, 8.4 and 13.3 cannot occur with 11 tasks and 10 episodes per setting | [Confirmed by the authors](https://github.com/ArcheOne-AI/RoboScript/issues/1); fix in next arXiv version |
| [P^2-MOPD](2026/2611.03953-p2-mopd/) (arXiv:2611.03953) | Text says 1.7B IM-MOPD never merged the medical teacher; Table 12 shows it did in 2 of 3 seeds | [Asked the authors](https://github.com/SinuoWang/P2-MOPD/issues/1) |
| [Sage-Taiyi](2026/2611.12762-sage-taiyi/) (arXiv:2611.12762) | Metamaterial reward 0.822 versus 0.852 from Eq. (4) and the reported transmissions | [Asked the authors](https://github.com/Alpha-Innovator/Sage-Taiyi/issues/1) |
| [EvoMemState](2026/2611.03743-evomemstate/) (arXiv:2611.03743) | One MemTrapBench Avg. in Table 1 (78.7) is not the mean of its four scenarios (81.75) | [Asked the authors](https://github.com/XMUDeepLIT/EvoMemState/issues/2) |
| [RoboColosseum](2026/2611.02497-robocolosseum/) (arXiv:2611.02497) | Text gives a 58–77% score range and a 13% success ceiling; Figure 5 shows 58–70% and cells up to 25% | [Asked the authors](https://github.com/RoboColosseum/robocolosseum-client/issues/1) |
| [NorthCUA](2026/2611.02102-northcua/) (arXiv:2611.02102) | Pro OSWorld 2.0 binary 27.3 after SFT is not k/108; all other NorthCUA binary scores are | [Asked the authors](https://huggingface.co/papers/2611.02102) |
| [ToolSpace](2026/2611.05036-toolspace/) (arXiv:2611.05036) | Headline 38.2-point drop comes from a DeepSeek -1017 row that is not in Figure 1(d) | [Asked the authors](https://github.com/dongguanting/ToolSpace/issues/4) |
| [uni-robot-agent](2026/2611.01560-uni-robot-agent/) (arXiv:2611.01560) | Section 5.1 gives Astra 98.6% depth retention from 42 episodes; Table 1 (252 episodes) gives 91.4% | [Answered by the authors](https://github.com/Open-RUA/uni-robot-agent/issues/39); 42-episode run explained |
| [Switch-SWE](2026/2611.02017-switch-swe/) (arXiv:2611.02017) | Section 4.3 workload ratios match a commented-out earlier Table 2, not the printed one | [Asked the authors](https://github.com/Miraclecsc/Switch-SWE/issues/2) |
| [Hybrid Computer Use](2026/2610.41432-hybrid-computer-use/) (arXiv:2610.41432) | Same OSWorld 1.0 runs cost $2.52/$5.65 in Table 2 and $0.504/$0.983 in Table 4 | [Asked the authors](https://github.com/microsoft/Hybrid-Computer-Use/issues/3) |
| [InfraRSI](2026/2611.11558-infrarsi/) (arXiv:2611.11558) | Text gives 1.55× first trial and 1.73× final on Qwen3.5-9B; Table 5 conditions give 1.22–1.24× and 1.70–1.82× | [Confirmed by the authors](https://github.com/TokenRhythm/InfraRSI/issues/1): 1.55× is a typo for 1.23×; fix in v2 |
| [Video-Coder](2026/2611.09894-video-coder/) (arXiv:2611.09894) | OmniWeaving gain 0.48 to 0.51 called 16.28 points; two identical Table 1 rows; 6k/2k vs 10k/4k data | [Asked the authors](https://github.com/CYWang735/Video-Coder/issues/4) |
| [SWAM](2026/2611.12870-swam/) (arXiv:2611.12870) | Table 4 54.76 is not k/1250; the other 115 ablation values are | [Asked the authors](https://github.com/shaaaaron/SWAM/issues/2) |
| [Drex](2026/2611.07854-drex/) (arXiv:2611.07854) | Three K≥6 flip rates in Table 7 (14.1, 17.8, 13.0%) are not k/173 | [Asked the authors](https://github.com/nace-ai/drex-decision-models/issues/18) |
| [CEPO](2026/2610.34722-cepo/) (arXiv:2610.34722) | Text says CEPO mitigates PE2's drop with more executors; Table S7 shows larger drops at |I| = 4 and 5 | [Asked the authors](https://github.com/mlvlab/CEPO/issues/2) |
| [StreamDuo](2026/2611.01120-streamduo/) (arXiv:2611.01120) | Headline 9.9% leakage baseline is a different run from the same-settings Proact-VL run (5.8%) | [Asked the authors](https://github.com/ZixianGao/StreamDuo-code/issues/1) |
| [CaPtain](2026/2610.40799-captain/) (arXiv:2610.40799) | Text says evaluation perturbations never appear in training; RL randomizes lighting, camera and materials | [Asked the authors](https://github.com/waltstephen/CaPtain/issues/1) |
| [WorkFactory](2026/2610.37161-workfactory/) (arXiv:2610.37161) | Abstract says larger models benefit more from more data; 30K→110K gains are 4B +168, 35B-A3B +82, 27B +38 | [Asked the authors](https://github.com/IQuestLab/WorkFactory/issues/2) |
| [VibeGame](2026/2610.33106-vibegame/) (arXiv:2610.33106) | Text says Luna gains no visual advantage in P2G; Table 1 Functional Visuals is higher in P2G for all three harnesses | [Asked the authors](https://github.com/tettethu/VibeGame/issues/7) |
| [Intrinsic Distribution Matching](2026/2610.39633-idm/) (arXiv:2610.39633) | APEX (Z-Image) numbers behind the headline comparison are not in the cited APEX paper | [Asked the authors](https://github.com/inclusionAI/IDM/issues/2) |
| [PhysLoop](2026/2611.16748-physloop/) (arXiv:2611.16748) | Table 1 Win is described as blinded multi-rater and as one author's unblinded comparisons; 6 of 9 Repair rates are not k/50 | [Asked the authors](https://github.com/DAGroup-PKU/PhysLoop/issues/1) |
| [WaveGen](2026/2611.12527-wavegen/) (arXiv:2611.12527) | 0.6B input dim 1158 is not divisible by 16 heads; nMOS intervals too wide for 2,000 ratings | [Asked the authors](https://github.com/sh-lee-prml/WaveGen/issues/2) |
| [SparseRead](2026/2608.22237-sparseread/) (arXiv:2608.22237) | NanoBot rows of Table 1 match none of the 30 Figure 6 settings | [Asked the authors](https://github.com/Liuzedooong/SparseReading/issues/1) |
| [LowRAM](2026/2611.07025-lowram/) (arXiv:2611.07025) | LowRAM-EQ rows of Table 3 come from a lower-compression setting of Table 10 than every other row | [Asked the authors](https://github.com/lowram-model/lowram/issues/2) |
| [Caper](2026/2610.40753-caper/) (arXiv:2610.40753) | SABER rates described as over 682 tasks fit 580; file-system destruction fits 47 of 84 | [Asked the authors](https://github.com/wudaoz/Caper/issues/2) |
| [ProTEUS](2026/2611.13348-proteus/) (arXiv:2611.13348) | Abstract claims >10-fold activity in both campaigns; ALDH reaches 6.85-fold (7.90 normalized) | [Closed by the authors](https://github.com/yikunpku/ProTEUS/issues/1) as completed, no comment |

## How each audit works

1. CheckPaper reviews the paper.
2. A person rechecks each finding against the original PDF. Only findings a reader can verify with a calculator or the paper itself go further.
3. We write a script, pinned to the exact PDF by its hash, that reproduces the numbers.
4. We ask the authors first, on the Hugging Face paper page, a GitHub issue or by email, and record their response here.

Every audit folder has the same five sections: Paper, Findings, Reproduce, Status, Author response. Responses are appended, never rewritten.

## Run an audit

```bash
git clone https://github.com/checkpaper/audits
cd audits
pip install -r requirements.txt
python 2026/2609.17488-limix-2/verify.py
```

## Check your own paper

Run [CheckPaper](https://checkpaper.app) on your manuscript before you submit.

## Contact

Corrections and author responses: open an issue or write to victor@checkpaper.app.

Code is MIT licensed. Text is CC BY 4.0.

# CheckPaper Audits

Reproducible consistency checks of influential research papers. Each audit lists numbers in a paper that disagree with its own tables, figures or cited sources, and ships a script that recomputes them from the original PDF.

We check papers people are reading right now: Hugging Face Daily Papers, widely covered studies and papers under public discussion. Findings come from [CheckPaper](https://checkpaper.app), an AI paper review tool, and a person verifies every one before it appears here.

## Audits

| Paper | Finding | Status |
| --- | --- | --- |
| [DeepSeek-V4.1-Flash](2026/2609.19969-deepseek-v4.1-flash/) (arXiv:2609.19969) | World knowledge claim versus Table 1; 5% to 10% claim versus Figure 6 | Contacting the authors |
| [LimiX-2](2026/2609.17488-limix-2/) (arXiv:2609.17488) | Table 7 PATHFINDER results imply 137 to 189 edges; the cited network has 195 | [Asked the authors](https://github.com/limix-ldm-ai/LimiX/issues/66) |
| [MDMA-assisted therapy for severe PTSD](2026/s41591-021-01336-3-mdma-ptsd-phase-3/) (Nature Medicine 2021) | Within-group CIs centred on the negative of their estimates; SDS CI includes zero while P = 0.0116 | Contacting the authors |
| [Sugar-rich foods and antibiotic microbiome disruption](2026/s41586-026-11077-3-sugar-antibiotics-microbiome/) (Nature 2026) | Fig. 4 title names E. faecalis, the data are E. faecium; Fig. 3a legend HR 0.72 versus 0.59 in Supplementary Table 4 | Not yet sent |

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

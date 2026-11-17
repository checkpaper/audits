# ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping (arXiv:2611.11306): consistency checks

Two human-baseline rates cannot be reached with the stated 450 decisions per condition, and one design effect does not follow from its ICC.

## Paper

- Title: ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping
- arXiv: [2611.11306v1](https://arxiv.org/abs/2611.11306v1) (the version checked, sha256 `6db2ca27…cb26b`)
- Hugging Face: [papers/2611.11306](https://huggingface.co/papers/2611.11306)
- Code: [imperialite/scrapebench](https://github.com/imperialite/scrapebench)
- CheckPaper report: [checkpaper.app/r/qr8eww886n](https://checkpaper.app/r/qr8eww886n)

## Findings

1. **Human rates and n = 450.** Sec. 6 (p. 9) gives 30 participants per condition, each deciding on 15 websites, so each condition has 450 decisions. Table 16 (p. 32) gives NEP over-refusal at P4 as 42.8%, and Table 18 (p. 32) gives NEP robots.txt opened at P4 as 39.4%. Neither is k/450: the nearest values are 192/450 = 42.67% and 193/450 = 42.89%, and 177/450 = 39.33% and 178/450 = 39.56%. The other rates fit, and the EP compliance row (220, 258 and 293 of 450) reproduces the reported χ² = 24.19 exactly.
2. **Design effect.** App. E.3 (p. 31) reports ICC = 0.345 and a design effect of 5.69 with 15 decisions per participant. 1 + (15 − 1) × 0.345 = 5.83. A value of 5.69 implies ICC 0.335. The second pair (ICC 0.238, design effect 4.34) agrees within rounding.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.11306v1, checks its hash, quotes Sec. 6, App. E.3 and Tables 16 and 18, and recomputes the counts, χ² and design effects.

## Status

[Asked the authors](https://github.com/imperialite/scrapebench/issues/2) on 2026-11-18.

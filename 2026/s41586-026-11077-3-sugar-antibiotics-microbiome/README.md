# Sugar-rich foods and antibiotic-induced microbiome disruption (Nature 2026): consistency checks

Two statements in the paper that disagree with its own data: the species named in the Fig. 4 title, and one hazard ratio in the Fig. 3a legend. The main result reproduces from the released data, and neither point changes it.

## Paper

- Title: Sugar-rich foods exacerbate antibiotic-induced microbiome disruption
- Authors: Dai, Ballweg, Jogia et al.; corresponding authors Peled, van den Brink, Schluter
- Journal: Nature 658, 757–764 (2026), [doi:10.1038/s41586-026-11077-3](https://doi.org/10.1038/s41586-026-11077-3)
- Files checked: the PDF and Supplementary Information from nature.com, and two tables from the authors' [data deposit](https://zenodo.org/records/23444717), all pinned by sha256 in `verify.py`
- CheckPaper report: [checkpaper.app/r/tdtzcshkr3](https://checkpaper.app/r/tdtzcshkr3)

## Findings

1. **Fig. 4 title names E. faecalis.** The title (PDF p. 6) reads "Sugar and antibiotics synergize to exacerbate E. faecalis expansion in the gut microbiome of humans and in mice". The human panel it heads, Fig. 4b, models E. faecium (ASV_1), and the authors' BLAST table assigns ASV_1 to Enterococcus faecium at 100% identity over 332 bp.
2. **Fig. 3a legend HR.** The legend (PDF p. 5) gives the sugar-group hazard ratio as 0.72 (95% CI 0.18 to 2.85, P = 0.6). Supplementary Table 4, which reports the same model, gives 0.59 (0.15 to 2.32, P = 0.4). Refitting the model in the authors' code (`fit_sugar_density_binarized`) on the released clinical table gives 0.59 (0.15 to 2.32), P = 0.45, and reproduces the other numbers in the legend and the table.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads the four files, checks their hashes, finds each quoted phrase on its page, looks up ASV_1 in the BLAST table, and refits the Cox model.

## Status

Contacting the authors, started 2026-11-10.

## Author response

None yet.

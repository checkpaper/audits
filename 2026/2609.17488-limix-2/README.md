# LimiX-2 (arXiv:2609.17488): consistency checks

The PATHFINDER results in Table 7 of LimiX-2 imply a ground-truth graph with fewer edges than the cited network.

## Paper

- Title: LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence
- arXiv: [2609.17488v1](https://arxiv.org/abs/2609.17488v1) (the version checked, sha256 `81cac824…232f`)
- Hugging Face: [papers/2609.17488](https://huggingface.co/papers/2609.17488)
- Code: [limix-ldm-ai/LimiX](https://github.com/limix-ldm-ai/LimiX)
- CheckPaper report: [checkpaper.app/r/n7q7y53n3u](https://checkpaper.app/r/n7q7y53n3u)

## Findings

1. **PATHFINDER edge count.** Table 7 (p. 22) reports causal skeleton recovery as F1 and SHD. For an undirected skeleton SHD = FP + FN and F1 = 2TP / (2TP + SHD), so each row fixes TP and bounds the true edge count between TP and TP + SHD. Every PATHFINDER row yields an integer TP, and together the rows place the edge count between 137 and 189. LimiX-2 gives the lower bound (TP = 137); TabCausal (F1 0, SHD 189) and DAG-GNN (F1 0.3846, SHD 144) give the upper bound. The PATHFINDER network in the [bnlearn repository](https://www.bnlearn.com/bnrepository/), cited for this dataset, has 109 nodes and 195 arcs.
2. **Control: PIGS.** The same calculation on the PIGS column gives 591 to 592 edges. bnlearn lists 592 arcs for PIGS, so the method recovers a known graph.

A reduced PATHFINDER graph, for example after dropping some variables, would explain the gap. The paper does not mention one.

## Reproduce

```bash
pip install pymupdf
python verify.py
```

The script downloads arXiv 2609.17488v1, checks its hash, reads all 14 rows of Table 7 from p. 22, and prints the TP and edge range for every row.

## Status

Resolved. The authors explained on 2026-11-13: following the CausalChamber pipeline, the constant variable F72 and its 7 edges were removed, leaving 188 edges, inside the 137 to 189 range derived here. Asked in [the LimiX repository](https://github.com/limix-ldm-ai/LimiX/issues/66).

## Author response

2026-11-13, limix-ldm (repository collaborator), in [the issue](https://github.com/limix-ldm-ai/LimiX/issues/66):

> Thanks for your questions. We follow their evaluation pipeline in CausalChamber (Gamella et al., 2025) and remove variables that are constant in the dataset, along with their incident edges. This choice is reasonable because relationships involving a constant variable cannot be inferred from the data. Specifically, the F72 variable in PATHFINDER keeps 'Present' in the data split we used. Therefore, we remove this variable and all edges incident to it. The number of edges incident to F72 is 7, so the number of remaining edges is 188. This is consistent with the derived edge-count interval (137–189).

Follow-up the same day: the authors agreed that noting the removal of constant variables would make the evaluation easier to reproduce, and said they will consider adding it to the paper or the evaluation code.

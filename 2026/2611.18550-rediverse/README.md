# Restoring Diversity in Distilled Image and Video Generators by Probing Activations (arXiv:2611.18550): consistency checks

Sec. 5.2 says ReDiverse beats Noise Optimization on all diversity metrics except SD3 Vendi, but Table 4a has Noise Optimization ahead on all five SDXL metrics. In Table 5a, the TPIPS_avg of "Regress at all blocks" equals that row's overall TPIPS from Table 8.

## Paper

- Title: Restoring Diversity in Distilled Image and Video Generators by Probing Activations
- arXiv: [2611.18550v1](https://arxiv.org/abs/2611.18550v1) (the version checked, sha256 `c5ea0706…1fce`)
- Hugging Face: [papers/2611.18550](https://huggingface.co/papers/2611.18550)
- Code: [H-furkan/rediverse](https://github.com/H-furkan/rediverse)
- CheckPaper report: [checkpaper.app/r/82em7qft78](https://checkpaper.app/r/82em7qft78)

## Findings

1. **ReDiverse versus Noise Optimization.** Sec. 5.2 (p. 8) says ReDiverse "surpasses Noise Optimization on all diversity metrics except Vendi for SD3". Table 4a (p. 7) supports this for SD3 only. On SDXL, Noise Optimization is ahead on all five diversity metrics: DINO 67.0 vs 65.0, DreamSim 37.9 vs 33.3, LPIPS 71.2 vs 67.9, TPIPS 25.1 vs 23.0, Vendi 7.83 vs 7.03.
2. **Table 5a, "Regress at all blocks".** Table 5a (p. 10) reports TPIPS_avg, which runs 6 to 9 points below the overall TPIPS of Table 8 (p. 25) for every other row (teacher 21.7 vs 30.2, student 13.9 vs 20.1, default 15.4 vs 22.4, block 16 17.0 vs 24.2). For "Regress at all blocks" the two are equal (26.6), and it is the only Table 5a row without a delta. As printed, it would also exceed the teacher's 21.7. The cell likely holds the overall value.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.18550v1, checks its hash, quotes Sec. 5.2 and Tables 4a, 5a and 8, and compares the values.

## Status

Issues are disabled on the code repository, so we [asked the authors on the Hugging Face paper page](https://huggingface.co/papers/2611.18550) on 2026-11-18.

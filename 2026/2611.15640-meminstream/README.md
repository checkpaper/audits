# MemInStream: Memorizing or Merely Recognizing? Rethinking Streaming Video Memory (arXiv:2611.15640): consistency checks

Sec. 5.3 says StreamForest has the best online average in all four memory categories; in Table 2 JoyAI-VL-Interaction leads State Tracking & Updating, 43.9 to 37.1.

## Paper

- Title: MemInStream: Memorizing or Merely Recognizing? Rethinking Streaming Video Memory
- arXiv: [2611.15640v1](https://arxiv.org/abs/2611.15640v1) (the version checked, sha256 `dc131e3c…ab0b`)
- Hugging Face: [papers/2611.15640](https://huggingface.co/papers/2611.15640)
- Code: [HKUST-LongGroup/MemInStream](https://github.com/HKUST-LongGroup/MemInStream)
- CheckPaper report: [checkpaper.app/r/72efsthrg8](https://checkpaper.app/r/72efsthrg8)

## Findings

1. **Best online model per category.** Sec. 5.3 (p. 8) says "Among online models, StreamForest achieves the highest average accuracy across all four memory categories, with particularly strong performance on State Tracking & Updating (37.06%)". In Table 2 (p. 9) StreamForest has the best online average on Episodic Retrieval (42.0), Multi-Evidence Integration (37.3) and Contextual Memory (35.4). On State Tracking & Updating, JoyAI-VL-Interaction, listed among the training-based online models, has 43.9; StreamForest has 37.1. Fig. 5 (p. 11) shows the same 43.9 for JoyAI with memory.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.15640v1, checks its hash, quotes Sec. 5.3, parses the online rows of Table 2, and prints the best model per category.

## Status

Not yet asked.

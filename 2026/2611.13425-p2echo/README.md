# Prompt2Echo (P2Echo): Text-Prompted Multi-View Echocardiography Segmentation with One Model (arXiv:2611.13425): consistency checks

The speed-up range over promptable methods is given as 4.28–159.36× (and 4–160× in the Discussion), but by Table VII the largest ratio is Grounding DINO-US-SAM at 168.09×; 159.36× is MedCLIP-SAMv2.

## Paper

- Title: Prompt2Echo (P2Echo): Text-Prompted Multi-View Echocardiography Segmentation with One Model
- arXiv: [2611.13425v1](https://arxiv.org/abs/2611.13425v1) (the version checked, sha256 `2987dafe…e647`)
- Hugging Face: [papers/2611.13425](https://huggingface.co/papers/2611.13425)
- Code: [moeinheidari7829/P2Echo](https://github.com/moeinheidari7829/P2Echo)
- CheckPaper report: [checkpaper.app/r/tpfj2c98mj](https://checkpaper.app/r/tpfj2c98mj)

## Findings

1. **Speed-up range (p. 7, p. 8 vs Table VII, p. 9).** The text says P2Echo is "4.28–159.36× faster than the evaluated promptable methods" and the Discussion says "4–160×". Table VII gives P2Echo 0.01546 s/image, MedCLIP-SAMv2 2.46376 s (159.36×) and Grounding DINO-US-SAM 2.59870 s (168.09×). The upper end should be 168.09×. The CENet ratio (1.51×) and the lower end (SAMUS, 4.28×) match.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.13425v1, checks its hash, quotes the passages and tables above, and recomputes the numbers.

## Status

Not yet asked.

# GameDojo: Benchmarking Real-Time Interactive Agents in Video Games (arXiv:2611.30771): consistency check

The abstract says that in real-time interaction "all models win 0 score", but Table 4 reports non-zero real-time win rates for three models, and GameDojo-4B above Random in real-time PG.

## Paper

- Title: GameDojo: Benchmarking Real-Time Interactive Agents in Video Games
- arXiv: [2611.30771v1](https://arxiv.org/abs/2611.30771v1) (the version checked, sha256 `bab58c2f…2687`)
- Hugging Face: [papers/2611.30771](https://huggingface.co/papers/2611.30771)
- Code: [THUSI-Lab/GameDojo](https://github.com/THUSI-Lab/GameDojo)
- CheckPaper report: [checkpaper.app/r/q7vfrr9429](https://checkpaper.app/r/q7vfrr9429)

## Findings

1. **Real-time results.** The abstract (p. 1) says "all models win 0 score" in real time, and Sec. 4.2 (p. 9) says "all evaluated models score below Random in PG and achieve zero WR". This holds at medium difficulty (Table 3). In Table 4 (p. 8), real-time easy WR is 2.5 for GPT-6.1-Sol, 6.4 for GameDojo-4B and 0.8 for Gamer-35B-A3B, and GameDojo-4B's real-time PG is 26.3 on easy and 12.3 on average, against 19.2 and 9.4 for Random. Sec. 4.3 itself reports the 26.26% figure.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.30771v1, checks its hash, quotes both sentences and the Table 4 rows, and compares them with Random.

## Status

[Asked the authors](https://github.com/THUSI-Lab/GameDojo/issues/2) on 2026-11-28.

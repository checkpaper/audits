# AI Reviews Are Biased Towards the Appendix (arXiv:2611.17811): consistency checks

The released code attributes human and LLM review weaknesses with different prompts, although the paper says the same step is reused.

## Paper

- Title: AI Reviews Are Biased Towards the Appendix
- arXiv: [2611.17811v1](https://arxiv.org/abs/2611.17811v1) (the version checked, sha256 `81ddeea6…6518`)
- Hugging Face: [papers/2611.17811](https://huggingface.co/papers/2611.17811)
- Code: [cincynlp/review_appendix](https://github.com/cincynlp/review_appendix) (commit `825e396` checked)
- CheckPaper report: [checkpaper.app/r/v4jkxx92ur](https://checkpaper.app/r/v4jkxx92ur)

## Findings

1. **Attribution prompts differ.** Section 5 (p. 7) says human reviews are attributed by reusing the second step of the LLM pipeline. In the code, `scripts/human_review/citation_iclr_human_review.py` adds a rule the LLM prompts (`scripts/llm_review/review_api.py`, `review_codex.py`, `review_claude.py`) do not have: "Assign a weakness to the Appendix ONLY if it is very obvious that it is directed at appendix content [...] Generic comments must NOT be assigned to the Appendix", plus "Base every answer only on what the review explicitly says". The LLM prompt instead asks to "Base your answer on where the content actually appears in the paper, not on where the review says it appears". The headline contrast (8.4% for humans versus 62% for LLMs, Table 1) is therefore measured under a stricter appendix rule for humans.
2. **Appendix threshold for the human sample.** Section 5 says the human sample uses papers with an appendix of at least 10 pages. The human attribution script reads PDFs from `pdf_app`, which `extract_long_appendix_iclr.py` fills only with papers of `MIN_PAGES = 15` or more.

## Reproduce

```bash
pip install -r ../../requirements.txt
python verify.py
```

The script downloads arXiv 2611.17811v1 and the three scripts at the pinned commit, checks their hashes, and prints the differing rules and the page threshold.

## Status

Contacting the authors, started 2026-11-17.

## Author response

None yet.

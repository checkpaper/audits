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

Explained by the authors on 2026-11-17 in [the review_appendix repository](https://github.com/cincynlp/review_appendix/issues/2). The prompts differ on purpose: human reviews rarely name a section, and without the extra rule the LLM guessed the appendix for generic comments. The authors checked attributions for both review types by hand. The paper does not yet say that the prompts differ, and the 10 versus 15 page point is open.

## Author response

From SaptGhosh, 2026-11-17 00:38 UTC:

> Thank you for this question. The prompts differ because AI-generated and human-written reviews are structured very differently.
>
> AI-generated reviews always say which section a strength or weakness refers to. They do this either directly ("Section 6.2 mentions xxx...") or in parentheses after the comment ("there might be a confound in the analysis (Section 6.2)"). This pattern is consistent across AI reviews, which makes attribution easy. The instruction "Base your answer on where the content actually appears in the paper, not on where the review says it appears" handles a different case that is common in AI reviews: a weakness that cites several sections to support its claim. For example, the main issue may be in Section 3, but the weakness also points to Sections 5 and 6 and Appendix B as support. In such cases, we want the weakness attributed to where the issue actually lies, the main body (Section 3), and this instruction is designed for that.
>
> Human-written reviews, on the other hand, rarely mention which section a weakness refers to. In our initial runs, this led the LLM to guess. For example, a generic comment like "the mathematical notations are hard to follow" was attributed to the appendix, since the appendix contains most of the proofs. But a careful reading of the review made it clear the reviewer was not talking about the appendix. We added the instruction to stop the LLM from assigning sections based on such assumptions.
>
> Most importantly, during our test runs we manually went through the outputs for both human and AI reviews and checked the attributions ourselves. We refined the prompts until they gave reliable attributions for each type of review. The instructions differ slightly only because the reviews themselves differ.

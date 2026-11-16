"""Reproduce the check on AI Reviews Are Biased Towards the Appendix, arXiv:2611.17811v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, quote  # noqa: E402

doc = fetch("2611.17811", "v1", "81ddeea6bc6aca92baf81cac95c3585f3c529d6f37171cfccfdbdc99ebdd6518")
RAW = "https://raw.githubusercontent.com/cincynlp/review_appendix/825e3962348e45f9a46a0c844a39bd5e9887d415/scripts/"
human = download(RAW + "human_review/citation_iclr_human_review.py", "2611.17811-human.py",
                 "1b07e9ca3aa8f34c110ca79b9cb70fc7202cde0b04d1a5bc14e229974af5316b").read_text()
llm = download(RAW + "llm_review/review_api.py", "2611.17811-llm-api.py",
               "817b13269c6ed2ebf15a4a744f1ed5ef58eafe4bbb47e8b69fed69dd314568c3").read_text()
extract = download(RAW + "download_papers/extract_long_appendix_iclr.py", "2611.17811-extract.py",
                   "69790c4613f2380fdb857b3b8d69e5246cb8135f1ad37b2730b59388b58f7ff6").read_text()

print("1. Section attribution: the paper says the human reviews reuse the LLM step")
quote(doc, 7, "we reuse the second step of our pipeline (right panel in Figure 2) to attribute each weakness")
quote(doc, 1, "humans draw only 8.4% of their weaknesses from the appendix")


def rules(src):
    block = src[src.index("Instructions:"):src.index("Return ONLY")]
    return [" ".join(r.split()) for r in re.split(r"\n\d+\. ", "\n" + block.split("\n", 1)[1]) if r.strip()]


print("\n  Human-review attribution prompt (citation_iclr_human_review.py):")
for r in rules(human):
    if re.search(r"Appendix ONLY|explicitly says|reviewer's own enumeration", r):
        print("   -", r)
print("  LLM-review attribution prompt (review_api.py), rules about where content appears:")
for r in rules(llm):
    if re.search(r"actually appears|would belong|Identify every", r):
        print("   -", r)
print("  'Appendix ONLY' rule in the LLM prompt:", "Appendix ONLY" in llm)

print("\n2. Appendix length threshold for the human sample")
quote(doc, 7, "the paper must have an appendix of at least 10 pages")
print("  citation_iclr_human_review.py reads", re.search(r'PDF_DIR = BASE_DIR / "(\w+)"', human).group(1),
      "; extract_long_appendix_iclr.py copies into",
      re.search(r'DESTINATION = Path\("(\w+)"\)', extract).group(1), "only papers with",
      re.search(r"MIN_PAGES = (\d+)", extract).group(0))

"""Reproduce the check on Intrinsic Distribution Matching (IDM), arXiv:2610.39633v1.

Run: python verify.py
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.39633", "v1", "0d7e5a4193b59e04d4bffaf84fe6dc23715442bce464b1851d5c6379723fea27")
apex = fetch("2604.12322", "v1", "db2238ca266febd0ced8162de0c1028703e9d7aeffcfd3c0a691c4a03eb3dea1")

print("Where does the APEX (Z-Image) row of Table 5 come from?")
quote(doc, 9, "over APEX by 3.87 and 1.44 points, respectively")
quote(doc, 12, "APEX (Liu et al., 2026a) is the published Z-Image reference from its comparison with TwinFlow")
quote(doc, 12, "A ⃝ APEX 2 52.60 77.23 88.64 90.38 88.76")
quote(doc, 19, "Self-adversarial one step generation via condition shifting. arXiv preprint arXiv:2604.12322, 2026a.")
text = " ".join(re.sub(r"\s+", " ", page.get_text()) for page in apex)
for token in ("Z-Image", "OneIG", "LongText", "52.60", "77.23", "88.64", "90.38", "88.76"):
    print(f"  arXiv:2604.12322v1 mentions {token!r}: {text.count(token)} times")

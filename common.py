"""Shared helpers: fetch a pinned arXiv PDF and look up text on a page."""
import hashlib
import pathlib
import re
import sys
import urllib.request

import fitz  # PyMuPDF

CACHE = pathlib.Path(__file__).resolve().parent / ".cache"


def fetch(arxiv_id, version, sha256):
    """Download arxiv_id+version once and check it is the exact file we audited."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{arxiv_id}{version}.pdf"
    if not path.exists():
        url = f"https://arxiv.org/pdf/{arxiv_id}{version}"
        print(f"Downloading {url}")
        req = urllib.request.Request(url, headers={"User-Agent": "checkpaper-audits"})
        path.write_bytes(urllib.request.urlopen(req, timeout=120).read())
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != sha256:
        sys.exit(f"{path.name}: sha256 {digest} differs from the audited file {sha256}")
    return fitz.open(path)


def page_text(doc, page):
    """Text of a 1-indexed page with line breaks and hyphenation joined."""
    text = doc[page - 1].get_text()
    text = re.sub(r"-\n", "", text)
    return re.sub(r"\s+", " ", text)


def quote(doc, page, phrase):
    """Print the phrase if it appears on the page, stop otherwise."""
    if phrase not in page_text(doc, page):
        sys.exit(f"p. {page}: phrase not found: {phrase}")
    print(f'p. {page}: "{phrase}"')

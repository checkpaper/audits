"""Reproduce the check on PACT (Recurrent Domain Incremental Adaptation of Time-Series Foundation Models), arXiv:2611.24075v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.24075", "v1", "e7a7dd18a5c3d7baf0c69fa62c9632f34bd8a9bc84f992016fd9674b202435e1")

print("Table 4 (App. C.1, p. 16): dataset, stream SD, seeds, PACT, comparator")
rows = {
    "FD": "FD 0.0106 3 0.9575 ± 0.0022 0.9041 ± 0.0061",
    "WISDM": "WISDM 0.0197 2 0.8775 ± 0.0173 0.8621 ± 0.0008",
    "HHAR": "HHAR 0.0214 3 0.8367 ± 0.0022 0.8591 ± 0.0044",
    "UCI-HAR": "UCI-HAR 0.0144 2 0.7910 ± 0.0046 0.8145 ± 0.0024",
    "Sleep-EDF": "Sleep-EDF 0.0316 3 0.6129 ± 0.0023 0.6482 ± 0.0023",
}
for s in rows.values():
    quote(doc, 16, s)

print("\n1. WISDM ordering (p. 16)")
quote(doc, 16, "The WISDM ordering changed when averaged over two seeds, with replay ahead by 1.54 points.")
v = rows["WISDM"].split()
pact, rep = float(v[3]), float(v[6])
print(f"  PACT {pact} - replay {rep} = {(pact - rep) * 100:+.2f} points: PACT is ahead, not replay.")

print("\n2. Number of seeds (Sec. 4.1, p. 6)")
quote(doc, 6, "Table 1 reports the mean over three training seeds and four fixed streams per dataset.")
for k, s in rows.items():
    print(f"  {k:9s} seeds in Table 4: {s.split()[2]}")
print("  WISDM and UCI-HAR have two seeds, not three.")

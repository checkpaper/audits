"""Reproduce the check on P^2-MOPD, arXiv:2611.03953v2.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.03953", "v2", "1532a8e9399e3e98480ddd8cbd84f4fc4af600abe4ee1a100e64cc314c5eb483")

print("Section 4.3 (p. 8) versus Table 12 (p. 16): did 1.7B IM-MOPD merge the medical teacher?")
quote(doc, 8, "The other three moved at most 0.03: MOPD (TA init) at both scales, and 1.7B IM-MOPD, "
              "which did not merge the medical teacher.")
quote(doc, 16, "At steps 25, 50 and 75 the recovery-gated rule merges the task vectors of the listed domains into the student")
rows = {
    42: "1.7B 42 Fin, IF 42.3 46.4 Fin 49.2 47.7 – 50.4 – 77.4",
    43: "43 IF 38.7 44.5 Med, Fin, IF 49.8 32.7 Fin 56.3 51.7 67.1",
    44: "44 IF 38.1 44.9 Med, IF 55.7 47.4 Fin 54.1 57.3 59.0",
}
for seed, row in rows.items():
    quote(doc, 16, row)
# Each row: seed, then for steps 25, 50 and 75 the merged domains, Pre and Post recovery, then Final.
print("  1.7B IM-MOPD domains merged, by seed:")
print("    seed 42: step 25 Fin, IF; step 50 Fin; step 75 none")
print("    seed 43: step 25 IF; step 50 Med, Fin, IF; step 75 Fin")
print("    seed 44: step 25 IF; step 50 Med, IF; step 75 Fin")
print("  Seeds 43 and 44 merge Med at step 50, so 2 of the 3 runs did merge the medical teacher.")

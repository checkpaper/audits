"""Reproduce the check on CoworkOS, arXiv:2611.03178v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.03178", "v1", "0db3eb94695af5b2bd6c6da600691091202d5e0df79d850ca734f2a85493cf15")
N = 133


def fits(value, n, dp):
    """True if value equals 100*k/n rounded to dp decimals for some whole k."""
    return any(abs(100 * k / n - value) <= 0.5 * 10 ** -dp + 1e-9 for k in range(n + 1))


def report(label, value, dp):
    k = [k for k in range(N + 1) if abs(100 * k / N - value) <= 0.5 * 10 ** -dp + 1e-9]
    near = sorted(range(N + 1), key=lambda k: abs(100 * k / N - value))[:2]
    note = f"= {k[0]}/133" if k else "not k/133; nearest " + ", ".join(f"{j}/133 = {100 * j / N:.{dp}f}" for j in sorted(near))
    print(f"  {label:10} {value:6.{dp}f}  {note}")


quote(doc, 26, "We use the 133-question OfficeQA Pro subset")

print("\nTable 1 (p. 15), OfficeQA Pro, printed with one meaningful decimal")
quote(doc, 15, "OfficeQA Pro 66.20 66.30 62.30 65.90")
for label, v in zip(["OpenHands", "Codex", "DSH", "CoworkOS"], [66.2, 66.3, 62.3, 65.9]):
    report(label, v, 1)

print("\nTable 2 (p. 33), OfficeQA across post-training rounds")
quote(doc, 33, "OfficeQA 55.64 53.38 52.63 56.14 59.40 62.11 +6.47")
for label, v in zip(["R0", "R1", "R2", "R3", "R4", "R5"], [55.64, 53.38, 52.63, 56.14, 59.40, 62.11]):
    report(label, v, 2)

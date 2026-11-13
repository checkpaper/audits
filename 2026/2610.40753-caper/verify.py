"""Reproduce the checks on Caper ("Shall We Approve?"), arXiv:2610.40753v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2610.40753", "v1", "0a96187ba780be4d0ef67e3085f1e22c57c517cf09226d95e6777a8f2d9e2bf3")


def fits(v, n):
    """v (one decimal, in %) can be k/n for an integer k."""
    return abs(round(v * n / 100) / n * 100 - v) <= 0.05 + 1e-9


quote(doc, 7, "We use its 682 shell-only tasks")
quote(doc, 7, "File-system destruction 30 32 22 84")

print("\n1. Table 10 (p. 23): harmful rate by category, nine systems")
CATS = {
    "Code tampering": ("16.7 16.7 13.2 21.1 9.6 21.1 17.5 8.8 2.6", 126),
    "Information leak": ("27.2 18.5 26.1 20.7 25.0 23.9 18.5 2.2 4.3", 104),
    "File-system destruction": ("14.9 8.5 23.4 14.9 10.6 27.7 14.9 10.6 10.6", 84),
    "Unauthorized access": ("21.6 16.2 21.6 16.2 14.9 24.3 9.5 4.1 8.1", 82),
    "Data destruction": ("27.3 18.2 20.8 24.7 22.1 26.0 13.0 18.2 14.3", 82),
    "Privilege escalation": ("14.3 8.6 12.9 12.9 14.3 8.6 8.6 11.4 4.3", 74),
    "Outbound network": ("9.6 19.2 15.4 11.5 11.5 19.2 19.2 11.5 5.8", 66),
    "Persistence": ("20.4 9.3 18.5 22.2 18.5 18.5 16.7 18.5 7.4", 64),
}
total = 0
for cat, (row, n_tasks) in CATS.items():
    quote(doc, 23, f"{cat} {row}")
    vals = [float(x) for x in row.split()]
    ns = [n for n in range(1, n_tasks + 1) if all(fits(v, n) for v in vals)]
    print(f"  {cat:24s} Table 1 has {n_tasks:3d} tasks; denominators that fit all nine rates: {ns}")
    total += ns[0]
print(f"  Sum of the fitted denominators: {total} (paper: 682)")

print("\n2. Table 3 (p. 9): SABER columns")
T3 = {
    "GLM-5.3-Flash": "19.7 57.4 9.1 66.6", "CARE": "15.0 47.9 13.6 61.6", "TS-Guard": "18.8 44.7 16.9 61.6",
    "gpt-oss-safeguard-20b": "18.6 53.1 12.1 65.2", "Qwen3Guard-Gen-8B": "16.0 52.1 14.3 66.4",
    "YoloFS": "21.2 54.1 14.1 68.3", "Claude Code Auto Mode": "14.8 44.0 18.3 62.2",
    "Caper (Claude Code hook)": "10.0 45.5 20.7 66.2", "Caper": "6.7 48.6 19.1 67.8",
}
for name, row in T3.items():
    quote(doc, 9, f"{name} {row}")
    vals = [float(x) for x in row.split()]
    print(f"    k/682: {['ok' if fits(v, 682) else 'no' for v in vals]}  k/580: {['ok' if fits(v, 580) else 'no' for v in vals]}")

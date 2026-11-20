"""Reproduce the check on TorchCurves, arXiv:2611.14516v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.14516", "v1", "c51b7c23a3d8c0ae12dd3ed6d9e1e9c5308455e7f311ab8697b341be05f01167")


def basis(t, k, x):
    """Cox-de Boor: values of all B-spline basis functions of degree k at x."""
    n = len(t) - 1
    b = [1.0 if t[i] <= x < t[i + 1] else 0.0 for i in range(n)]
    for d in range(1, k + 1):
        nb = []
        for i in range(n - d):
            left = (x - t[i]) / (t[i + d] - t[i]) * b[i] if t[i + d] > t[i] else 0.0
            right = (t[i + d + 1] - x) / (t[i + d + 1] - t[i + 1]) * b[i + 1] if t[i + d + 1] > t[i + 1] else 0.0
            nb.append(left + right)
        b = nb
    return b


print("1. Number of coefficients (Sec. 3.1, p. 4)")
quote(doc, 4, "P = |knots|−degree+1")
print("2. Non-zero basis functions (Sec. 4, p. 6)")
quote(doc, 6, "only degree+2 basis functions are non-zero")
for k in range(1, 6):
    t = [-1.0] * (k + 1) + [-1 + 2 * j / 10 for j in range(1, 10)] + [1.0] * (k + 1)
    xs = [-0.999 + 1.998 * j / 400 for j in range(401)]
    vals = [basis(t, k, x) for x in xs]
    P = len(vals[0])
    nz = max(sum(abs(v) > 1e-12 for v in row) for row in vals)
    print(f"  degree {k}: |knots| = {len(t)}, P = {P} = |knots| - degree - 1 "
          f"(paper formula gives {len(t) - k + 1}); max non-zero basis = {nz} = degree + 1")

print("3. KAN architecture (Sec. 5, p. 7 vs Figure 4 caption, p. 10)")
quote(doc, 7, "the architecture [16, W, W, 1], meaning, 16 input features")
quote(doc, 10, "Training-step time ratios for idiomatic [32, W, W, 1] cubic KANs")

"""Reproduce the check on Sage-Taiyi, arXiv:2611.12762v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.12762", "v1", "ee522780f32e47acf6c6a59d77ca48d764ea78e6ac129432ea2dd8f2cd7ae524")

print("Metamaterial case (Section 3.3.3, p. 25 and Table 6, p. 26): reward of the best design")
quote(doc, 25, "The objective maximizes high passband transmission while penalizing stopband transmission")
quote(doc, 25, "𝑅meta = 𝑇pass −1.5𝑇stop, (4)")
quote(doc, 25, "reported average stopband and passband transmissions of 6.2% and 94.5%, respectively")
quote(doc, 25, "a final best reward of 0.822 after ten optimization rounds")
quote(doc, 26, "Optimization reward 𝑅meta – Dimensionless 0.822")
t_pass, t_stop = 0.945, 0.062
print(f"  Eq. (4) at the reported transmissions: {t_pass} - 1.5 x {t_stop} = {t_pass - 1.5 * t_stop:.3f}, reported 0.822")
# The reported transmissions are rounded to 0.1%; the reward still cannot reach 0.822.
low = (t_pass - 0.0005) - 1.5 * (t_stop + 0.0005)
print(f"  Lowest value allowed by rounding of 94.5% and 6.2%: {low:.4f}")

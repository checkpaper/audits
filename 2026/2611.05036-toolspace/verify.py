"""Reproduce the check on ToolSpace, arXiv:2611.05036v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.05036", "v1", "697822d55a570dba21a4f8f411bdbb914672bf1c8385851e311d675709e420bb")

print("The 38.2-point drop on AutomationBench Pro")
quote(doc, 3, "On AutomationBench Pro, seven frontier models drop by up to 38.2 points relative to the standard version (Figure 1).")
quote(doc, 13, "DeepSeek-V4.1-Flash-1017 60.5 22.3 −38.2 51.3 36.9 −14.4 DeepSeek-V4.1-Flash 54.8 20.0 −34.8")
quote(doc, 1, "(d) Performance on Pro Benchmarks")
quote(doc, 1, "Automation Pro 18.0 22.7 24.7 24.0 20.0 26.3")
quote(doc, 1, "τ³-Bench Banking Pro 12.2 20.4 29.6 29.6 35.7 35.7")
table2 = {"Claude Opus 5.5": (59.2, 26.3), "GPT 6.1 Sol": (50.8, 24.7), "DeepSeek-V4.1-Flash-1017": (60.5, 22.3),
          "DeepSeek-V4.1-Flash": (54.8, 20.0), "GLM 5.3": (52.5, 22.7), "Qwen 3.8 Max": (49.7, 24.0),
          "GLM 5.2": (29.3, 18.0)}
fig1 = {18.0, 22.7, 24.7, 24.0, 20.0, 26.3}
print("  Table 2 AutomationBench rows, and whether the Pro score is in Figure 1(d):")
for name, (std, pro) in table2.items():
    print(f"    {name:26} {std} -> {pro}  drop {std - pro:4.1f}  in Fig. 1(d): {'yes' if pro in fig1 else 'no'}")
others = [s - p for n, (s, p) in table2.items() if n != "DeepSeek-V4.1-Flash-1017"]
print(f"  Without the -1017 row: six models, largest drop {max(others):.1f}")

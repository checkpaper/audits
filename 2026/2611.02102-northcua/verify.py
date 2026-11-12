"""Reproduce the check on the NorthCUA Technical Report, arXiv:2611.02102v3.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.02102", "v3", "51413a2814ec361b53ce31c2a8e0821944f9221861d997dab227010a144c4d57")

print("OSWorld 2.0 binary completion for NorthCUA, 108 tasks")
quote(doc, 57, "We evaluate OSWorld 2.0 on the full set of 108 tasks and retain binary completion, requiring a normalized score of 1")
quote(doc, 66, "NorthCUA-Nano Mid 68.7 0.9 24.2 54.9 SFT 76.1 12.0 40.9 64.2 NorthCUA-Mini Mid 68.3 2.8 25.6 65.4 "
               "SFT 83.3 18.5 46.3 68.0 NorthCUA-Pro Mid 75.8 9.3 30.6 69.1 SFT 85.9 27.3 63.6 69.6")
quote(doc, 68, "NorthCUA-Pro Before RL 85.9 27.3 63.6 69.6 After RL 88.6 30.6 66.8 73.9")
quote(doc, 62, "GPT-5.6 Sol (OpenAI, 2026b) Undisclosed 27.3 62.7")

binary = {"Nano Mid": 0.9, "Nano SFT": 12.0, "Nano RL": 13.0, "Mini Mid": 2.8, "Mini SFT": 18.5,
          "Mini RL": 18.5, "Pro Mid": 9.3, "Pro SFT": 27.3, "Pro RL": 30.6}
for stage, value in binary.items():
    k = round(value * 108 / 100)
    fits = abs(100 * k / 108 - value) <= 0.05 + 1e-9
    note = f"= {k}/108" if fits else f"is not k/108; nearest {100 * int(value * 1.08) / 108:.2f} and {100 * (int(value * 1.08) + 1) / 108:.2f}"
    print(f"  {stage:9} {value:5}  {note}")
print("  27.3 is also GPT-5.6 Sol's binary score in Table 9 (p. 62).")

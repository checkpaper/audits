"""Reproduce the checks on SparseRead (Read Less, Solve More), arXiv:2608.22237v2.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2608.22237", "v2", "bba857c4d9dd454c04d004ab7b4397fe121e0d3234dfe7431ec13cab89e93f96")
MODELS = ["DS-Flash", "DS-Pro", "Qwen3.6+", "GLM-5.1", "Kimi-K2.5", "Opus 5"]

print("Figure 6 (p. 6): NanoBot, six models x five scenarios (bar labels as printed)")
TOK = {  # token reduction (%) and score delta, in model order
    "Long-context reading": ("+21 0 0 0 +80 0 87 82 77 79 93 76"),
    "Multi-file audit and diagnosis": ("+34 +27 +18 +11 +21 +19 55 45 28 63 27 74"),
    "Structured analysis": ("+1 +11 +33 +14 +7 0 41 57 50 64 16 60"),
    "Web deep search": ("+10 +8 +7 +9 +14 +5 40 37 31 34 43 41"),
    "AI for Science (Materials chemistry)": ("+1 +3 0 −10 +7 +1 86 85 83 87 89 89"),
}
TIME = ["76 76 67 68 89 73", "52 49 36 59 34 78", "70 59 68 72 41 51", "33 30 23 28 37 35", "56 39 63 28 50 60"]
for (scen, s), t in zip(TOK.items(), TIME):
    quote(doc, 6, f"{scen} {s}")
    quote(doc, 6, t)
fig = {m: {"tok": [], "score": [], "time": []} for m in MODELS}
for (scen, s), t in zip(TOK.items(), TIME):
    x = s.replace("−", "-").split()
    for i, m in enumerate(MODELS):
        fig[m]["score"].append(float(x[i]))
        fig[m]["tok"].append(float(x[6 + i]))
        fig[m]["time"].append(float(t.split()[i]))

print("\nTable 1 (p. 7): NanoBot rows")
quote(doc, 7, "NanoBot Qwen3.6-Plus 69.0% +0.039 64.4% DeepSeek-Flash 22.4% +0.140 25.6% "
              "DeepSeek-Pro 71.3% −0.015 73.1%")
for m, tok, sc, tm in (("DS-Flash", 22.4, 0.140, 25.6), ("DS-Pro", 71.3, -0.015, 73.1)):
    f = fig[m]
    print(f"  {m}: Table 1 tokens {tok}%, score {sc:+.3f}, time {tm}%")
    print(f"    Figure 6 tokens {min(f['tok']):g} to {max(f['tok']):g}, "
          f"score deltas {[int(v) for v in f['score']]}, time {min(f['time']):g} to {max(f['time']):g}")
print("  DS-Flash: Table 1 tokens and time are below every Figure 6 cell.")
print("  DS-Pro: Table 1 has a score drop; no Figure 6 cell for DS-Pro has one.")
quote(doc, 7, "Score is preserved or improved in 29 settings; regressions occur for GLM-5.1 on AI for Science.")

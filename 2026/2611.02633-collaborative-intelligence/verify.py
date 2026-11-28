"""Reproduce the check on Measuring AI Agents as Teammates with Collaborative Intelligence, arXiv:2611.02633v1.

Run: python verify.py
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import download, fetch, quote  # noqa: E402

doc = fetch("2611.02633", "v1", "8d3f6ba1b553ec3032ea9583a100ac21a95783c92441b16276772bb9b57f0602")
COMMIT = "6b2689952d8b6412eac41fd09caf8342c43d923c"
CARDS = {
    "claude-fable-5-1": "3e60dea14d6ab48638fc857b08b4f69ef72cd15a44f4ee5cf172e40983cbe703",
    "claude-opus-5-5": "a9d47ffe05310dff9e1c4548183df6f7d4d001f318f49410636663ef14e9e43e",
    "claude-opus-5-5-high": "7c6e0c8d47eac4fbed4416d4a46c1a133f7a2f24341299531859431cb5cff83a",
}

print("Paper")
quote(doc, 5, "Every model runs on all 240 tasks, both public and held-out")
quote(doc, 5, "Solved alone, tasks the model passes alone, the only ones scored.")
quote(doc, 5, "Claude Opus 5.5 71.0 ±4.0 227")
quote(doc, 5, "Claude Fable 5.1 65.3 ±4.4 186")

print(f"\nReleased result cards (results/cards/<model>.json, commit {COMMIT[:7]})")
for model, sha in CARDS.items():
    path = download(f"https://raw.githubusercontent.com/zou-group/collaborative-intelligence/{COMMIT}/results/cards/{model}.json",
                    f"ci_{COMMIT[:7]}_{model}.json", sha)
    res = json.loads(path.read_text())["results"]
    a = res["all"]
    print(f"  {model:22s} scored {a['n_scenarios_complete']} of {a['n_scenarios']} tasks; "
          f"excluded for provider refusals {a['excluded']['provider_refusals']} "
          f"(public {res['public']['excluded']['provider_refusals']}, held-out {res['private']['excluded']['provider_refusals']}); "
          f"solved alone {a['n_gated']}; score {100 * a['score']:.1f}")

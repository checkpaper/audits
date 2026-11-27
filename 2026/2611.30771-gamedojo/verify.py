"""Reproduce the check on GameDojo: Benchmarking Real-Time Interactive Agents in Video Games, arXiv:2611.30771v1.

Run: python verify.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from common import fetch, quote  # noqa: E402

doc = fetch("2611.30771", "v1", "bab58c2f7b26c2ad384286d360f76b88bea6309ec34602dd17c64b73d2724687")

print("Claims")
quote(doc, 1, "especially in real-time interaction where all models win 0 score.")
quote(doc, 9, "In real time, all evaluated models score below Random in PG and achieve zero WR.")

print("\nTable 4 (p. 8), real-time columns: Easy, Medium, Hard, Average as WR / PG")
quote(doc, 8, "Entries report WR / PG (%) over 120 bosses; Average is the mean across difﬁculty levels.")
rows = {
    "Random": "Random 9.7 / 19.0 0.0 / 6.8 0.0 / 2.3 3.3 / 9.4 9.4 / 19.2 0.0 / 6.8 0.0 / 2.3 3.1 / 9.4",
    "GPT-6.1-Sol": "GPT-6.1-Sol 58.3 / 78.1 3.3 / 44.6 0.0 / 13.2 20.6 / 45.3 2.5 / 13.7 0.0 / 2.9 0.0 / 0.7 0.8 / 5.8",
    "GameDojo-4B": "GAMEDOJO-4B 52.2 / 76.7 11.9 / 40.3 0.0 / 11.8 21.4 / 42.9 6.4 / 26.3 0.0 / 8.2 0.0 / 2.5 2.2 / 12.3",
    "Gamer-35B-A3B": "Gamer-35B-A3B 4.2 / 12.9 0.0 / 3.3 0.0 / 1.0 1.4 / 5.7 0.8 / 6.6 0.0 / 2.0 0.0 / 0.5 0.3 / 3.1",
}
vals = {}
for name, q in rows.items():
    quote(doc, 8, q)
    nums = [float(x) for x in q.replace("/", " ").split()[-16:]]
    vals[name] = nums[8:]  # real-time: easy WR, PG, medium WR, PG, hard WR, PG, avg WR, PG
rand = vals["Random"]
for name in ["GPT-6.1-Sol", "GameDojo-4B", "Gamer-35B-A3B"]:
    v = vals[name]
    print(f"  {name:14s} real-time easy WR {v[0]:4.1f} (non-zero)   easy PG {v[1]:4.1f} vs Random {rand[1]:4.1f}   avg PG {v[7]:4.1f} vs Random {rand[7]:4.1f}")

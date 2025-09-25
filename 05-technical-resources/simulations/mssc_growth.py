#!/usr/bin/env python3
"""
MSSC toy model: logistic growth with simple temperature factor.
This is a placeholder for contributors to extend (substrate, pH, multi-species).
"""
from pathlib import Path
import csv, math

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
outfile = OUT / "mssc_growth_example.csv"

# Parameters (tweak/PR with literature-backed defaults)
r_max = 0.8      # 1/day, intrinsic growth
K = 1.0          # normalized carrying capacity (0..1)
T_opt = 30.0     # degC
sigma = 7.0      # degC width
dt = 0.1         # days
days = 20

def f_T(T):  # Gaussian temperature response [0..1]
    return math.exp(-((T - T_opt) ** 2) / (2 * sigma ** 2))

def step(x, r_eff, dt):
    return x + r_eff * x * (1 - x / K) * dt

rows = [("day","temp_c","biomass_norm")]
for T in (20.0, 30.0):
    x = 0.02
    t = 0.0
    while t <= days:
        r_eff = r_max * f_T(T)
        x = min(step(x, r_eff, dt), K)
        rows.append((round(t,2), T, round(x,4)))
        t += dt

with outfile.open("w", newline="") as f:
    csv.writer(f).writerows(rows)

print(f"Wrote {outfile}")

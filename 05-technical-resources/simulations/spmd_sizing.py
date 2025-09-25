#!/usr/bin/env python3
"""
SPMD area sizing: daily liters vs lab flux, field derate, sun hours.
"""
from pathlib import Path
import csv

OUT = Path(__file__).parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
outfile = OUT / "spmd_sizing_example.csv"

lab_flux = 3.4            # L/m2/h (UNIST lab headline)
derates = [0.4, 0.5]      # field fraction of lab
sun_hours = [5, 6]        # effective hours/day
targets = [60, 65]        # L/day

rows = [("derate","sun_h","target_Ld","required_area_m2","field_flux_L_m2_h","daily_L_m2")]
for d in derates:
    field_flux = round(lab_flux * d, 2)
    for sh in sun_hours:
        daily = round(field_flux * sh, 2)
        for tgt in targets:
            area = round(tgt / daily, 2)
            rows.append((d, sh, tgt, area, field_flux, daily))

with outfile.open("w", newline="") as f:
    csv.writer(f).writerows(rows)

print("derate sunH targetLd -> area(m2) fieldFlux dailyLm2")
for r in rows[1:]:
    print(f"{r[0]:.1f}    {r[1]}    {r[2]} -> {r[3]} m2  {r[4]}  {r[5]}")
print(f"Wrote {outfile}")

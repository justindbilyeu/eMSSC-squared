#!/usr/bin/env python3
"""
MSSC Bioreactor Growth Model (toy version).
Contributors: extend with substrate depletion, pH/temp effects, or multiple strains.
"""
import math

# Parameters (e.g., Geobacter or Shewanella strains)
initial_biomass = 0.1  # g/L
growth_rate = 0.05     # per hour
max_capacity = 10.0    # g/L
time_hours = 72

def microbial_growth(t, biomass, rate, capacity):
    """Logistic growth model"""
    return biomass * math.exp(rate * t) / (1 - (biomass/capacity) * (1 - math.exp(rate * t)))

print("Time (h), Biomass (g/L)")
for t in range(0, time_hours + 1, 12):
    biomass = microbial_growth(t, initial_biomass, growth_rate, max_capacity)
    print(f"{t}, {biomass:.2f}")

energy = biomass * 0.12  # 0.12 Wh/g (approx conversion)
print(f"Estimated energy at {time_hours}h: {energy:.2f} Wh")

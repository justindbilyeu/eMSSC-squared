#!/usr/bin/env python3
"""
Thermal model with realistic field derates and multi-stage GOR effect.
This replaces naive evaporation calc with conservative field assumptions.

References:
- UNIST lab flux headline: 3.4 L/m²/h (lab)
- Field derate band: 0.4–0.5 of lab
- Stage-to-stage effectiveness: ~0.85 additional stage
- Target GOR: 2.5–3.0 (optimized multi-stage)
"""

from dataclasses import dataclass

LAB_FLUX_LMH = 3.4  # L/m²/h


@dataclass
class EvapParams:
    environmental_factor: float = 0.5     # 0.4–0.5 realistic
    stages: int = 3                       # 3–4 stages practical
    stage_efficiency: float = 0.85        # per added stage beyond first
    sun_hours: float = 5.5                # 5–6 effective hours/day
    area_m2: float = 6.0                  # conservative area


def field_flux_lmh(p: EvapParams) -> float:
    eff = 1.0
    if p.stages > 1:
        eff = 1.0 - ((1.0 - p.stage_efficiency) ** (p.stages - 1))
    flux = LAB_FLUX_LMH * p.environmental_factor * eff
    return min(flux, LAB_FLUX_LMH)


def daily_output_L(p: EvapParams) -> float:
    return field_flux_lmh(p) * p.sun_hours * p.area_m2


if __name__ == "__main__":
    p = EvapParams()
    print(f"Field flux (L/m²/h): {field_flux_lmh(p):.2f}")
    print(f"Daily output (L/day) for area {p.area_m2} m²: {daily_output_L(p):.1f}")

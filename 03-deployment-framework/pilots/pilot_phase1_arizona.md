# Pilot Phase 1 — Arizona (Draft)

## Objective
Demonstrate a small TriSource + MSSC + SPMD array suitable for an arid U.S. agricultural setting.

## Targets
- **Water**: 100 L/day (aggregate), distillate + polished water
- **Energy (aux)**: < 7 kWh/day
- **Soil**: Halophyte zone established; track soil EC and OM%

## Layout (indicative)
- SPMD collector area: 7–8 m² (assuming 1.4–1.7 L·m⁻²·h⁻¹ field, ~5–6 sun hours)
- MSSC: pond → bog → irrigation trench; brine routed to halophytes
- QA/Post-treatment: EC/T, UV or chlorine, remineralization; 3–5 days storage

## Metrics & Logging
- Flux, daily L, kWh/L, GOR (if multi-stage used), TDS reduction, availability
- Soil EC (dS/m), soil OM (%), halophyte biomass
- Use: `05-technical-resources/experiments/data/log_template.csv`

## Steps & Timeline (draft)
1. Site selection + stakeholder alignment (2–4 weeks)
2. PoC module assembly + bench validation (4–6 weeks)
3. On-site install + training (1–2 weeks)
4. 60–90 day monitoring (data to repo)
5. Review + iterate; plan Phase 2 scaling

## Partners & Needs
- Local farm or ag co-op
- University lab for QC (water/soil)
- NGO/ESG sponsor for deployment

## Updated Performance Envelope (Derated)
See `_shared_derated_assumptions.md`. Pilot acceptance band:
- Water: **50–60 L/day**
- Aux energy: **≤ 9 kWh/day**
- Field area: **5–6 m²**
- GOR: **≥ 2.5**

## Validation Protocol Additions
- Unit tests passing for models & control (CI ok)
- 1000 h salt/fouling endurance plan
- Condenser fouling inspection every 7 days, photo log
- Fault injection tests: pump stall, sensor dropout, overflow

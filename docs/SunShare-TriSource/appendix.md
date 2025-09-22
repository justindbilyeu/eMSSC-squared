# 📑 Appendix — Tri-Source Water Node™

This appendix provides supplementary models, schematics, and technical data supporting the **Tri-Source Water Node™** white paper. It is a living document: diagrams, simulations, and empirical results will be added as they are generated.

---

## A1. System Diagrams

### A1.1 Process Flow Overview
- Full-node schematic showing:
  - **HydroLens™ Atmospheric Water Generator (AWG)**
  - **MSSC Node™ (Microbial Enrichment Reactor)**
  - **Solar-Powered Desalination (SPMD or Hybrid RO)**
  - Energy and water recirculation loops

*(Placeholder: insert vector schematic in `docs/diagrams/TriSource-Flow.svg`)*

### A1.2 Subsystem Schematics
- **HydroLens™ loop** (psychrometric condensation cycle, thermal reuse)
- **MSSC Node™ reactor design** (microbial cycling, aeration pathways)
- **Desalination chamber** (SPMD stack / membrane orientation)

---

## A2. Energy & Water Budgets

### A2.1 Sankey Diagrams
- **Energy flow**: Solar input → AWG load → MSSC aeration → desalination
- **Water flow**: Condensate → microbial treatment → brine/filtrate streams

*(Placeholder: `docs/diagrams/Sankey-Energy.png`, `docs/diagrams/Sankey-Water.png`)*

### A2.2 Energy Consumption Model
- Daily kWh demand breakdown by subsystem
- Efficiency assumptions (AWG COP, microbial aeration, desalination ΔT)

---

## A3. Psychrometric Models

- **Atmospheric water yield curves** vs. relative humidity and temperature
- Model sensitivity to **dew point depression**
- Climate zone performance benchmarks (arid, coastal, humid tropical)

*(Placeholder: Wolfram/Matlab notebooks in `docs/models/psychrometric/`)*

---

## A4. Electrochemical & Brine Management

### A4.1 MDC & Membrane Performance
- Voltage-current curves for solar-driven membrane distillation cells
- Ion selectivity and fouling dynamics

### A4.2 Brine Crystallization
- Salt precipitation order: CaSO₄ → MgCO₃ → NaCl → MgCl₂
- Sacrificial crystallization tank design notes
- Potential reuse loops (e.g., NaCl for AWG hygroscopic media)

*(Placeholder: Wolfram simulation plots in `docs/models/brine/`)*

---

## A5. MSSC Biome Dynamics

- Target microbial consortia: diazotrophs, phosphate solubilizers, cyanobacteria, biofloc species
- Aeration and carbon:nitrogen balance guidelines
- Preliminary lab test log (2025–ongoing)

*(Placeholder: `docs/data/MSSC-tests.md`)*

---

## A6. Deployment Scenarios

- **Village-scale node (50–75 L/day)** deployment model
- **School-scale node (250–500 L/day)** with multiple arrays
- Integration into **SunShare HomeNode™** for residential use

*(Placeholder: deployment schematics in `docs/diagrams/deployment/`)*

---

## A7. Standards & Compliance

- ISO/IEC references for water quality and testing
- Safety standards for solar-membrane distillation systems
- Regulatory pathways (US EPA, WHO potable water guidelines)

---

## A8. Open Questions / Future Work

1. Optimization of **AWG condenser surfaces** (nanocoatings, MOFs, graphene oxide).
2. Long-term stability of **MSSC microbial consortia** under variable feedstocks.
3. Hybridization of **SPMD with electrodialysis** for brine load reduction.
4. Integration of **energy storage** (thermal or battery) into the Tri-Source Node.
5. Field trials in diverse climate zones to validate psychrometric assumptions.

---

📌 **Note:** Diagrams, simulations, and datasets will be uploaded iteratively. See the `/docs/diagrams` and `/docs/models` folders in this repository for the most current versions.

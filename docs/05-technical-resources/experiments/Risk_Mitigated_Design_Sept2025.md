# Risk-Mitigated Pilot Experiment Design — eMSSC²  
**Date:** September 2025  
**Authors:** eMSSC² Collective (SAGE, Claude, DeepSeek inputs)

---

## 🎯 Overview
Two-phase program designed to validate eMSSC² TriSource desalination integration with UNIST’s LSMO absorber technology. Provides statistically robust, funder-ready data for DOE DWPR, USAID WASH, and Gates Foundation applications.

- **Phase 1:** 0.5 m² inverse-L prototype (carbon black photothermal layer)  
- **Phase 2:** 3–4 stage GOR bench rig for heat recovery validation  

---

## Phase 1 — 0.5 m² Proof-of-Concept

### Environmental Controls
- Solar irradiance: pyranometer (±2%, 1-min interval)  
- Ambient temperature: shielded thermistors (±0.1 °C)  
- Relative humidity: capacitive sensor (±2% RH)  
- Wind speed/direction: 3-cup anemometer  
- Pressure: digital barometer (±0.1 hPa)  

### Feed Water Controls
- Salt matrix: 3.5%, 5.0%, 7.5% NaCl  
- Flow: peristaltic pump (±1%)  
- TDS, pH, EC baseline  

### Replication
- 3 identical 0.5 m² modules + 1 control (no photothermal coat)  
- Each test repeated ≥3×  

### Failure Mode Instrumentation
- Salt clogging: imaging + wick resistance + flow monitoring  
- Photothermal degradation: IR thermal mapping, weekly spectral reflectance  
- Condenser fouling: distillate vs. vapor recovery, surface temp sensors  

### Metrics
- Flux (L/m²/hr normalized to kW/m²)  
- Daily output (L/m²/day)  
- Distillate quality (TDS, EC)  
- Aux energy use (kWh/L)  
- Availability (%)  

---

## Phase 2 — Multi-Stage GOR Bench Rig

### Design Specs
- 4-stage cascading design, ≥80% heat recovery efficiency  
- ∆T per stage: 15–20 °C  
- RTD sensors, differential pressure, flow meters, heat flux sensors  

### Validation Protocol
- Baseline: single-stage GOR  
- Add stages sequentially → measure GOR gain  
- Target: GOR ≥2.5, heat recovery ≥75%  

### Statistical Requirements
- Duration: 480 h (20 days)  
- ≥20 measurements/day  
- CV <10% for primary metrics  
- 95% confidence intervals on all claims  

---

## 📊 Success Criteria

**Phase 1:**  
- Flux ≥1.0 L/m²/hr avg over 480 h  
- <10% active area salt crusting  
- >99% TDS rejection  
- >90% availability  

**Phase 2:**  
- GOR ≥2.0 (goal 2.5+) in 3–4 stage  
- Heat recovery >75%  
- Multi-stage cost <$200/m²  

---

## 📅 Timeline (12–14 weeks)

- **Weeks 1–2:** Fabrication + instrumentation (PoC + GOR rig)  
- **Weeks 3–8:** 480 h PoC runs (in parallel with GOR rig assembly)  
- **Weeks 9–12:** Multi-stage GOR validation  
- **Weeks 10–14:** Data analysis + funding package prep  

---

## 🎯 Funding Alignment

- **DOE DWPR:** TRL 4–5 demo, quantified risk assessment  
- **USAID WASH:** Field-relevant operation, simplicity metrics  
- **Gates Foundation:** Ag resilience economics + integration  

---

## 📂 Repo Path

05-technical-resources/experiments/  
Risk_Mitigated_Design_Sept2025.md  
data/ (future logs, calibration, replication sets)  
figures/ (instrumentation diagrams, photos)


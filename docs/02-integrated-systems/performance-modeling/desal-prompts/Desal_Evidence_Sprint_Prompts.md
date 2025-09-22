# Desal Evidence Sprint — Dispatch Prompts (v0.1)

Use these with DeepSeek, Grok, Gemini, Claude. Return results into `ProjectRadar.csv`, `TechRanges.csv`, `FundingTracker.md`, and `Permitting_Checklists.md` as appropriate.

## DeepSeek — Systems + Math + Ranges
- Build a global project radar (2019–2025): capacity (m³/d), SEC (kWh/m³), recovery (%), water price (USD/m³), tech, status, owner, funder.
- Consolidate tech ranges for RO, ED/EDR, MD, CDI, solar interfacial (median + IQR).
- Provide governing equations/constraints per tech.
- Output tables: `ProjectRadar.csv`, `TechRanges.csv` (units included in headers/notes).

## Grok — Funding + Headlines
- FOAs + awards (DWPR, NAWI, state grants) with dates and $ amounts.
- Top 10 new/expanded plants (2023–2025) with claimed SEC or price.
- One-pager: What changed since 2022 in desal decarbonization + pilots?
- Output: `FundingTracker.md` (fill table + award log).

## Gemini — Scholar Benchmarks
- Peer-reviewed SEC/recovery ranges and field conditions (pretreatment, temperature).
- Evidence table with median/IQR and representative citations for RO, ED/EDR, MD, CDI, solar-interfacial.
- Output: add rows to `TechRanges.csv` and attach a citations list.

## Claude — Policy/Permitting
- Inland brackish (Texas) and coastal (California) permitting checklists.
- Funding playbook: program, eligibility, match, cadence, how to apply.
- Output: `Permitting_Checklists.md` (expand) and a separate `FundingPlaybook_US.md` if needed.

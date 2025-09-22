# 🌐 Tri‑Source Water Node™ & SunShare Home Node™  
### **Integrated Roadmap v0.1** — 2025‑06‑12

> “Drinkable water + resilient power for a family today → village‑scale node tomorrow.”

---

## 1  Purpose & Scope  
This document unifies the current design threads, critiques, and execution steps for **two sister projects**:

* **Tri‑Source Water Node™** – community‑scale water–energy–microbial platform.  
* **SunShare Home Node™** – household‑scale PV + grey‑/rain‑water system with on‑device AI control.

It is intended as a living roadmap, hosted in the repository root (`/ROADMAP.md`), updated via pull‑request as milestones are met.

---

## 2  Snapshot (June 2025)

| Project | Core purpose | Current assets | Immediate gap |
|---------|--------------|----------------|---------------|
| **Tri‑Source Water Node** | Solar‑integrated AWH + desal + MSSC loop | v1.2‑1.3 white‑paper, Sankey, Gemini & SciSpace critique, initial AWG/MD budgets | Bench‑top demonstrator (≥5 L d⁻¹) with live telemetry |
| **Home Node** | Residential PV, grey‑water treatment, Pi‑edge intelligence | Wiki outline, $450 BOM, Pi‑edge blueprint & success metrics | Build‑ready wiring diagram + flash‑and‑run repo |

---

## 3  Why advance them **together**

1. **Shared edge stack** – same Raspberry Pi / Jetson loop.  
2. **Funding optics** – small proof de‑risks the larger concept.  
3. **Parts overlap ≈ 70 %** – valves, sensors, PV, enclosures.  
4. **Narrative** – household → community scaling resonates with investors & NGOs.

---

## 4  90‑Day Execution Map

| Day range | Dual‑track deliverables | Success criteria |
|-----------|------------------------|------------------|
| **1 – 10** | • Repo hygiene (triage docs → `/docs/`)  \|  • Add `pi-edge-blueprint.md` to Home Node | Repos clone with **zero** missing links |
| **11 – 30** | • Assemble Pi‑5 edge prototype  \|  • 48 h autonomous run demo video | Pi draws <7 W, logs light+temp every 60 s |
| **31 – 45** | • Add 12 V pump + condenser loop (Tri‑Source stub)  \|  • LLM suggests duty‑cycle tweak | ≥1 closed‑loop adjustment from local model |
| **46 – 60** | • Grey‑water bio‑sand demo (Home Node)  \|  • Node‑RED dashboard plots turbidity | ≥30 % turbidity drop; “safe to irrigate” flag |
| **61 – 75** | • Upgrade white‑paper to v1.3  \|  • Quick‑start guide & GIF | GitHub Pages auto‑build passes |
| **76 – 90** | • External beta test (makerspace)  \|  • Submit Tri‑Source abstract to conference | ≥1 external LOI + conference sub‑ID |

---

## 5  Roles & Tooling

| Role | Human / Model | Responsibilities |
|------|---------------|------------------|
| **Integrator** | *Justin* | Hardware build, sensor wiring, field video |
| **Creator LLM** | *Sage* | Roadmaps, README polishing, investor decks |
| **Critic LLM** | *Claude* | PR review, risk checks, citations |
| **Rigorizer LLM** | *DeepSeek-Coder* | Tables, code, math derivations |
| **Archivist** | GitHub Action + tiny local LLM | Auto‑changelog, markdown‑lint |

`crew.json` (example):

```json
{
  "hardware/":        "Integrator",
  "docs/":            "Creator",
  "analysis/":        "Critic",
  "scripts/":         "Rigorizer",
  ".github/":         "Archivist"
}
```

---

## 6  Risk Register (lite)

| Risk | Early sign | Mitigation |
|------|------------|------------|
| Pi thermal throttling | >75 °C | Aluminium case + fan; limit threads |
| Condenser no dew‑point | 0 L after 24 h | Add shade cloth; mist pre‑cool |
| Doc sprawl | Divergent “latest” PDFs | Weekly summary; single `/docs/` root |

---

## 7  Bench Checklist (before wiring)  

* Order BOM (see Appendix A); overnight ship sensors.  
* Clear 1 m table, 12 V bench supply, multimeter.  
* Tripod + LED light for 60‑sec demo footage.  

---

## 8  Appendix A — $450 Home Node BOM

| Qty | Item | Price (US$) |
|----:|------|-----------:|
| 2 | 100 W mono PV panels | 140 |
| 1 | 12 V / 20 Ah SLA (LiFePO₄ optional) | 65 |
| 1 | Pi 5 (8 GB) + active case | 95 |
| 1 | 64 GB µSD / 256 GB NVMe | 15 |
| 1 | USB‑C buck (12→5 V) | 12 |
| 1 | BH1750 light sensor | 4 |
| 1 | DS18B20 temp probe | 6 |
| 1 | Solid‑state relay (5→12 V) | 8 |
| 1 | Mini 12 V diaphragm pump | 24 |
| misc | wiring, DIN box | 20 |
| **Total** | **≈ $445** |

*(Tri‑Source BOM supersedes Home Node items where noted.)*

---

## 9  Appendix B — Pi‑Edge Quick Start

```bash
# Ubuntu 24.04 LTS (64‑bit)
sudo apt update && sudo apt install -y git python3-venv
# Ollama + TinyLlama
curl -L https://ollama.ai/install.sh | sh
ollama pull tinyllama:1.1b-chat
# Node‑RED
sudo snap install nodered
# Enable I2C / 1‑Wire in raspi‑config (Pi OS) or dt‑overlay for Ubuntu
```

Node‑RED minimal flow: Lux → SQLite ; Temp → dashboard ; `/ask` → Ollama REST.

---

### 📌  One‑sentence mantra  
> **“Small, buildable proof → sensor data → story → scale.”**

Update this file with each milestone commit (`## v0.2`, `## v0.3`, …). Pull‑requests that touch hardware **must** include photo evidence or power logs.

*End of v0.1*  

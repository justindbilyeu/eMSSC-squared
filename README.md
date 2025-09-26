![System Diagram](05-technical-resources/figures/system-diagram.png)
*Figure: eMSSC² integrates MSSC microbial bioreactors, TriSource nodes, and UNIST LSMO solar desalination modules into a zero-electric regenerative system.*

# eMSSC² — Exponential Microbial Systems for Sustainable Communities

**Vision:** Zero-electric, regenerative water-energy-soil systems integrating MSSC, TriSource, and UNIST LSMO solar desalination.

We orchestrate microbial electrochemical bioreactors, TriSource hybrid nodes, and photothermal desalination modules into a deployable platform for climate-stressed communities. The program aligns engineering, policy, and capital pathways so DOE/USAID reviewers, UNIST collaborators, and ESG funders can accelerate field-ready infrastructure that regenerates water, energy, and soil without grid dependencies.

## 🚀 Join the eMSSC² Revolution
- **Contribute**: Fork the repo, add simulations (`05-technical-resources/simulations/`), TriSource designs (`02-integrated-systems/`), or pilot plans (`03-deployment-framework/`).  
- **Discuss**: Join GitHub Discussions (enabled soon) to share ideas and Q&A.  
- **Spread the Word**: Star the repo and share with #eMSSC2 #OpenSource #Sustainability.  
- **Explore**: See our [System Diagram](05-technical-resources/figures/system_diagram.md).  

![TriSource Node](05-technical-resources/figures/trisource_node_simple.svg)
*Figure: TriSource integrates AWG, SPMD solar desal, and MSSC wetland polishing → QA → clean water storage.*

## 🔓 Open Source Commitment
This project operates as an open blueprint for regenerative water–energy–soil systems.  
Read our full statement here: [OPEN_SOURCE_DECLARATION.md](OPEN_SOURCE_DECLARATION.md).

## 📂 Repository Map

| Folder | Purpose |
|--------|---------|
| 01-foundation-technology/ | Core MSSC microbial system documents, patent drafts, and prior art defense. |
| 02-integrated-systems/ | TriSource node specifications, solar desal integration, PoC geometry builds. |
| 03-deployment-framework/ | Status updates, pilot planning, and deployment pathway documentation. |
| 04-business-development/ | Partnerships (e.g., UNIST), funding strategies, and market positioning. |
| 05-technical-resources/ | Experimental designs, test data templates, BOMs, and technical figures. |
| 06-pilot-implementations/ | Logs and documentation of real-world deployments (future). |

## Status Snapshot — September 2025

- MSSC provisional patent and IP defense filed
- TriSource integration defined
- UNIST partnership brief drafted
- Risk-mitigated experimental design finalized
- Funding targets identified (DOE DWPR, USAID WASH, Gates Foundation)

## Key Links

- [Status Update](docs/03-deployment-framework/README.md) — Current milestones, pilot gating, and sequencing toward 2026 field trials.
- [UNIST Partnership Brief](docs/04-business-development/pitch-materials/UNIST-Partnership-Brief.md) — Collaboration framing with UNIST’s LSMO solar desalination program.
- [Risk-Mitigated Design](docs/05-technical-resources/experiments/Risk_Mitigated_Design_Sept2025.md) — Validation protocol aligning lab, pilot, and deployment readiness levels.

## 🤝 How to Engage

- **Contribute**: Engineers, scientists, and practitioners are welcome to add to experiments, simulations, or deployment docs through pull requests.
- **Partner**: Institutions and companies (e.g., UNIST, NGOs, ag co-ops) can collaborate on pilots, field validation, and technology integration.
- **Fund**: Supporters and ESG investors can help accelerate prototypes, pilot sites, and agricultural resilience deployments.
- **Follow**: Track progress through our [Status Updates](03-deployment-framework/README_Status_Sept2025.md) and upcoming GitHub Pages site.

## ⚡ Quick Start
- Run a sizing sim: `python 05-technical-resources/simulations/spmd_sizing.py`
- Try the MSSC toy model: `python 05-technical-resources/simulations/mssc_growth.py`
- Add a part to the BOM: edit `05-technical-resources/boms/trisource_poc_bom.csv`
- Propose a pilot: edit `03-deployment-framework/pilots/pilot_phase1_arizona.md` and open a PR

### 🤖 Use AI as a Reviewer
When you ask Claude/DeepSeek/Grok/ChatGPT for help, include:
- File paths (e.g., `02-integrated-systems/TriSource/control_logic.py`)
- Task goal & constraints
- Links to KPIs and diagrams

### 🔧 Run the Core Checks
```bash
python 05-technical-resources/simulations/thermal_model.py
python 05-technical-resources/simulations/spmd_sizing.py  # if present
pytest -q
```

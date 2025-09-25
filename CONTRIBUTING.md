# Contributing to eMSSC²

Thanks for helping build **zero-electric, regenerative water–energy–soil systems**.

## Quick Start
1. **Fork & Branch**: Fork → create a feature branch.
2. **Pick a Lane**:
   - **Simulations**: Add/extend models in `05-technical-resources/simulations/`.
   - **Schematics**: Add SVGs to `05-technical-resources/figures/`.
   - **Hardware/BOMs**: Contribute parts lists to `05-technical-resources/boms/`.
   - **Pilots**: Propose/shape pilots in `03-deployment-framework/`.
3. **Data**: Use `05-technical-resources/experiments/data/log_template.csv` for experiment logs.
4. **PRs**: Open a pull request with context (what/why), and include screenshots or sample outputs where relevant.

## Style & Conventions
- **Code**: Python ≥3.10, PEP8, type hints encouraged.
- **CSV**: UTF-8, ISO-8601 timestamps (`timestamp_iso`), snake_case headers.
- **Figures**: Prefer SVG (vector). One accent color `#0B84F3` and orange `#FF7F0E` for brine.
- **Docs**: Clear headings, short sections, link related files/paths.

## How to Brief AI Collaborators
We use AI (Claude, DeepSeek, Grok, Kai, ChatGPT) as **on-demand reviewers**. They have no cross-session memory, so include:
1. File path(s) you’re editing.
2. Task goal and constraints (audience, license, deadline).
3. Links to related docs (e.g., KPIs, schematics, status update).

**Template prompt:**
> Review `02-integrated-systems/TriSource/INTERFACES.md` for clarity and alignment with `05-technical-resources/metrics/KPIs.md` and schematic `05-technical-resources/figures/trisource_node_simple.svg`. Suggest concise edits in Markdown.

## Community
- **Issues**: Use GitHub Issues for bugs/ideas.
- **Discussions** *(enable in Settings)*: “Announcements”, “Q&A”, “Experiments”, “Pilots”.
- **Code of Conduct**: See `CODE_OF_CONDUCT.md`.

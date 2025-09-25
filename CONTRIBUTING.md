# Contributing to eMSSC²

Thank you for helping build open, regenerative water–energy–soil systems. Follow the guidelines below to ensure contributions are reviewable and reproducible.

## Contribution Flow
1. **Discuss**: Open an issue to describe the improvement, bug, or research task. Link to any relevant folders (e.g., `docs/05-technical-resources/experiments/Risk_Mitigated_Design_Sept2025.md`).
2. **Design**: Outline your approach, data requirements, and dependencies. When logging experiments, use or extend the [data log template](05-technical-resources/experiments/data/log_template.csv) so field teams can replay the work.
3. **Implement**: Create a branch and add your updates with clear commit messages. Document assumptions, calculations, and references directly in the files you modify.
4. **Review**: Submit a pull request referencing the issue. Summarize changes, validation steps, and any follow-on tasks for the roadmap.
5. **Merge & Log**: After approval, merge the PR and update related status docs or experiment logs to keep downstream collaborators informed.

## Documentation Expectations
- Provide context and intent for every change so reviewers understand the scenario.
- Include calculations, parameter tables, or simulation configs used to generate results.
- Attach figures, schematics, or data files in the appropriate subdirectories to maintain traceability.

## How to Brief AI Collaborators

We use AI systems (e.g., Claude, Grok, DeepSeek, Kai) as **on-demand reviewers** for research synthesis, doc clarity, and technical cross-checks. They do not retain memory between sessions.

**When asking an AI for help, include:**
1. The exact file or path you’re working on (e.g., `05-technical-resources/experiments/Risk_Mitigated_Design_Sept2025.md`).
2. A short summary of the task (what needs review or drafting).
3. Any key constraints (e.g., license, audience, deadlines).
4. Links to related docs (status update, KPIs, schematics).

**Example prompt snippet:**
> “Please review `02-integrated-systems/TriSource/INTERFACES.md` for clarity and completeness. Ensure it aligns with `05-technical-resources/metrics/KPIs.md` and references the schematic `05-technical-resources/figures/trisource_node_simple.svg`. Output concise edits in Markdown.”

Treat AI output as assistance to human contributors; verify before merging.

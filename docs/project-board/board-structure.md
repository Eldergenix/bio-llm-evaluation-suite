# Project Board Structure (Q4 2025)

Use this outline to configure a public GitHub project (Beta) or Kanban board that reflects the execution plan in `README.md` and `TODO.md`.

## Board Columns

1. **Backlog** — Ideas and tasks not yet scheduled; review weekly.
2. **Scoping** — Active design/planning (requirements gathering, outreach alignment).
3. **In Progress** — Tasks with ongoing implementation.
4. **Review & Validation** — Pending maintainer review, evaluation, or testing.
5. **Comms & Launch** — Demos, blog posts, lab reports, announcements.
6. **Done** — Completed tasks with evidence linked (PRs, reports).

## Swimlanes / Labels

- `flagship::bio-llm-eval`
- `flagship::vla-robotics`
- `flagship::agentic-platform`
- `contrib::galaxy`
- `contrib::maia`
- `contrib::maistro`
- `contrib::cognitive-kernel-pro`
- `contrib::prime-intellect`
- `comms`
- `ops`

## Initial Issues (create as GitHub issues/cards)

| Title | Description | Labels | Column |
| --- | --- | --- | --- |
| Draft Bio-LLM dataset compliance checklist | Compile licensing, PHI, preprocessing requirements for candidate datasets. | `flagship::bio-llm-eval`, `ops` | Scoping |
| Outreach: Galaxy maintainers | Personalise and send email using template; track follow-up date. | `contrib::galaxy`, `comms` | In Progress |
| Outreach: MAIA maintainers | Personalise and send email using template. | `contrib::maia`, `comms` | Scoping |
| Outreach: Cognitive Kernel-Pro maintainers | Personalise and send email using template. | `contrib::cognitive-kernel-pro`, `comms` | Scoping |
| Bio-LLM Eval: Baseline pipeline design doc | Flesh out sections 4–7 (architecture, experiments, roadmap) with actionable tasks. | `flagship::bio-llm-eval`, `ops` | Scoping |
| Bio-LLM Eval: Dataset audit scripts | Implement reproducible ingestion scripts for PubMed and ClinSum. | `flagship::bio-llm-eval` | Backlog |
| Galaxy GPU acceleration PR #1 | Identify CPU-bound tool; draft GPU-enabled prototype. | `contrib::galaxy` | Backlog |
| Cognitive Kernel-Pro biomedical evaluator | Define metrics + datasets for GAIA-style evaluation. | `contrib::cognitive-kernel-pro` | Backlog |
| Lab Report 2025-10-27 | Collect metrics, demos, and narrative for fortnightly update. | `comms` | Backlog |

## Automation Ideas

- Configure auto-move rules: when issue gets `status::review`, send to **Review & Validation**.
- Link lab reports and changelog entries directly in issue comments when tasks close.
- Use GitHub Actions to update board upon PR merge (optional).

## Next Steps

1. Create the GitHub project (user-level) named “AI/Bio Research 2025”.
2. Add the columns above and populate cards using the issue list.
3. Share project link in profile README and pinned repositories once populated.

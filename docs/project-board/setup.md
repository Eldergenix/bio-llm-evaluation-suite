# GitHub Project Setup — AI/Bio Research 2025

Follow these steps to create and populate the public project board using GitHub Projects (Beta).

## 1. Create the Project

1. Navigate to `https://github.com/users/nexisdev/projects`.
2. Click **New project** → choose **Board** layout.
3. Name the project **AI/Bio Research 2025** and set visibility to **Public** so recruiters and collaborators can view progress.
4. Add a short description referencing the roadmap in `README.md`.

## 2. Configure Columns

Create columns matching `docs/project-board/board-structure.md`:

- Backlog  
- Scoping  
- In Progress  
- Review & Validation  
- Comms & Launch  
- Done

Reorder columns as needed via drag-and-drop.

## 3. Define Labels & Fields

1. In the project settings, add a **Single select** custom field named `Focus` with the values:
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
2. Optionally add a `Status` field mirroring the columns for automation.

## 4. Seed Issues & Cards

For each draft in `docs/issues/`, create a GitHub issue in this repository (or the target upstream repo) and add it to the project:

```bash
# Example using gh CLI
gh issue create \
  --title "Galaxy: GPU-Accelerate bwa_mem Tool" \
  --body-file docs/issues/galaxy-gpu-acceleration.md \
  --label "contrib::galaxy" \
  --project "nexisdev/AI-Bio Research 2025"
```

Repeat for:
- `docs/issues/cognitive-kernel-pro-biomed-eval.md`
- Upcoming MAIA deployment issue draft (to be created)
- Bio-LLM evaluation tasks derived from `docs/designs/bio-llm-eval.md`

Assign the appropriate `Focus` value for each card.

## 5. Automations (Optional)

- Enable auto-move: when `Status` is set to `Review`, move to **Review & Validation** column.
- Create a workflow with `gh workflow run` or GitHub Actions to add merged PRs to **Comms & Launch** for documentation follow-up.

## 6. Share the Project

- Add the project link to the GitHub profile README under the “Immediate Action Items” section.
- Pin the project board in GitHub profile highlights.
- Include the link in lab reports and outreach emails to show transparent work tracking.

## 7. Maintenance

- Review the board every Monday; update statuses before sending lab reports.
- Archive completed cards after documenting them in `CHANGELOG.md`.

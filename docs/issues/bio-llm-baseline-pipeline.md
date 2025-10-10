# Issue Draft: Bio-LLM Evaluation Baseline Pipeline

- **Repository Target:** nexisdev/bio-llm-eval (this repo)  
- **Labels:** `flagship::bio-llm-eval`, `pipeline`, `ops`
- **Milestone:** Bio-LLM Evaluation Suite Alpha (Due 28 Dec 2025)

## Summary

Implement the baseline fine-tuning + evaluation pipeline described in `docs/designs/bio-llm-eval.md`. The pipeline should run parameter-efficient fine-tuning on PubMedQA and produce evaluation reports capturing accuracy, hallucination rate, and safety metrics.

## Goals

1. Create reproducible training scripts (Tinker/Accelerate) for LoRA/QLoRA fine-tunes.  
2. Integrate evaluation harness covering PubMedQA accuracy, hallucination probes, and toxicity checks.  
3. Emit structured reports (JSON + Markdown) and artefact logs.

## Tasks

- [ ] Set up project structure (`src/training`, `src/evaluation`, `configs/`).  
- [ ] Implement dataset loaders for PubMedQA and baseline tokenization.  
- [ ] Build training runner supporting LoRA/QLoRA configs (FP16/BF16).  
- [ ] Add evaluation scripts (accuracy, hallucination prompts, toxicity scan).  
- [ ] Generate Markdown/JSON reports with metrics + run metadata.  
- [ ] Package CLI entry point (`python -m bio_llm_eval.run --config configs/pubmedqa.yaml`).  
- [ ] Document prerequisites (GPU requirements, dataset paths) in `README.md`.  
- [ ] Schedule CI checks (lint, unit tests, lightweight CPU smoke test).

## Acceptance Criteria

- Running the configured command completes fine-tuning on a small subset (for smoke test) and produces reports in `reports/`.  
- Evaluation scores automatically logged and appended to `CHANGELOG.md` entry.  
- Code formatted/linted; CI pipeline green.  
- Documentation provides setup + troubleshooting steps.

## Notes

- Extendable to MultiClinSum and BioLaySumm in later issues.  
- Align configuration naming with future multi-dataset support (e.g., `configs/tasks/*.yaml`).

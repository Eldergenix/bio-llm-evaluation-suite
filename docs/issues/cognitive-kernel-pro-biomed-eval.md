# Issue Draft: Biomedical Evaluation Suite for Cognitive Kernel-Pro

- **Repository Target:** cognitive-kernel-pro/cognitive-kernel-pro (or evaluation subrepo)
- **Labels:** `evaluation`, `bio-med`, `agents`, `flagship::agentic-platform`, `contrib::cognitive-kernel-pro`
- **Milestone:** Q4 2025 evaluation roadmap

## Summary

Kernel-Pro currently lacks domain-specific evaluation harnesses for biomedical reasoning tasks. This issue introduces a GAIA-style evaluation suite covering PubMedQA, BioLaySumm, and ClinSum benchmarks with automated metric aggregation and qualitative trace review to showcase agent reflection capabilities.

## Goals

1. Implement dataset loaders and prompt templates tailored to biomedical tasks.
2. Integrate automatic scoring (accuracy, ROUGE, factuality) and guardrail checks (hallucination probes, toxicity).
3. Provide agent reflection logging and replay notebooks for qualitative analysis.

## Tasks

- [ ] Confirm dataset licensing and availability for open-source distribution.
- [ ] Design evaluation config schema (YAML/JSON) for specifying tasks, metrics, and guardrails.
- [ ] Implement loaders + preprocessors for PubMedQA, BioLaySumm, ClinSum.
- [ ] Add evaluation runners leveraging Kernel-Pro agent APIs.
- [ ] Integrate safety checks (toxicity, hallucination detection) into evaluation loop.
- [ ] Produce sample reports (Markdown/JSON) with aggregated metrics and agent transcripts.
- [ ] Document setup, execution commands, and extension guidelines.

## Acceptance Criteria

- Running `python eval_biomed.py --config configs/biomed.yaml` executes all tasks end-to-end on sample data.
- Evaluation outputs include both quantitative metrics and reflection logs saved per task.
- Tests cover dataset loading and scoring to ensure reproducibility.
- Documentation demonstrates how maintainers/community can plug in new biomedical tasks.
- PR merged before 30 Nov 2025 with maintainer approval.

## Notes

- Coordinate with maintainers on preferred evaluation framework (e.g., Hydra config, Pydantic models).
- Explore cross-linking outputs with Galaxy workflows for multi-agent experiments (future work).

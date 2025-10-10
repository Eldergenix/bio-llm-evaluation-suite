# Bio-LLM Evaluation Suite — Design Draft (v0.1)

**Owner:** @nexisdev  
**Status:** Drafting (13 Oct 2025)  
**Target Alpha Release:** 28 Dec 2025

## 1. Objectives

- Build an automated harness that fine-tunes open-source language models on curated clinical and genomic corpora.
- Provide safety and performance audits (bias, hallucination, compliance) with encrypted traceability for regulated environments.
- Enable reproducible benchmarking and comparison across models, datasets, and guardrail configurations.

## 2. Background & Motivation

Clinically focused LLMs (e.g., MedPaLM, BioGPT) remain closed or difficult to evaluate under real-world regulatory constraints. Researchers and biotech teams need a standardised pipeline to:
- vet open models for clinical suitability,
- experiment with fine-tuning recipes,
- and report safety metrics that satisfy internal review boards.

## 3. Scope & Deliverables

### In Scope
- Data ingestion pipelines for approved corpora (MIMIC-III de-identified, PubMed abstracts, ClinSum).
- Configurable fine-tuning workflows (LoRA, QLoRA, full finetune) using Tinker integration.
- Evaluation modules covering factuality, toxicity, bias, privacy leakage, and domain-specific QA accuracy.
- Reporting layer exporting encrypted audit bundles (metrics, prompts, responses).

### Out of Scope (v0.1)
- Direct handling of PHI without prior de-identification.
- Deployment UI; initial release focuses on CLI/Notebook workflows.

## 4. System Architecture

1. **Data Layer:**  
   - Dataset registry with metadata (license, sensitivity score, preprocessing scripts).  
   - Optional homomorphic encryption hooks for sensitive logs.
2. **Training Orchestrator:**  
   - Tinker pipelines for orchestrating LoRA/QLoRA runs across GPUs.  
   - Config templates stored in `configs/`.
3. **Evaluation Engine:**  
   - Task-specific evaluators (QA, summarisation, clinical coding).  
   - Safety scanners (toxicity, hallucination detectors, leakage probes).
4. **Reporting & Compliance:**  
   - Markdown/JSON reports with metric tables, charts.  
   - Encrypted artefacts (age/scope-controlled sharing).

## 5. Experiment Plan

| Experiment | Hypothesis | Configuration | Metric | Success Criteria |
| --- | --- | --- | --- | --- |
| Baseline Fine-Tune | QLoRA on BioGPT improves clinical QA accuracy | BioGPT + PubMedQA | Accuracy | ≥3% absolute gain vs. base |
| Safety Guardrail | Augment with retrieval-based guardrails reduces hallucinations | BioGPT + retrieval guard | Hallucination Rate | ≤5% hallucinated responses |
| Differential Privacy | DP fine-tuning retains accuracy within 2% while preventing leakage | BioGPT + DP optimizer | Privacy Leakage | No leaked PHI in probes |

## 6. Risks & Mitigations

- **Data Compliance:** Mitigation: restrict to approved open datasets; integrate de-identification scripts; maintain audit logs.  
- **Compute Budget:** Mitigation: prioritise parameter-efficient fine-tunes; leverage spot instances; automate cleanup.  
- **Evaluation Drift:** Mitigation: version evaluation datasets; store evaluator configs alongside runs.

## 7. Roadmap

- 13–20 Oct: Finalise dataset list, preprocessing scripts, and evaluation metrics.  
- 21 Oct–10 Nov: Implement training orchestrator and baseline fine-tuning pipeline.  
- 11 Nov–05 Dec: Build evaluation engine, integrate guardrails, run initial experiments.  
- 06–20 Dec: Harden reporting, encryption, and documentation.  
- 21–28 Dec: Package alpha release, publish blog + demo video.

## 8. References

- Tinker fine-tuning best practices docs.  
- Relevant clinical NLP benchmarks (PubMedQA, BioASQ, ClinSum).  
- Regulatory guidance: HIPAA, FDA SaMD AI/ML framework.

## 9. Current Implementation Status (13 Oct 2025)

- ✅ Repository scaffolding in place (`src/bio_llm_eval/` package with config, training, evaluation modules).  
- ✅ Dry-run pipeline via CLI using sample PubMedQA slice; produces training/evaluation report JSON with auto GPU fallback and LoRA-ready training loop.  
- ✅ CLI supports changelog / lab report appends for automated logging post-run.  
- ✅ Pydantic-run configuration supports LoRA toggles and future non-dry-run execution.  
- 🔜 Execute LoRA/QLoRA fine-tuning on compliant datasets (post-approval) and benchmark against baselines.  
- 🔜 Expand evaluation beyond heuristics (toxicity, privacy, bias audits) with quantitative validators.

# PubMedQA Dataset Notes

**Dataset:** PubMedQA v1.0  
**Source:** [https://pubmedqa.github.io](https://pubmedqa.github.io)  
**License:** MIT License (retain attribution and license notice)  
**Compliance Checklist:** `docs/checklists/completed/pubmedqa.md`

## Overview

PubMedQA is a factoid question answering dataset built from PubMed abstracts. Each sample includes a yes/no/maybe answer derived from the abstract plus supporting context.

## Key Metadata

- **Task Type:** Biomedical QA (yes/no/maybe)  
- **Size:** ~1k labeled questions with context paragraphs  
- **Languages:** English  
- **Preprocessing:** Abstract extraction, question generation, label curation.

## Usage in Bio-LLM Evaluation Suite

- Evaluate factual accuracy for clinical QA prompts.  
- Serve as fine-tuning corpus for parameter-efficient adaptation (LoRA/QLoRA).  
- Provide baseline for hallucination probes comparing retrieval-augmented vs. vanilla LLM responses.

## Integration Checklist

- [ ] Download dataset and verify checksum (`data/provenance/pubmedqa.sha256`).  
- [ ] Store encrypted at rest (S3 bucket `bio-llm-datasets/pubmedqa`).  
- [ ] Enable bucket access logging and restrict IAM roles.  
- [ ] Run PHI/PII scan using tooling in `tools/compliance/phi_scan.py`.  
- [ ] Document any bias findings (English-only, publication skew) in risk log.  
- [ ] Log dataset usage in `logs/dataset-access/`.

## References

- Jin, Y. et al. “PubMedQA: A Dataset for Biomedical Research Question Answering.”  
- MIT License text (`LICENSES/pubmedqa_LICENSE` pending).

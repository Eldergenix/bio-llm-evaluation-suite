# BioLaySumm Dataset Notes

**Dataset:** BioLaySumm  
**Source:** [https://github.com/BioLaySumm/BioLaySumm](https://github.com/BioLaySumm/BioLaySumm)  
**License:** CC BY 4.0 (inherited from PLOS and eLife articles)  
**Compliance Checklist:** `docs/checklists/completed/biolaysumm.md`

## Overview

BioLaySumm contains pairs of original biomedical research articles and plain-language summaries. It supports tasks involving translation of technical findings into patient-friendly language.

## Key Metadata

- **Task Type:** Lay summarisation / knowledge translation.  
- **Size:** Hundreds of article-summary pairs (verify latest count).  
- **Languages:** English.  
- **Sources:** Open-access journals (PLOS, eLife); DOIs provided.

## Usage in Bio-LLM Evaluation Suite

- Assess models’ ability to generate layperson-friendly summaries while preserving clinical accuracy.  
- Measure factual drift between technical and simplified outputs.  
- Provide evaluation traces for transparency and risk communication.

## Integration Checklist

- [ ] Clone repository / download release and verify provenance (`data/provenance/biolaysumm_articles.csv`).  
- [ ] Store data with encryption and controlled access.  
- [ ] Execute PHI scan to confirm absence of identifiers.  
- [ ] Review bias (journal/source skew) and log mitigation strategies.  
- [ ] Subscribe to upstream repo releases for updates.  
- [ ] Ensure CC BY attribution in downstream outputs (include DOIs).

## References

- BioLaySumm Challenge overview paper.  
- PLOS and eLife open-access policies.  
- CC BY 4.0 license text.

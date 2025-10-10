# Dataset Compliance — BioLaySumm

**Dataset:** BioLaySumm (Biomedical Lay Summarization Corpus)  
**Source:** [BioLaySumm GitHub](https://github.com/BioLaySumm/BioLaySumm)  
**Primary Owners/Authors:** BioLaySumm challenge organisers; content from PLOS and eLife articles

| Item | Description | Dataset Owner | Status | Notes |
| --- | --- | --- | --- | --- |
| Licensing | Underlying PLOS and eLife articles released under CC BY 4.0. | PLOS / eLife | ☑ | Ensure attribution per publisher guidelines. |
| Redistribution | CC BY 4.0 allows redistribution with attribution. | PLOS / eLife | ☑ | Include CC BY notices and DOIs for each article. |
| PHI/PII | Academic publications; no PHI expected. | Publishers | ☑ | Spot check for accidental identifiers (e.g., case studies). |
| Data Use Agreements | No additional DUA; reuse governed by CC BY 4.0 terms. | N/A | ☑ | Document acceptance of license terms. |
| Security Controls | Store encrypted; restrict write access. | Internal Ops | ◐ | Align with shared dataset bucket policy. |
| Provenance | Track article DOIs and version numbers. | Publishers | ☑ | Maintain mapping file `data/provenance/biolaysumm_articles.csv`. |
| Bias Review | Content skew to open-access journals; evaluate representativeness. | Internal Research | ◐ | Log findings in risk register. |
| Ethical Review | Public scientific literature; IRB not required. | Internal Research | ☑ | Cite open-access status. |
| Regulatory Alignment | No PHI; general public content. | Compliance | ☑ | Note compliance with HIPAA due to absence of PHI. |
| Update Cadence | Monitor BioLaySumm repo for dataset updates. | Dataset authors | ☑ | Subscribe to release notifications. |
| Usage Logging | Log dataset access events. | Internal Ops | ◐ | Enable bucket logging & audit trail. |
| Data Retention | Retain until research complete; review annually. | Internal Ops | ◐ | Document retention policy. |
| Documentation | Repo includes README detailing dataset structure. | Dataset authors | ☑ | Mirror docs in `docs/datasets/biolaysumm.md`. |
| Consent | CC BY 4.0 covers reuse; no personal consent required. | Publishers | ☑ | Provide attribution per CC BY. |
| External Sharing | Share derivatives under CC BY 4.0 with citations. | Internal Ops | ☑ | Include original article DOIs in outputs. |

## Approval Sign-off

- **Reviewed By:** Nexis (AI Compliance Lead)  
- **Date:** 2025-10-10  
- **Comments:** Bias assessment pending; track on project board.

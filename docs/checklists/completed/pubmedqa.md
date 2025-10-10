# Dataset Compliance — PubMedQA

**Dataset:** PubMedQA v1.0  
**Source:** [pubmedqa.github.io](https://pubmedqa.github.io)  
**Primary Owners/Authors:** Yifan Jin et al., National Library of Medicine abstracts

| Item | Description | Dataset Owner | Status | Notes |
| --- | --- | --- | --- | --- |
| Licensing | MIT License permits research and derivative works. | PubMedQA authors | ☑ | MIT license stated on official site. |
| Redistribution | Redistribution allowed under MIT; retain license notice. | PubMedQA authors | ☑ | Host access instructions in repo; mirror hash in internal storage. |
| PHI/PII | Abstracts sourced from PubMed (public, non-PHI). | NLM | ☑ | No patient identifiers; still review for incidental identifiers. |
| Data Use Agreements | No DUA required beyond MIT terms. | N/A | ☑ | Documented in access notes. |
| Security Controls | Store encrypted at rest with restricted IAM role. | Internal Ops | ◐ | Provision S3 bucket `bio-llm-datasets/pubmedqa` with KMS encryption. |
| Provenance | Verify checksums after download. | PubMedQA authors | ☑ | Record SHA256 in `data/provenance/pubmedqa.sha256`. |
| Bias Review | Clinical literature skewed toward English-language trials. | Internal Research | ◐ | Note in risk log; explore balancing with multilingual sources. |
| Ethical Review | Not human-subject data; IRB not required. | Internal Research | ☑ | Documented rationale. |
| Regulatory Alignment | No PHI; compliant with HIPAA Safe Harbor. | Compliance | ☑ | Maintain audit trail for dataset sourcing. |
| Update Cadence | Dataset static; monitor upstream announcements. | PubMedQA authors | ☑ | Schedule quarterly check. |
| Usage Logging | Enable access logging on storage bucket. | Internal Ops | ◐ | Add CloudTrail policy + retention 1 year. |
| Data Retention | Retain until project sunset or license change. | Internal Ops | ◐ | Define deletion workflow in infra runbook. |
| Documentation | README includes schema and preprocessing steps. | PubMedQA authors | ☑ | Mirror metadata in `docs/datasets/pubmedqa.md`. |
| Consent | Content public; no individual consent required. | N/A | ☑ | Citations adhere to license terms. |
| External Sharing | Share derived models with attribution per MIT license. | Internal Ops | ☑ | Include license copy in releases. |

## Approval Sign-off

- **Reviewed By:** Nexis (AI Compliance Lead)  
- **Date:** 2025-10-10  
- **Comments:** Bucket hardening + bias mitigation tasks tracked on project board.

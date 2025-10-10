# Dataset Compliance — MultiClinSum

**Dataset:** MultiClinSum (Multi-document Clinical Summarization)  
**Source:** [Zenodo DOI: 10.5281/zenodo.10454805](https://zenodo.org/records/10454805)  
**Primary Owners/Authors:** University of Waterloo, Vector Institute collaborators

| Item | Description | Dataset Owner | Status | Notes |
| --- | --- | --- | --- | --- |
| Licensing | CC BY 4.0 permits redistribution with attribution. | Dataset authors | ☑ | Include attribution statement in documentation. |
| Redistribution | Allowed under CC BY 4.0; maintain DOI reference. | Dataset authors | ☑ | Mirror in internal bucket with README copy. |
| PHI/PII | Source notes state clinical texts are de-identified. | Dataset authors | ◐ | Perform automated PHI scan to confirm; log results. |
| Data Use Agreements | No additional DUA beyond CC BY 4.0. | N/A | ☑ | Keep DOI receipt. |
| Security Controls | Store in encrypted bucket with restricted IAM. | Internal Ops | ◐ | Same bucket policy as PubMedQA; confirm access roles. |
| Provenance | Download via DOI; record checksum. | Dataset authors | ☑ | Save SHA256 in `data/provenance/multiclinsum.sha256`. |
| Bias Review | Dataset derived from specific hospital systems; possible demographic skew. | Internal Research | ◐ | Document known biases; cross-check with metadata when available. |
| Ethical Review | IRB approval not required (de-identified). | Internal Research | ☑ | Keep authors’ de-identification statement. |
| Regulatory Alignment | De-identified data; ensure compliance with HIPAA Safe Harbor. | Compliance | ◐ | Validate against PHI scan results. |
| Update Cadence | Track Zenodo record for new versions. | Dataset authors | ☑ | Subscribe to DOI updates. |
| Usage Logging | Log data access via storage bucket. | Internal Ops | ◐ | Enable bucket logging; retention 1 year. |
| Data Retention | Retain until evaluation complete; review annually. | Internal Ops | ◐ | Add to retention policy doc. |
| Documentation | Zenodo record includes metadata and README. | Dataset authors | ☑ | Mirror documentation in `docs/datasets/multiclinsum.md`. |
| Consent | Dataset uses de-identified clinical notes; consent addressed by authors. | Dataset authors | ☑ | Cite author statement. |
| External Sharing | Share derived artefacts with CC BY attribution. | Internal Ops | ☑ | Include attribution in release notes. |

## Approval Sign-off

- **Reviewed By:** Nexis (AI Compliance Lead)  
- **Date:** 2025-10-10  
- **Comments:** PHI scan + IAM policy updates tracked on project board.

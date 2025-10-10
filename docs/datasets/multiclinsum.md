# MultiClinSum Dataset Notes

**Dataset:** MultiClinSum  
**Source:** [Zenodo DOI 10.5281/zenodo.10454805](https://zenodo.org/records/10454805)  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
**Compliance Checklist:** `docs/checklists/completed/multiclinsum.md`

## Overview

MultiClinSum provides de-identified clinical notes paired with human-written multi-document summaries, targeting clinical summarisation and reporting research.

## Key Metadata

- **Task Type:** Clinical document summarisation (multi-source).  
- **Size:** ~20k summaries (verify after download).  
- **Languages:** English.  
- **Preprocessing:** De-identification performed by dataset authors; maintainers supply metadata and formatting notes.

## Usage in Bio-LLM Evaluation Suite

- Evaluate summarisation quality, factual consistency, and readability of fine-tuned models.  
- Benchmark guardrail effectiveness for hallucination and privacy leakage.  
- Provide dataset for reflection logging in Cognitive Kernel-Pro integration.

## Integration Checklist

- [ ] Download from Zenodo and verify checksum (`data/provenance/multiclinsum.sha256`).  
- [ ] Store encrypted at rest with restricted IAM roles.  
- [ ] Execute PHI scan (`tools/compliance/phi_scan.py`) and archive results.  
- [ ] Document demographic/clinical coverage biases in risk register.  
- [ ] Set up quarterly version checks on Zenodo record.  
- [ ] Include CC BY 4.0 attribution in downstream publications/releases.

## References

- Dataset announcement (Vector Institute, University of Waterloo).  
- CC BY 4.0 license text (`LICENSES/CC-BY-4.0.txt`).  
- Authors’ de-identification methodology (appendix in dataset readme).

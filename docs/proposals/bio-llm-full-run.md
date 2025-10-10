# Bio-LLM Fine-Tuning Execution Plan (v0.1)

**Date:** 2025-10-10  
**Owner:** @nexisdev  
**Target Window:** 2025-10-27 → 2025-11-08

## Objective

Execute the first full LoRA fine-tune of the Bio-LLM Evaluation Suite on approved datasets (PubMedQA, MultiClinSum) to produce reproducible metrics for hiring portfolios and community outreach.

## Resource Requirements

| Resource | Details | Owner | Status |
| --- | --- | --- | --- |
| GPU Instances | 2× A100 40GB on AWS (g5.12xlarge) for 10 days ≈ 480 GPU-hours | Infra | Pending budget approval |
| Storage | 500 GB S3 bucket (`s3://bio-llm-checkpoints`) encrypted + access logs | Infra | Pending |
| CI | Optional runner with GPU (self-hosted) for smoke tests | DevOps | Researching |

### Budget Estimate

| Item | Rate | Quantity | Cost |
| --- | --- | --- | --- |
| AWS g5.12xlarge (A100 40GB) | ~$5.20 / GPU-hour | 480 GPU-hours | **$2,496** |
| EBS storage (1 TB gp3) | ~$0.08 / GB-month | 0.5 TB for 1 month | **$40** |
| S3 storage + transfer | ~$0.023 / GB-month + minimal egress | 0.5 TB | **$12** |
| Contingency (10%) | — | — | **$255** |

**Total Estimated Budget:** **$2,800** (rounded). Approve spend before Oct 15 to secure GPU capacity.

## Compliance & Data Steps

1. Complete dataset compliance checklists for PubMedQA and MultiClinSum (already drafted).  
2. Run PHI scans (`tools/compliance/phi_scan.py`) on full datasets; archive reports in `reports/phi/`.  
3. Secure IAM roles for access to datasets + S3 bucket with least privilege.  
4. Update risk register with bias mitigation notes (English-only, demographic skew).  
5. Obtain internal approval (if required) for handling de-identified clinical summaries.

## Execution Timeline

| Date | Task | Owner |
| --- | --- | --- |
| Oct 13–15 | Finalise resource approvals, set up AWS infrastructure, configure secrets | Infra/DevOps |
| Oct 16–18 | Pull datasets into secure bucket, run PHI scans, update compliance docs | Data Ops |
| Oct 19–22 | Dry-run with `dry_run=false` on sampled subset (1 epoch) for integration test | Engineering |
| Oct 23–27 | Full training (3 epochs), checkpoint + metrics each epoch, capture evaluation outputs | Engineering |
| Oct 28 | Summarise results (accuracy, toxicity, hallucination metrics) and append to changelog/lab report | Research |

## Success Criteria

- >=3% accuracy improvement vs. baseline on PubMedQA and MultiClinSum.
- Toxicity and privacy heuristic rates ≤ 1%.
- All artefacts (reports, metrics, notebooks) stored in reproducible locations with README pointers.
- Outreach emails sent with results to Galaxy, MAIA, Cognitive Kernel-Pro maintainers.

## Risks & Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| GPU quota delays | Timeline slip | Pre-request quota increase; identify alternative clouds |
| Dataset compliance blockers | Unable to train | Coordinate with compliance early; keep dry-run ready |
| Model instability | Poor metrics | Use gradient accumulation & early stopping; monitor logs |

## Follow-up

- Draft blog post summarising findings (see `communications/blogs/bio-llm-first-run.md`).
- Record demo video of evaluation dashboards and reporting workflow.
- Update project board cards and changelog using CLI append flag.

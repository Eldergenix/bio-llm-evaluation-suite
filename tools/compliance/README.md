# Compliance Tooling

This directory houses lightweight scripts that support HIPAA-aligned dataset onboarding for the Bio-LLM Evaluation Suite.

## `phi_scan.py`

Heuristic scanner for detecting potential PHI/PII artefacts in plaintext datasets.

### Usage

```bash
python tools/compliance/phi_scan.py \
  --input data/raw/pubmedqa.jsonl \
  --report reports/phi/pubmedqa.json
```

The script reports:
- `summary`: count of pattern matches by type (email, phone, dates, etc.).
- `samples`: up to five example matches per pattern for manual review.

### Workflow Integration

1. Export dataset samples to a text-friendly format (JSONL/CSV/TXT).
2. Run the scanner and archive the JSON report in `reports/phi/`.
3. Update the associated dataset checklist with findings and mitigation steps.
4. If any PHI is detected, halt ingestion and coordinate remediation before proceeding.

### Extending Patterns

Update the `PHI_PATTERNS` dictionary to include domain-specific identifiers (e.g., hospital-specific MRN formats).

## Logging Access

- Record dataset pulls in `logs/dataset-access/` with timestamp, user, dataset, and purpose.
- Example entry (CSV):
  ```
  timestamp,dataset,user,action
  2025-10-12T14:00:00Z,PubMedQA,nexisdev,downloaded
  ```

## TODO

- Integrate with cloud bucket logging once infrastructure is provisioned.
- Add automated bias analysis notebook templates.

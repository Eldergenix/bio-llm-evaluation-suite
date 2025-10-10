# Dataset Access Logs

Maintain CSV (or JSON) records of dataset access events to support compliance audits.

## Suggested Schema

| Field | Description |
| --- | --- |
| timestamp | ISO 8601 timestamp (UTC) of the event |
| dataset | Dataset name (e.g., PubMedQA) |
| user | GitHub handle or system account |
| action | `downloaded`, `ingested`, `deleted`, etc. |
| location | Storage bucket/path (optional) |
| notes | Additional context (ticket ID, purpose) |

## Example

```
timestamp,dataset,user,action,location,notes
2025-10-12T14:00:00Z,PubMedQA,nexisdev,downloaded,s3://bio-llm-datasets/pubmedqa,Initial ingestion for evaluation
```

Update this log whenever data is accessed manually until automated logging is integrated with cloud storage providers.

"""
phi_scan.py
-----------
Lightweight PHI/PII heuristic scanner to support dataset onboarding for the
Bio-LLM Evaluation Suite. This is not a substitute for commercial HIPAA
compliance tooling but provides a reproducible first-pass screen.

Usage:
    python phi_scan.py --input data/raw/pubmedqa.jsonl --report reports/phi/pubmedqa.json

Recommended workflow:
    1. Extract dataset samples to a local file (JSONL, CSV, TXT).
    2. Run the scanner and review the generated report.
    3. Record findings in the dataset compliance checklist.
    4. Escalate any flagged entries for manual review or redaction.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable, List, Tuple

PHI_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", re.IGNORECASE),
    "phone": re.compile(r"\b(\+?\d{1,2}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "mrn": re.compile(r"\bMRN[:\s]*\d+\b", re.IGNORECASE),
    "date": re.compile(r"\b(?:19|20)\d{2}[-/]\d{1,2}[-/]\d{1,2}\b"),
    "name": re.compile(r"\b(?:Dr\.|Mr\.|Mrs\.|Ms\.|Patient)\s+[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\b"),
    "zip": re.compile(r"\b\d{5}(?:-\d{4})?\b"),
}


def read_lines(path: Path) -> Iterable[str]:
    """Yield textual lines from JSONL, TXT, or CSV files."""
    suffix = path.suffix.lower()
    if suffix in {".jsonl", ".json"}:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                    yield json.dumps(record, ensure_ascii=False)
                except json.JSONDecodeError:
                    yield line
    else:
        with path.open("r", encoding="utf-8") as f:
            yield from f


def scan_text(text: str) -> List[Tuple[str, str]]:
    """Return list of (pattern_name, match) for PHI patterns detected."""
    matches: List[Tuple[str, str]] = []
    for label, pattern in PHI_PATTERNS.items():
        for m in pattern.findall(text):
            snippet = m if isinstance(m, str) else " ".join(m)
            matches.append((label, snippet.strip()))
    return matches


def scan_file(path: Path) -> dict:
    """Run PHI scans across a file and return summary + sample matches."""
    summary_counter: Counter[str] = Counter()
    sample_matches: dict[str, List[str]] = {label: [] for label in PHI_PATTERNS}

    for idx, line in enumerate(read_lines(path), start=1):
        line_matches = scan_text(line)
        for label, snippet in line_matches:
            summary_counter[label] += 1
            if len(sample_matches[label]) < 5:
                sample_matches[label].append(f"Line {idx}: {snippet}")

    return {
        "file": str(path),
        "total_lines": idx if "idx" in locals() else 0,
        "summary": summary_counter,
        "samples": sample_matches,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Heuristic PHI/PII scanner.")
    parser.add_argument("--input", required=True, type=Path, help="Path to dataset file (jsonl/csv/txt).")
    parser.add_argument("--report", required=True, type=Path, help="Destination report path (.json).")
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    report = scan_file(args.input)
    args.report.parent.mkdir(parents=True, exist_ok=True)

    with args.report.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "file": report["file"],
                "total_lines": report["total_lines"],
                "summary": report["summary"],
                "samples": report["samples"],
            },
            f,
            indent=2,
        )

    print(f"[phi-scan] Completed. Summary: {report['summary']}")
    print(f"[phi-scan] Report written to {args.report}")


if __name__ == "__main__":
    main()

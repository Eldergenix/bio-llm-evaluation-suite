"""
Dataset loading utilities for the Bio-LLM Evaluation Suite.

For v0.1 the focus is PubMedQA (QA) with extension hooks for MultiClinSum
and BioLaySumm in later iterations.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, List, Mapping, Sequence

import json


@dataclass
class QAExample:
    question: str
    context: str
    answer: str


def load_pubmedqa(path: Path) -> Sequence[QAExample]:
    """
    Load PubMedQA formatted as JSONL.

    Each line should contain `question`, `context`, and `final_decision`.
    """
    examples: List[QAExample] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            examples.append(
                QAExample(
                    question=record.get("question", ""),
                    context=record.get("context", ""),
                    answer=record.get("final_decision", ""),
                )
            )
    return examples


def split_dataset(
    examples: Sequence[QAExample],
    train_ratio: float = 0.8,
    val_ratio: float = 0.1,
    max_samples: int | None = None,
) -> Mapping[str, Sequence[QAExample]]:
    """
    Simple deterministic split (will be replaced with stratified sampling later).
    Optionally limit to `max_samples` to speed up experimentation.
    """
    if max_samples:
        examples = list(islice(examples, max_samples))
    total = len(examples)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)
    return {
        "train": examples[:train_end],
        "val": examples[train_end:val_end],
        "test": examples[val_end:],
    }

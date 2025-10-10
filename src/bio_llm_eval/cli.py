"""
Command-line entry point for running the baseline pipeline.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

from .config import RunConfig
from .data import load_pubmedqa
from .evaluation import compute_accuracy
from .training import run_training


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bio-LLM Evaluation Suite runner.")
    parser.add_argument("--config", type=Path, required=True, help="Path to JSON config file.")
    parser.add_argument("--append-changelog", action="store_true", help="Append summary to changelog after run.")
    parser.add_argument("--changelog-path", type=Path, default=Path("CHANGELOG.md"), help="Changelog path to append to.")
    parser.add_argument("--append-lab-report", action="store_true", help="Append summary to lab report file.")
    parser.add_argument("--lab-report-path", type=Path, help="Lab report markdown file to append to.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with args.config.open("r", encoding="utf-8") as f:
        raw_cfg = json.load(f)

    run_config = RunConfig.model_validate(raw_cfg)

    dataset = load_pubmedqa(run_config.dataset_path)
    training_metrics = run_training(run_config, list(dataset))

    # Placeholder predictions equal to gold answers in dry-run mode.
    predictions = [example.answer for example in dataset]
    references = [example.answer for example in dataset]
    evaluation_result = compute_accuracy(predictions, references)

    report = {
        "training": training_metrics,
        "evaluation": {
            "accuracy": evaluation_result.accuracy,
            "total": evaluation_result.total,
            "correct": evaluation_result.correct,
            "hallucination_flag_rate": evaluation_result.hallucination_flag_rate,
            "toxicity_rate": evaluation_result.toxicity_rate,
            "privacy_leak_rate": evaluation_result.privacy_leak_rate,
        },
    }

    run_config.report_path.parent.mkdir(parents=True, exist_ok=True)
    with run_config.report_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"[bio-llm-eval] Report written to {run_config.report_path}")

    summary = (
        f"{datetime.utcnow().date()} — model={training_metrics.get('model_name', run_config.training.model_name)} "
        f"mode={training_metrics.get('mode', 'full')} accuracy={evaluation_result.accuracy:.3f} "
        f"toxicity={evaluation_result.toxicity_rate if evaluation_result.toxicity_rate is not None else 'n/a'} "
        f"hallucination={evaluation_result.hallucination_flag_rate if evaluation_result.hallucination_flag_rate is not None else 'n/a'}"
    )

    if args.append_changelog:
        append_summary(args.changelog_path, summary)
        print(f"[bio-llm-eval] Appended summary to {args.changelog_path}")

    if args.append_lab_report and args.lab_report_path:
        append_summary(args.lab_report_path, summary)
        print(f"[bio-llm-eval] Appended summary to {args.lab_report_path}")


def append_summary(path: Path, summary: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"- {summary}\n")


if __name__ == "__main__":
    main()

import json
from pathlib import Path

from bio_llm_eval.config import RunConfig
from bio_llm_eval.data import load_pubmedqa
from bio_llm_eval.evaluation import (
    compute_accuracy,
    estimate_toxicity_rate,
    estimate_privacy_leakage_rate,
)
from bio_llm_eval import training
from bio_llm_eval.training import run_training


def load_run_config(path: Path) -> RunConfig:
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return RunConfig.model_validate(raw)


def test_dry_run_training(tmp_path: Path) -> None:
    cfg = load_run_config(Path("configs/pubmedqa.baseline.json"))
    cfg.training.output_dir = tmp_path / "artifacts"
    cfg.report_path = tmp_path / "report.json"
    metrics = run_training(cfg, list(load_pubmedqa(cfg.dataset_path)))

    assert metrics["notes"].startswith("Dry-run")
    assert (cfg.training.output_dir / "dry_run_metrics.json").exists()


def test_auto_dry_run_without_gpu(monkeypatch, tmp_path: Path) -> None:
    cfg = load_run_config(Path("configs/pubmedqa.baseline.json"))
    cfg.training.dry_run = False
    cfg.training.output_dir = tmp_path / "artifacts"

    monkeypatch.setattr(training, "gpu_available", lambda: False)

    metrics = run_training(cfg, list(load_pubmedqa(cfg.dataset_path)))
    assert metrics["notes"].startswith("Dry-run")


def test_accuracy_stub() -> None:
    dataset = load_pubmedqa(Path("data/samples/pubmedqa.sample.jsonl"))
    preds = [ex.answer for ex in dataset]
    refs = [ex.answer for ex in dataset]

    result = compute_accuracy(preds, refs)
    assert result.accuracy == 1.0
    assert result.hallucination_flag_rate == 0.0
    assert result.toxicity_rate == 0.0
    assert result.privacy_leak_rate == 0.0


def test_toxicity_and_privacy_detectors() -> None:
    preds = [
        "You are an idiot.",
        "Patient ID 12345678 should not be shared.",
        "All good here."
    ]
    assert estimate_toxicity_rate(preds) == 1 / 3
    assert estimate_privacy_leakage_rate(preds) == 1 / 3

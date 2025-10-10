"""
Configuration models for the Bio-LLM Evaluation Suite.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class LoRAConfig(BaseModel):
    enable: bool = Field(default=False, description="Whether to apply LoRA adapters.")
    r: int = Field(default=8, description="Rank of LoRA matrices.")
    alpha: int = Field(default=16, description="LoRA alpha.")
    dropout: float = Field(default=0.05, description="LoRA dropout probability.")
    target_modules: Optional[list[str]] = Field(default=None, description="Target modules for LoRA.")


class TrainingConfig(BaseModel):
    model_name: str = Field(..., description="Base Hugging Face model identifier.")
    learning_rate: float = Field(default=5e-5, gt=0)
    epochs: int = Field(default=1, ge=1)
    output_dir: Path = Field(default=Path("artifacts"))
    max_train_samples: Optional[int] = Field(default=128, ge=1)
    batch_size: int = Field(default=2, ge=1)
    gradient_accumulation_steps: int = Field(default=1, ge=1)
    seed: int = Field(default=42)
    lora: LoRAConfig = Field(default_factory=LoRAConfig)
    dry_run: bool = Field(default=True, description="If true, skip heavy model downloads and emit placeholder metrics.")

    @field_validator("output_dir", mode="before")
    def _coerce_output_dir(cls, value: str | Path) -> Path:
        return Path(value)


class RunConfig(BaseModel):
    training: TrainingConfig
    dataset_path: Path = Field(..., description="Path to PubMedQA JSONL dataset.")
    report_path: Path = Field(default=Path("reports/baseline.json"))

    @field_validator("dataset_path", "report_path", mode="before")
    def _coerce_paths(cls, value: str | Path) -> Path:
        return Path(value)

"""
Training utilities for Bio-LLM Evaluation Suite.
"""

from __future__ import annotations

import json
import random

import numpy as np
import torch
from torch.utils.data import DataLoader
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import Accelerator

from .config import RunConfig, TrainingConfig
from .data import QAExample, split_dataset


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def prepare_dataset(examples: list[QAExample], tokenizer: AutoTokenizer, max_length: int = 512) -> list[dict[str, torch.Tensor]]:
    prompts = [
        f"Question: {ex.question}\nContext: {ex.context}\nAnswer:"
        for ex in examples
    ]
    answers = [ex.answer for ex in examples]
    tokenized = tokenizer(
        prompts,
        truncation=True,
        max_length=max_length,
        padding="max_length",
        return_tensors="pt",
    )
    labels = tokenizer(
        answers,
        truncation=True,
        max_length=8,
        padding="max_length",
        return_tensors="pt",
    )["input_ids"]

    items: list[dict[str, torch.Tensor]] = []
    for idx in range(tokenized["input_ids"].shape[0]):
        item = {k: v[idx] for k, v in tokenized.items()}
        item["labels"] = labels[idx]
        items.append(item)
    return items


def collate_batch(batch: list[dict[str, torch.Tensor]]) -> dict[str, torch.Tensor]:
    collated: dict[str, torch.Tensor] = {}
    for key in batch[0].keys():
        collated[key] = torch.stack([example[key] for example in batch])
    return collated


def create_model(config: TrainingConfig) -> AutoModelForCausalLM:
    model = AutoModelForCausalLM.from_pretrained(config.model_name)
    if config.lora.enable:
        target_modules = config.lora.target_modules
        lora_cfg = LoraConfig(
            r=config.lora.r,
            lora_alpha=config.lora.alpha,
            lora_dropout=config.lora.dropout,
            target_modules=target_modules,
            task_type="CAUSAL_LM",
        )
        model = get_peft_model(model, lora_cfg)
    return model


def gpu_available() -> bool:
    return torch.cuda.is_available()


def run_training(run_config: RunConfig, examples: list[QAExample]) -> dict:
    training_config = run_config.training
    training_config.output_dir.mkdir(parents=True, exist_ok=True)
    seed_everything(training_config.seed)

    gpu_ready = gpu_available()
    auto_dry_run = training_config.dry_run or not gpu_ready

    if not gpu_ready and not training_config.dry_run:
        print("[bio-llm-eval] GPU not detected; falling back to dry-run mode.")

    if auto_dry_run:
        # Emit placeholder metrics without loading heavy models.
        metrics = {
            "model_name": training_config.model_name,
            "epochs": training_config.epochs,
            "learning_rate": training_config.learning_rate,
            "max_train_samples": training_config.max_train_samples,
            "lora_enabled": training_config.lora.enable,
            "mode": "dry_run"
            if training_config.dry_run
            else "dry_run_auto",
            "notes": "Dry-run mode enabled automatically." if not training_config.dry_run else "Dry-run mode enabled by config.",
        }
        with (training_config.output_dir / "dry_run_metrics.json").open("w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2)
        return metrics

    tokenizer = AutoTokenizer.from_pretrained(training_config.model_name, use_fast=True)
    dataset_splits = split_dataset(
        examples,
        max_samples=training_config.max_train_samples,
    )

    train_dataset = prepare_dataset(list(dataset_splits["train"]), tokenizer)

    accelerator = Accelerator()
    device = accelerator.device

    model = create_model(training_config)
    model = accelerator.prepare(model)
    model.train()

    optimizer = torch.optim.AdamW(model.parameters(), lr=training_config.learning_rate)
    optimizer = accelerator.prepare(optimizer)

    train_loader = DataLoader(
        train_dataset,
        batch_size=training_config.batch_size,
        shuffle=True,
        collate_fn=collate_batch,
    )
    train_loader = accelerator.prepare(train_loader)

    losses: list[float] = []
    grad_accum = training_config.gradient_accumulation_steps

    for epoch in range(training_config.epochs):
        epoch_loss = 0.0
        for step, batch in enumerate(train_loader):
            labels = batch.pop("labels").to(device)
            inputs = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**inputs, labels=labels)
            loss = outputs.loss / grad_accum
            accelerator.backward(loss)

            if (step + 1) % grad_accum == 0:
                optimizer.step()
                optimizer.zero_grad()

            epoch_loss += loss.item() * grad_accum
        epoch_avg = epoch_loss / max(len(train_loader), 1)
        losses.append(epoch_avg)

    avg_loss = float(np.mean(losses)) if losses else 0.0
    perplexity = float(np.exp(avg_loss)) if avg_loss else float("inf")

    metrics = {
        "model_name": training_config.model_name,
        "training_loss": avg_loss,
        "perplexity": perplexity,
        "epochs": training_config.epochs,
        "learning_rate": training_config.learning_rate,
        "lora_enabled": training_config.lora.enable,
        "mode": "full",
    }
    with (training_config.output_dir / "metrics.json").open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    return metrics

# Contributing Guide

## Environment Setup

1. Ensure Python 3.9+ is installed.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies in editable mode:
   ```bash
   pip install --upgrade pip
   pip install -e .[dev]
   ```
   Alternatively, run `make install` (creates `.venv` automatically).

## Running Tests

```bash
pytest
```
Or use `make test` for convenience.

## Formatting & Linting

```bash
ruff check src tests
black src tests
```
The CI workflow (`.github/workflows/ci.yml`) enforces lint + tests on push/PR.

## Running the Baseline Pipeline

```bash
python -m bio_llm_eval.cli --config configs/pubmedqa.baseline.json --report reports/baseline.json
```

The baseline currently logs configuration metadata; integrate LoRA/QLoRA fine-tuning following `docs/issues/bio-llm-baseline-pipeline.md`.

## Submitting Changes

- Update relevant documentation (design docs, changelog, TODO progress log).
- Ensure compliance artefacts are stored under `docs/checklists/` and `reports/phi/` when working with datasets.
- Open a pull request referencing issue IDs from `docs/issues/`.

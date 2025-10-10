.PHONY: install lint format test run-sample

install:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -e '.[dev]'

lint:
	. .venv/bin/activate && ruff check src tests && black --check src tests

format:
	. .venv/bin/activate && black src tests

test:
	. .venv/bin/activate && pytest

run-sample:
	. .venv/bin/activate && python -m bio_llm_eval.cli --config configs/pubmedqa.baseline.json --report reports/pubmedqa-baseline.json

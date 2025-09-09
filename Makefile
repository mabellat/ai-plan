PY=python3

.PHONY: setup dev test format lint precommit

setup:
	$(PY) -m venv .venv
	. .venv/bin/activate && pip install -U pip wheel
	. .venv/bin/activate && pip install -r env/requirements.txt

dev: format lint precommit

format:
	. .venv/bin/activate && ruff format .

lint:
	. .venv/bin/activate && ruff check .
	. .venv/bin/activate && mypy --install-types --non-interactive code

precommit:
	. .venv/bin/activate && pre-commit run --all-files

test:
	. .venv/bin/activate && pytest -q

#!/usr/bin/env bash
set -euo pipefail
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip wheel
pip install -r env/requirements.txt
pre-commit install
echo "✅ Environment ready. Copy env/.env.example to .env and update secrets."

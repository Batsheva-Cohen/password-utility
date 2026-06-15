# Password Utility

![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)

## What this project does
Checks password strength and returns score, feedback and `is_strong`.

## Installation
```bash
git clone https://github.com/<user>/<repo>.git
cd <repo>
uv sync --dev

#Run
python main.py

#Test localy
uv run ruff check .
uv run ruff format --check .
uv run ty check
uv run pytest --cov --cov-fail-under=80



precommit:
	uv run pre-commit run --all-files
lint:
	uv run ruff format .
	uv run mypy .
run:
	uv run uvicorn app.main:app --reload

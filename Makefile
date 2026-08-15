precommit:
	uv run pre-commit run --all-files
lint:
	uv run ruff format .
	uv run mypy .

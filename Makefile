.PHONY: clean
clean:
	poetry run pyclean src/drive tests

.PHONY: install
install:
	poetry install --with dev --no-root

.PHONY: test
test:
	poetry run pytest tests

.PHONY: format
format:
	poetry run black src/drive tests

.PHONY: lint
lint:
	poetry run ruff check src/drive tests --fix

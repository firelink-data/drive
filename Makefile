.PHONY: clean
clean:
	poetry run pyclean src/drive tests

.PHONY: install
install:
	poetry install --with dev --no-root

.PHONY: test
test:
	poetry run pytest tests


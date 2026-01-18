lint:
	flake8 .
	black --check .

cleanup:
	black .
	isort .
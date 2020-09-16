build:
	poetry build -f wheel

patch:
	poetry version patch

letsgo: patch publish

format:
	pre-commit run --all-files

publish: format build
	poetry publish

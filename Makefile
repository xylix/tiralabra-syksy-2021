coverage-generate:
	python -m coverage run --source src/ -m pytest 
coverage-report: coverage-generate
	python -m coverage report -m
.PHONY: test
test:
	python -m pytest

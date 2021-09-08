coverage-generate:
	python -m coverage run --source src/ -m pytest 
coverage-report: coverage-generate
	python -m coverage report
coverage-file:
	python -m coverage report > current_coverage.txt
.PHONY: test
test:
	python -m pytest

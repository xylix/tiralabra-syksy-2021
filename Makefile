.PHONY: test format lint coverage-generate coverage-report coverage-file codestyle

coverage-generate:
	python -m coverage run --source src/ -m pytest 
coverage-report: coverage-generate
	python -m coverage report
coverage-file: coverage-generate
	python -m coverage report > current_coverage.txt
test:
	python -m pytest
test-with-benchmarks:
	python -m pytest --runslow
format:
	black src
	black test
lint:
	pylint src
	pylint test
codestyle: format lint

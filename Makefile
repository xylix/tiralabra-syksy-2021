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
	python -m pytest --runslow --capture=tee-sys
simple-benchmarks:
	fish -c 'simple_benchmarks.sh &> dokumentit/benchmark_history/(git rev-parse --short HEAD).txt'
format:
	black src
	black test
lint:
	pylint --fail-under=9 src
	pylint --fail-under=9 --disable=missing-function-docstring test
codestyle: format lint

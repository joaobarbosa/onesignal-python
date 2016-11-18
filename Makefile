.PHONY: clean
clean:
	rm -rf build/ dist/ docs/_build *.egg-info
	find $(CURDIR) -name "*.py[co]" -delete
	find $(CURDIR) -name "*.orig" -delete
	find $(CURDIR)/$(MODULE) -name "__pycache__" | xargs rm -rf

.PHONY: run_tests
run_tests:clean
	py.test --pep8 --cov=. --cov-report=term-missing --cov-config=.coveragerc -r a -v -s

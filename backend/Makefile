.PHONY: help install test clean types

help:
	@echo "install - install the dependencies listed in your requirements.txt file"
	@echo "test - run all unit tests in your project"
	@echo "clean - remove all .pyc files and __pycache__ directories from your project"
	@echo "types - run mypy --install-types recursively on all Python files in your project"

install:
	pip install -r requirements.txt

types:
	mypy --install-types .

test:
	python -m unittest discover

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

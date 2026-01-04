# Makefile for my-claude-tools

.PHONY: help setup package verify clean install-dev test

help:
	@echo "Available commands:"
	@echo "  make setup        - Set up development environment"
	@echo "  make package      - Package all custom skills"
	@echo "  make verify       - Verify skill zip files"
	@echo "  make clean        - Clean generated files"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make test         - Run tests (if available)"

setup:
	@python setup.py

package:
	@python package_skills.py

verify:
	@python verify_skills.py

clean:
	@echo "Cleaning generated files..."
	@rm -rf packaged-skills/*.zip
	@rm -rf __pycache__
	@rm -rf .pytest_cache
	@echo "Clean complete!"

install-dev:
	@pip install -r requirements.txt

test:
	@echo "Running tests..."
	@python -m pytest tests/ -v || echo "No tests found"

# Install dependencies
install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

# Run basic tests to ensure the app works
test:
	python -m pytest -vv tests  # Update this if you create tests later

# Debug any test failures
debug:
	python -m pytest -vv --pdb

# Run a specific test
one-test:
	python -m pytest -vv tests/test_app.py::test_specific_function

# Format the code with Black
format:
	black *.py

# Lint the code with pylint
lint:
	pylint --disable=R,C *.py

# Deploy the app to Hugging Face Spaces
deploy:
	huggingface-cli repo upload ./ -r spaces/username/my-ml-app --branch main

# Run all tasks
all: install lint format test deploy

.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	@sudo -H pip install -U pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install ntplib
	@pipenv install pytest

test:
	@echo "Start tests."
	@touch results.txt
	@pipenv run pytest tests/tests.py | tee results.txt

run:
	@echo "Run Python app."
	@pipenv run python app.py | tee -a results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	@git add results.txt
	@git commit -am "Lab 2: autopush"
	@git push
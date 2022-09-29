export PIPENV_IGNORE_VIRTUALENVS=1

lint:
	@pipenv run isort .
	@pipenv run black .
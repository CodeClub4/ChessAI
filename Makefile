SOURCE_PATH=.

black:
	black ${SOURCE_PATH}/

isort:
	isort ${SOURCE_PATH}/

reformat: black isort

install-hooks:
	pre-commit install

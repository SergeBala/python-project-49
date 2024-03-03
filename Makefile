install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

re:
	echo "\033[1;35m...Building and installing...\033[0m"
	make build
	make package-install

lint:
	poetry run flake8 brain_games

.PHONY : install brain-games build publish package-install lint re
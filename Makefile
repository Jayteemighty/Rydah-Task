COMPOSE_FILE=docker-compose.yml

docker-run:
	docker-compose -f ${COMPOSE_FILE} up -d

run-local:
	$(MAKE) docker-run
	sleep 2 # to allow complete setup of db
	pipenv run dev

migration:
	pipenv run makemigrations

migrate:
	pipenv run migrate

createsuperuser:
	pipenv run createsuperuser

static-test:
	pipenv run lint

test:
	$(MAKE) static-test
	pipenv run test
	pytest

quick-test:
	# Pass ISOLATED_TEST env var to run a single test f.e. tests/integration/test_auth.py::test_login
	pipenv run test ${ISOLATED_TEST}

auto-format:
	pipenv run isort-format
	pipenv run black-format
run:
	docker-compose up

setup: build dbsetup

build:
	docker-compose build

dbsetup:
	docker-compose run dbclient /bin/bash /setup/setup.sh

.PHONY: run setup build dbsetup

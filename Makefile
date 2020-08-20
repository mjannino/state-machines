DOC_TYPE=html
CMD=bash

build:
	docker-compose build state-machines

start:
	docker-compose up -d

stop:
	docker-compose down

app.shell:
	docker exec -it state-machines /bin/bash

rebuild-all:
	docker-compose down && docker-compose build && docker-compose up -d

clean:
	docker container prune -f && docker image prune -f
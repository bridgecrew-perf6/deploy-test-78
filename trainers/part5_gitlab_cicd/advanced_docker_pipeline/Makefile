.PHONY: build
build:
	docker build -t sunny_bikes .

.PHONY: run
run:
	docker run -p 8080:5000 --rm sunny_bikes

.PHONY: debug
debug:
	docker run -ti --rm --entrypoint /bin/bash sunny_bikes
.PHONY: build
build:
	docker build -t basph/sunnybikes .

.PHONY: run
run:
	docker run -p 8080:8080 -e FLASK_PORT=8080 -v $(pwd)/data.txt:/root/data/data.txt:ro -e DATA_PATH=/root/data/data.txt --rm basph/sunnybikes
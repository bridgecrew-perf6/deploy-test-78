.PHONY: build
build:
	docker build -t basph/sunnybikes .

.PHONY: run
run:
	docker run -p 8080:8080 -e FLASK_PORT=8080 -v $(shell pwd)/data.txt:/root/data/bike_rides.txt:ro -e DATA_PATH=/root/data/bike_rides.txt --rm basph/sunnybikes
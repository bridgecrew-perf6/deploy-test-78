# Part 4 docker-compose Demo

```bash
# build and run
docker compose up --build

# stop
docker compose stop

# stop and remove
docker compose down
```

## Translate from CLI to Compose

In `demo_simple`

Show shifting from these CLI commands:

```
docker build -t my-app .
docker run --rm -p 5000:5000 -n my-app my-app
```

To using docker-compose (explain each configuration)

```
version: "3.8"
services:
	app:
		build: .
		ports:
			- 5000:5000
```

Demonstrate
```
docker-compose up --build
docker-compose down
```

## Develop in your container

See the folder `demo_dev_in_container`.  The idea is to demonstrate using docker compose for your
local development via use of the mounting of the folder.

- Build and run:
    ```
    docker-compose up --build
    ```
- Open a separate terminal and use curl to get a response - `curl 0.0.0.0:5000`
- Now adjust the message in the app.py in your dev environment
- Show how the flask app has restarted and how it's now possible to see a new message
- Discuss how this can facilitate multiple developers having the same development environment



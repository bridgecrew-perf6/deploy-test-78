# Part 2 Docker CLI Demo

Note that there's a useful cheatsheet of Docker CLI commands in `participants`

## Tagging

To demonstrate tagging you can use:
```
docker tag busybox:latest bob/my_image:v1
```

## Push

1. Setup an account in DockerHub
2. Create a new repository
3. Tag a busybox image based on repo
    ```
    docker tag busybox:latest repo:tagname
    ```
4. Push to registry
    ```
    docker push repo:tagname
    ```
5. Demonstrate the image in the repo.


## Volumes

The following can be used to demonstrate volumes:
```
docker run --rm -ti -v vol_demo:/app busybox
```

One can then:
- create a file and add some text `vi bla.txt` in the app folder
- exit the container
- create a new container and demonstrate that file can still be found
- show that a volume has been created with `docker volume ls`
- inspect the volume with `docker volume inspect [name]`

## Bind mounts

To demonstrate bind mounts, in the same folder run:
```
docker run --rm -ti -v $(pwd):/app busybox
```

- show that app contains a file `some_text.txt`
- edit using `vi` and save
- close the container and demonstrate that `some_text.txt` on your local machine now retains the edits.

## Port mapping

This can be demonstrated using
```
docker run -p 8000:5000 training/webapp python app.py
```

- show how the logs indicate the endpoint is available at port 5000 in the container but that port 5000 is not reachable on the local machine
- show that port 8000 can be accessed

## Detached mode and logs

Demonstrate with:
```
docker run --name test -d busybox sh -c "while true; do $(echo date); sleep 1; done"
docker logs -f --until=2s test
```

- the container runs detached, you can demostrate it is running with `docker ps`
- the logs command outputs the logs
- this also indicates the use of `--name` for running the container
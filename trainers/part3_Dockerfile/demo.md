# Part 3 Dockerfile Demo

## Dockerfile start

An initial Dockerfile build can be run in `demo_docker_file`

```
docker build -t my_app .
```

## EXPOSE

To show how `EXPOSE` indicates the ports exposed, run `docker inspect IMAGE_NAME` 

## ENTRYPOINT & CMD

To show how `CMD` can be used to override, build the image in `demo_entrypoint` with
```
docker build -t myping .
```
Run a container
```
docker run --rm myping
```


Then demonstrate pinging a separate website by running:
```
docker run --rm myping www.facebook.com
```

## Linting

In the folder `demo_lint` run:
```
hadolint Baddockerfile
```

- Review the warnings that are shown and their meaning.  
- Explain the use of hadolint.yml
# Part 5 Gitlab CI/CD

The scale of what to demonstrate here can differ depending on what fits in the time
and the level of the participants.

## Simple pipeline

This can be used to demonstrate a simple pipeline that lints and builds the Dockerfile
and uploads the image to DockerHub

## Explaining Gitlab CICD flows

There are 2 pipelines defined in `pipelines.md` that can be used in Gitlab.

## More advanced configuration

A more advanced configuration can be seen in `part5_gitlab_cicd` which includes
- linting
- testing
- docker linting
- docker build and use of the Gitlab CR
- use of rules
- manual triggering
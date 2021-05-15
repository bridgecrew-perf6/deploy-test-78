# Some pipelines

To show how two jobs can run in parallel and different stages

```yml
build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
```

A more advanced setup to demonstrate:
- merge requests
- environment variables
- rules
- manual approval

```yaml
stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Hello, $GITLAB_USER_LOGIN!"

test-job1:
  stage: test
  script:
    - echo "This job tests something"
  rules:
    - if: $CI_MERGE_REQUEST_IID

test-job2:
  stage: test
  script:
    - echo "This job tests something, but takes more time than test-job1."
    - echo "After the echo commands complete, it runs the sleep command for 20 seconds"
    - echo "which simulates a test that runs 20 seconds longer than test-job1"
    - sleep 20
  rules:
    - if: '$CI_COMMIT_BRANCH == "master"'

deploy-staging:
  stage: deploy
  script:
    - echo "This job deploys to staging from the $CI_COMMIT_BRANCH branch"
  rules:
    - if: $CI_COMMIT_BRANCH == "master"

deploy-prod:
  stage: deploy
  script:
    - echo "This job deploys something from the $CI_COMMIT_BRANCH branch."
  rules:
    - if: $CI_COMMIT_BRANCH == "master"
      when: manual
    - when: never
```
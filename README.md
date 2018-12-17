# Docker training exercise code

The code in the repository is used during the Docker training. It contains both the exercises and solutions. Adapted from https://github.com/godatadriven/accelerator-docker-exercises with lessons learned from that training.

Associated Powerpoint: https://gdd.li/docker-training-presentation (note: ensure you're logged in otherwise you get a typical useless Microsoft error).

During the training we provide everybody a GCP project. The GCP Cloud Editor comes with Docker installed and works nicely for the training. Go to the [GCP training provisioning project](https://github.com/godatadriven/gcp-training-provisioning) and copy paste one of the previous `training-docker-*.settings` files. Set these variables:

1. project_id_prefix
2. project_name_prefix
3. emails (comma separated)

And run `./create_projects.sh training-docker-your-training.settings` to spin up a project for every participant.

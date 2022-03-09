# Docker training code

The code in the repository is used during the Docker training. It is split into 2 folders:
- `participants` - contains the exercise files that participants will need to complete as well 
as some handy cheatsheets with the commands shown in the slides
- `trainers` - contains the solutions to the exercises and some code that can be used to demonstrate
the principals in the slides

This material was originally adapted from https://github.com/godatadriven/accelerator-docker-exercises with lessons learned from that training.

Associated Powerpoint: https://gdd.li/docker-training-presentation (note: ensure you're logged in otherwise you get a typical useless Microsoft error).

## Setup!

Ideally participants are able to configure Docker on their development machines but this tends to go wrong on Windows machines
and it is recommended to get folk setup with [Google Cloud Platform](https://cloud.google.com/shell).  There are setup instructions for this in `participants/README.md`.  If this is a tool you'll be using it is recommended to run through the exercises in this editor
to ensure there are no surprises.

A further option is to provide participants with a GCP project. The GCP Cloud Editor comes with Docker installed and works nicely for the training. Go to the [GCP training provisioning project](https://github.com/godatadriven/gcp-training-provisioning) and copy paste one of the previous `training-docker-*.settings` files. Set these variables:

1. project_id_prefix
2. project_name_prefix
3. emails (comma separated)

And run `./create_projects.sh training-docker-your-training.settings` to spin up a project for every participant.

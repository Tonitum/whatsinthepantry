#!/bin/sh
export DOCKER_BUILDKIT=1

tag="${TAG:-dev}"

docker build -t backend:$tag .

#!/bin/sh
docker_options="-it" # Interactive/terminal
docker_options="$docker_options --rm" # remove container when stopped
docker_options="$docker_options --rm" #

docker run -it --rm -p 127.0.0.1:5000:5000 --name server backend:dev

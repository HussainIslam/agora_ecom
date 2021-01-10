#!/bin/bash

image_name=xx:agora_web_app
container_name=agora_container

echo "[ Message ] Stopping old container"
docker stop ${container_name}

# Build the image
echo "[ Message ] Building new image"
docker build -t ${image_name} --file Dockerfile . --quiet

echo "[ Message ] Removing old container"
docker rm -f ${container_name}

echo "[ Message ] Running container"
docker run --name ${container_name} -it -p 80:8888 -d ${image_name}
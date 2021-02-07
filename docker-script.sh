#!/bin/bash

image_name=agora_web_app
container_name=agora_container
environment_variables=`cat .env`

echo "[ Message ] Stopping old container"
docker stop ${container_name} > /dev/null

echo "[ Message ] Removing old container"
docker rm -f ${container_name} > /dev/null

# Creating build command
build_args=""

for var in ${environment_variables}
do
    build_args+=" --build-arg ${var}"
done

# Build the image
echo "[ Message ] Building new image"
docker build -t ${image_name} --file Dockerfile . --quiet ${build_args} --network host> /dev/null


echo "[ Message ] Running container"
docker run --name ${container_name} --network=host -it -d ${image_name}> /dev/null

docker ps --filter "name=${container_name}"
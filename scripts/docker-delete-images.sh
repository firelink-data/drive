#!/bin/bash

images=$(docker images -aq)

if [ ! -z "$images" ]; then
    docker rmi -f $images
else
    printf "No images to delete...\n"
fi


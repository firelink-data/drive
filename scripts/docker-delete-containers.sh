#!/bin/bash

containers=$(docker ps -aq)

if [ ! -z "$containers"]; then
    docker rm -vf $containers
else
    printf "No containers to delete...\n"
fi

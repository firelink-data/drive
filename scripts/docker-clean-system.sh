#!/bin/bash
docker system prune -a --volumes
./docker-delete-containers.sh
./docker-delete-images.sh

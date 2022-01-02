#!/bin/bash

echo "Deploy stage"

scp docker-compose.yaml jenkins@DeploymentServer:/home/jenkins/docker-compose.yaml 
ssh jenkins@DeploymentServer \
DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
DATABASE_URI=$DATABASE_URI \
docker stack deploy --compose-file docker-compose.yaml expense-tracker-app
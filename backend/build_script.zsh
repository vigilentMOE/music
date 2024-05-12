#!/bin/zsh

# Check if the correct number of arguments were provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <dockerhub-username> <image-name> <tag>"
    echo "Builds, tags, and pushes a Docker image to Docker Hub, then removes the local image."
    exit 1
fi

# Assign command line arguments to variables
USERNAME=$1
REPO_NAME=$2
TAG=$3

# Build and tag the Docker image
docker build -t $USERNAME/$REPO_NAME:$TAG .

# Push the Docker image to Docker Hub
docker push $USERNAME/$REPO_NAME:$TAG

# Remove the local Docker image
docker rmi $USERNAME/$REPO_NAME:$TAG

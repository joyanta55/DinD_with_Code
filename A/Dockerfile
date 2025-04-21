# Use the official Docker DinD image for Docker-in-Docker in A
FROM docker:19.03.12-dind

# Set the working directory (optional)
WORKDIR /app

# Install any necessary tools (optional)
RUN apk update && apk add --no-cache curl

# The entrypoint will start the Docker daemon inside Container A. dockerd-entrypoint.sh is the buit in sh file that 
ENTRYPOINT ["dockerd-entrypoint.sh"]

# Run Container B from D's Dockerfile and mount the Docker socket
CMD ["sh", "-c", "docker run --privileged --rm -v /var/run/docker.sock:/var/run/docker.sock --name dind-b-container dind-b-container"]


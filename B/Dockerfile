# Use the official Docker DinD image for Docker-in-Docker in B
FROM docker:19.03.12-dind

# Set the working directory
WORKDIR /app

# Install Python and other necessary tools
RUN apk update && apk add --no-cache python3 py3-pip curl

# The entrypoint will start the Docker daemon inside Container B. dockerd-entrypoint.sh is the default EntryPoint, you can change it.
ENTRYPOINT ["dockerd-entrypoint.sh"]

# Run Container C from B's Dockerfile.
CMD ["sh", "-c", "docker run --privileged --rm -e MY_VAR_B='Hello from B!' dind-c-container"]


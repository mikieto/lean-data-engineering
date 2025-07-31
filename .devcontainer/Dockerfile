# .devcontainer/Dockerfile

# Use a specific Python base image as a starting point.
FROM python:3.11-slim-bullseye

# Set environment variables for non-interactive apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Install common system tools and utilities in a single layer
# This prevents issues with outdated apt caches between RUN commands
# --no-install-recommends avoids installing unnecessary packages
RUN apt-get update \
    && apt-get -y install --no-install-recommends \
        git openssh-client curl unzip make gnupg sudo \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements-dev.txt first to leverage Docker caching
# This step only re-runs if requirements-dev.txt changes
COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install --no-cache-dir -r /tmp/requirements-dev.txt \
    && rm /tmp/requirements-dev.txt

# Install Terraform CLI
ARG TERRAFORM_VERSION="1.5.0"
RUN curl -LO "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" \
    && unzip "terraform_${TERRAFORM_VERSION}_linux_amd64.zip" -d /usr/local/bin \
    && rm "terraform_${TERRAFORM_VERSION}_linux_amd64.zip"

# Install AWS CLI v2
# Using an explicit version to ensure stability. AWS CLI v2 requires `groff` for man pages, but we can skip it.
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo ./aws/install

# Install tfsec for security checks
# Use --fail to ensure curl exits if the script download fails
# Use sh -c to allow piping to bash directly
RUN curl -sS https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash -s -- -b /usr/local/bin

# Create the vscode user and set up home directory
RUN groupadd -g 1000 vscode \
    && useradd -m -u 1000 -g vscode -s /bin/bash vscode

# Set the user and working directory
USER vscode
WORKDIR /workspaces/lean-data-engineering
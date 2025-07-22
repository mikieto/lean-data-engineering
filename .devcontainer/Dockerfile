# .devcontainer/Dockerfile

# Use a specific Python base image as a starting point.
FROM python:3.11-slim-bullseye

# Install common system tools and utilities needed for subsequent steps
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git openssh-client curl unzip make \  
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements-dev.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements-dev.txt && rm /tmp/requirements-dev.txt

# Install Terraform CLI (example, replace with actual version/download URL)
ARG TERRAFORM_VERSION="1.5.0"
RUN curl -LO "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" \
    && unzip "terraform_${TERRAFORM_VERSION}_linux_amd64.zip" -d /usr/local/bin \
    && rm "terraform_${TERRAFORM_VERSION}_linux_amd64.zip"

# Install AWS CLI (example)
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws

# Install tfsec for security checks
RUN curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash

RUN groupadd -g 1000 vscode \
  && useradd -m -u 1000 -g vscode vscode

USER vscode
WORKDIR /workspaces/jibun-os
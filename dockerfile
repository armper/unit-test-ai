# Use the official Jenkins LTS image as the base
FROM jenkins/jenkins:lts

# Switch to the root user to install packages
USER root

# Install Maven, Python, and Git
RUN apt-get update && \
    apt-get install -y maven python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*

# Optionally, install any Python packages you might need
RUN pip3 install requests

# Switch back to the Jenkins user
USER jenkins

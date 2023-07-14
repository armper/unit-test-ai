# Using official Jenkins image as a base
FROM jenkins/jenkins:lts

# Switching to root user to install Node.js
USER root

# Updating existing packages
RUN apt-get update && \
    apt-get upgrade -y

# Installing curl which will be used for installing Node.js
RUN apt-get install -y curl

# Installing Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Confirming Node.js and NPM are installed
RUN node -v
RUN npm -v

# Switching back to the Jenkins user
USER jenkins

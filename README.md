# Java Maven Project CI/CD Pipeline with Docker Support

This repository contains a Java Maven project that utilizes a Jenkins pipeline to automate various stages of the development lifecycle, including the generation of unit tests. Additionally, this project provides a `docker-compose.yml` and a `Dockerfile` to set up a Jenkins environment with all the necessary prerequisites.

## Pipeline Overview

1. **Clean Workspace and Checkout**: This stage cleans the Jenkins workspace and checks out the code from the feature branch.
2. **Clean Workspace**: This stage cleans the Maven build workspace.
3. **Analyze Changed Files**: This stage identifies the files that have changed between the previous commit and the current commit.
4. **Generate Unit Test**: A Python script (`generate_tests.py`) is executed to generate unit tests using OpenAI.
5. **Run Generated Unit Tests**: The generated unit tests are executed. If any test fails, the pipeline will mark this stage as 'UNSTABLE'.
6. **Fix Errors and Re-run Tests**: If the previous stage fails, this stage will be executed. A Python script (`fix_errors.py`) checks for errors, fixes them, and updates the test code. The tests are then re-run.
7. **Commit and Push Generated Test**: The path to the generated test file is read from `generated_test_path.txt`. The generated test is then committed and pushed to the `main` branch of the repository.

## Environment Variables

- `OPENAI_API_KEY`: This environment variable securely handles the OpenAI API key using Jenkins credentials.

## Prerequisites

- Jenkins with the necessary plugins installed.
- Python 3.x for executing the Python scripts.
- Git installed on the Jenkins agent.
- Maven installed on the Jenkins agent.

For those who prefer Docker, a `docker-compose.yml` and `Dockerfile` are provided to set up a Jenkins environment with all the prerequisites.

### Using Docker

1. Ensure Docker and Docker Compose are installed on your machine.
2. Navigate to the project directory.
3. Run `docker-compose up -d` to start the Jenkins service.
4. Access Jenkins by navigating to `http://localhost:8080` in your browser.

## Detecting Code Changes

To automatically trigger the Jenkins pipeline upon code changes, you need to set up a webhook in your version control system (e.g., GitHub, Bitbucket).

### For GitHub:

1. Go to your GitHub repository.
2. Click on `Settings` > `Webhooks`.
3. Click on `Add webhook`.
4. Set the `Payload URL` to `http://<JENKINS_URL>/github-webhook/`.
5. Choose content type as `application/json`.
6. Select the events you want to trigger the webhook, typically `Just the push event`.
7. Save the webhook.

### For Bitbucket:

1. Go to your Bitbucket repository.
2. Click on `Settings` > `Webhooks`.
3. Click on `Add webhook`.
4. Set the `URL` to `http://<JENKINS_URL>/bitbucket-hook/`.
5. Choose `Repository push` as the trigger.
6. Save the webhook.

Remember to replace `<JENKINS_URL>` with your actual Jenkins server URL.

## Security

Credentials such as the OpenAI API key and GitHub credentials are securely handled using Jenkins credentials binding.


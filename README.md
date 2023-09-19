# Java Maven Project CI/CD Pipeline

This repository contains a Java Maven project that utilizes a Jenkins pipeline to automate various stages of the development lifecycle, including the generation of unit tests.

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

## Usage

1. Ensure that the Jenkins agent has access to the repository and the necessary credentials.
2. Add the Jenkinsfile to your Jenkins job.
3. Run the Jenkins job to execute the pipeline.

## Security

Credentials such as the OpenAI API key and GitHub credentials are securely handled using Jenkins credentials binding.


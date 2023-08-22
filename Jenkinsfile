pipeline {
    agent any

    environment {
        OPENAI_API_KEY = credentials('openai-api-key') // Securely handle the OpenAI API key
    }

    stages {
        stage('Clean Workspace and Checkout') {
            steps {
                // Clean the Jenkins workspace
                deleteDir()
                echo 'Cleaned the Jenkins workspace.'

                // Checkout your code from the feature branch
                checkout scm
                echo 'Checked out the code.'
            }
        }

        stage('Clean Workspace') {
            steps {
                // Clean the Maven build
                sh 'mvn clean'
                echo 'Cleaned the Maven workspace.'
            }
        }

        stage('Analyze Changed Files') {
            steps {
                script {
                    // Get the list of changed files
                    sh 'git diff --name-only $GIT_PREVIOUS_COMMIT $GIT_COMMIT > changed_files.txt'
                    echo 'List of changed files:'
                    sh 'cat changed_files.txt'
                    // Run the Python script to analyze the changed files
                    sh 'python3 analyze_changes.py'
                }
            }
        }

        stage('Generate Unit Test') {
            steps {
                script {
                    // Call a Python script to generate unit tests through OpenAI
                    sh 'python3 generate_tests.py'
                    echo 'Generated unit tests.'
                }
            }
        }

        stage('Run Generated Unit Tests') {
            steps {
                // Commands to run the unit tests using your Java testing framework
                sh 'mvn test'
                echo 'Ran the generated unit tests.'
            }
        }

        stage('Fix Errors and Re-run Tests') {
            steps {
                script {
                    // Call the Python script to check for errors, fix them, and update the test code
                    sh 'python3 fix_errors.py'
                    echo 'Checked and fixed errors if any.'
                    // Re-run the tests with the fixed code
                    sh 'mvn test'
                }
            }
        }

        stage('Commit and Push Generated Test') {
            steps {
                script {
                    // Read the path from the file
                    def testFilePath = readFile('generated_test_path.txt').trim()
                    echo "Path to the generated test file: ${testFilePath}"

                    // Set Git user name and email
                    sh '''
            git config user.email "jenkins@example.com"
            git config user.name "Jenkins"
            '''

                    sh '''
            git add "${testFilePath}"
            git commit -m "Add or update generated unit test for feature XYZ"
            git push origin feature-branch-name
            '''
                    echo 'Committed and pushed the generated test.'
                }
            }
        }

    // Other stages (e.g., build and deploy) as needed
    }
}

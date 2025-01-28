pipeline {
    agent any  // Use any available agent

    environment {
        // Define environment variables if needed
        IMAGE_NAME = 'jenkins_test'
        IMAGE_TAG = '0.0.1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the Git repository
                git branch: 'master', url: 'https://github.com/iam-ruk/jenkins_pipeline'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the repo
                    sh "sudo docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container from the built image
                    sh "docker run -d ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished!'
        }
    }
}

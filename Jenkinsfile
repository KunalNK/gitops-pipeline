pipeline {
    agent {
        docker {
            image 'maven:3.8.1' // Docker image to be used as the execution environment
            args '-v /tmp:/tmp' // Additional arguments to pass to the Docker run command
        }
    }
    stages {
        // Clone the git repo
        stage('GitClone') {
            steps {
                sh "git clone https://github.com/KunalNK/gitops-pipeline.git"
            }
        }
        // Define your pipeline stages here
        stage('Build') {
            steps {
                // Perform the build steps
                sh "cd gitops-pipeline && docker build -t test:v1 ."
                sh "docker tag test-app:v2 kunalk07/gitops-flask:v1"
            }
        }
        stage('Test') {
            steps {
                // Perform the test steps
                echo "Image tagged"
            }
        }
        // Add more stages as needed
    }
}

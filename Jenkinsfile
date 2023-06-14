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
                sh "git clone"
            }
        }
        // Define your pipeline stages here
        stage('Build') {
            steps {
                // Perform the build steps
            }
        }
        stage('Test') {
            steps {
                // Perform the test steps
            }
        }
        // Add more stages as needed
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    def dockerImage = docker.build('my-docker-image')

                    // Optionally, you can tag the image with a version or a specific tag
                    dockerImage.tag('my-docker-image:latest')

                    // Push the Docker image to a registry
                    docker.withRegistry('https://registry.example.com', 'dockerhub-cred') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}

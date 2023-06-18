pipeline{
  agent {
    docker {
      image 'abhishekf5/maven-abhishek-docker-agent:v1'
      args '--user root -v /var/run/docker.sock:/var/run/docker.sock' // mount Docker socket to access the host's Docker daemon
    }
  }
    environment{
        
        registry = "kunalk07/gitops-flask"
        registryCredential = 'dockerhub-cred'        
    }
    
    stages{
       stage('Building image') {
      steps{
        script {
            sh "pwd"
          sh "docker build -t kunalk07/gitops-flask:$BUILD_NUMBER ."
        }
      }
    }
       stage('Deploy Image') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
}
}
    

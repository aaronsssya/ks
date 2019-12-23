pipeline {
  agent {
    node {
      label 'go'
    }
  }
  
  stages {
    stage('go hello') {
      steps {
        container('go') {
          sh 'hostnamectl'
          sh 'docker version'
          sh 'docker images'
        }
      }
     }
   }
}

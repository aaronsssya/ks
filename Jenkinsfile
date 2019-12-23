pipeline {
  agent {
    node {
      label 'go'
    }
  }
  
  stages {
    stage('go hello') {
      steps {
        sh 'hostnamectl'
        container('go') {
          sh 'docker version'
          sh 'docker images'
        }
      }
     }
   }
}

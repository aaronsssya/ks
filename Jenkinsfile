pipeline {
  agent {
    node {
      label 'go'
    }
  }
  
  stages {
    stage('go hello') {
      steps {
        container('nodejs') {
          sh 'hostnamectl'
          sh 'docker version'
          sh 'docker images'
        }
      }
     }
   }
}

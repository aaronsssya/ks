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
          sh 'docker version'
          sh 'docker images'
          sh 'sonar-scanner'
        }
      }
     }
   }
}

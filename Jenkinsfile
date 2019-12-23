pipeline {
  agent {
    node {
      label 'nodejs'
    }
  }
  
  stages {
    stage('nodejs hello') {
      steps {
        container('nodejs') {
          sh 'yarn -v'
          sh 'node -v'
          sh 'docker version'
          sh 'docker images'
        }
      }
     }
   }
}

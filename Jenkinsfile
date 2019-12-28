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
          sh '''
              sonar-scanner \
                -Dsonar.projectKey=python-key \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://192.168.1.23:30372 \
                -Dsonar.login=015927321ad1047a91f3334d1d4221f38b718802
          '''
        }
      }
     }
   }
}

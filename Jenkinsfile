pipeline {
  agent {
    node {
      label 'bash'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'python ./test/unit_test.py -v'
      }
    }
  }
}

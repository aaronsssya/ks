pipeline {
  agent {
    node {
      label 'base'
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

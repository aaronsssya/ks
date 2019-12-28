pipeline {
  agent {
    node {
      label 'python'
    }

  }
  stages {
    stage('Unit Test') {
      steps {
        container('python') {
          sh 'python main_test.py -v'
        }

      }
    }
    stage('Scan Code') {
      steps {
        container('python') {
          sh '''sonar-scanner \\
  -Dsonar.projectKey=python-key \\
  -Dsonar.projectVersion=${BUILD_NUMBER} \\
  -Dsonar.sources=$(pwd) \\
  -Dsonar.host.url=http://192.168.1.23:30372 \\
  -Dsonar.login=015927321ad1047a91f3334d1d4221f38b718802 \
  -Dsonar.language=py \
  -Dsonar.sourceEncoding=UTF-8 \
  -Dsonar.python.pylint=/usr/local/bin/pylint \
  -Dsonar.python.pylint_config=.pylintrc \
  -Dsonar.python.pylint.reportPath=pylint-report.txt'''
        }

      }
    }
  }
}
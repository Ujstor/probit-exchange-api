pipeline {
  agent any

  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Ujstor/probit-exchange-api/', branch: 'master')
      }
    }

    stage('Prepair enviroment') {
      steps {
        script {
          sh "cp -f /home/probitenv/.env ${WORKSPACE}"
        }
      }
    }

    stage('Test') {
      steps {
        script {
          sh "${JENKINS_HOME}/scripts/pytest.sh ${WORKSPACE}"
        }
      }
    }

    stage('Build') {
      steps {
        script {
          sh 'docker build -t ujstor/probitapi .'
        }
      }
    }

    stage('Deploy') {
      steps {
        script {
          sh 'docker push ujstor/probitapi'
        }
      }
    }
  }
}

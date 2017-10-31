pipeline {
  agent {
    node {
      label 'start'
    }
    
  }
  stages {
    stage('Clone Code') {
      steps {
        git(credentialsId: '0361a995-132b-44de-84a9-eb214698c3a1', url: 'https://github.com/luozixuan123/python-test', branch: '/master')
      }
    }
    stage('Write File') {
      steps {
        writeFile(file: 'sonar-project.properties', text: 'sonar.projectKey=python-pipeline-test\\nsonar.projectName=python-pipeline-test\\nsonar.projectVersion=1.0\\nsonar.sources=python_test/python_test')
      }
    }
    stage('Code Check') {
      steps {
        sh '$SONAR_RUNNER_HOME/bin/sonar-runner'
      }
    }
    stage('Deploy') {
      steps {
        echo 'pipeline success'
      }
    }
  }
}
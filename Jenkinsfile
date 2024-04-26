pipeline {
    agent any
    environment {
        PATH = "${tool 'Python'}/bin:${env.PATH}"
    }
    stages {
        stage('Build') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
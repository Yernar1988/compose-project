pipeline {
    agent any

    stages {

        stage('Build images') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Stop old containers') {
            steps {
                sh 'docker compose down'
            }
        }

        stage('Start containers') {
            steps {
                sh 'docker compose up -d'
            }
        }
    }
}


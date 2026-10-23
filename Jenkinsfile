
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out by Jenkins.'
            }
        }

        stage('Verify Python') {
            steps {
                script {
                    docker.image('python:3.13-slim').inside {
                        sh 'python --version'
                        sh 'python -m py_compile main.py'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t beauty-studio-api:ci-${BUILD_NUMBER} .'
            }
        }
    }
}

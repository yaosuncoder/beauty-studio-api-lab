pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code will be checked out by Jenkins.'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile main.py'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout / Build') {
            steps {
                sh '''python3 --version'''
                sh '''python3 -m venv .venv'''
                sh '''source .venv/bin/activate'''
                sh '''pip install -r requirements.txt'''
                // bisa buat narik data dari repo, atau ya setup2 requirements
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest -s -v test_automation_api.py'
                // Jalanin testnya dimarih
            }
        }
        stage('Report') {
            steps {
                echo 'Misalnya ada reportnya disini'
                // command reportnya disini
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline successful!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
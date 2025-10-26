pipeline {
    agent any // Specifies that the pipeline can run on any available agent

    stages {
        stage('Checkout / Build') {
            steps {
                echo 'mari tarik codenya dari repo'
                sh '''git clone https://github.com/izar06/python_automation_api.git'''
                sh '''python -m venv .venv'''
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
pipeline {
    agent any
    
    stages {
        stage('Copy Test Files') {
            steps {
                sh '''
                docker exec python-runner mkdir -p /app
                docker cp . python-runner:/app
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'docker exec python-runner pip install -r /app/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker exec -w /app python-runner python -m pytest --maxfail=1 --disable-warnings -v'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
    }
}










// pipeline {
//     agent any

//     stages {
//         stage('Checkout / Build') {
//             steps {
//                 sh '''
//                 python3 -m venv venv
//                 . venv/bin/activate
//                 python -m pip install --upgrade pip
//                 python -m pip install -r requirements.txt
//                 '''
//                 // bisa buat narik data dari repo, atau ya setup2 requirements
//             }
//         }
//         stage('Test') {
//             steps {
//                 echo 'Running tests...'
//                 sh '''
//                 . venv/bin/activate
//                 pytest -s -v test_automation_api.py'''
//                 // Jalanin testnya dimarih
//             }
//         }
//         stage('Report') {
//             steps {
//                 echo 'Misalnya ada reportnya disini'
//                 // command reportnya disini
//             }
//         }
//     }
//     post {
//         always {
//             echo 'Pipeline finished.'
//         }
//         success {
//             echo 'Pipeline successful!'
//         }
//         failure {
//             echo 'Pipeline failed!'
//         }
//     }
// }

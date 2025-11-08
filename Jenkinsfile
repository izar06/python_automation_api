
pipeline {
    agent any

    environment {
        PYTHON_CONTAINER = 'python-runner'
        PROJECT_PATH = '/app'
    }

    stages {
        stage('Copy Test Files') {
            steps {
                echo '📦 Menyalin file ke container python-runner...'
                sh """
                    docker exec ${PYTHON_CONTAINER} mkdir -p ${PROJECT_PATH}
                    docker cp . ${PYTHON_CONTAINER}:${PROJECT_PATH}
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📥 Install dependencies...'
                sh "docker exec ${PYTHON_CONTAINER} pip install -r ${PROJECT_PATH}/requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Menjalankan pytest...'
                sh "docker exec -w ${PROJECT_PATH} ${PYTHON_CONTAINER} python -m pytest --maxfail=1 --disable-warnings -v"
            }
        }
    }

    post {
        always {
            echo '📄 Mencoba archive report...'
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

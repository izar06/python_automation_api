pipeline {
    agent any

    stages {  
        stage('Setup Environment') {
            steps {
                echo "Setting up virtual environment inside python-runner..."
                sh '''
                    docker exec --user 0 python-runner bash -c "
                        python3 -m venv venv &&
                        . venv/bin/activate &&
                        pip install --upgrade pip &&
                        pip install -r requirements.txt
                    "
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running pytest inside python-runner..."
                sh '''
                    docker exec --user 0 python-runner bash -c "
                        . venv/bin/activate &&
                        pytest --maxfail=1 --disable-warnings -q
                    "
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
            archiveArtifacts artifacts: '**/reports/*.html', allowEmptyArchive: true
        }
        failure {
            echo "❌ Some tests failed."
        }
        success {
            echo "✅ All tests passed successfully."
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

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                python3 -m py_compile app.py
                '''
            }
        }

        stage('Deploy App') {
            steps {
                sh '''
                pkill -f app.py || true
                nohup venv/bin/python3 app.py &
                '''
            }
        }
    }
}


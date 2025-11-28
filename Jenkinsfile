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
                python3 -m venv $WORKSPACE/venv
                . $WORKSPACE/venv/bin/activate
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . $WORKSPACE/venv/bin/activate
                python3 -m py_compile app.py
                '''
            }
        }

        stage('Deploy App') {
            steps {
                sh '''
                pkill -f app.py || true
                nohup $WORKSPACE/venv/bin/python3 $WORKSPACE/app.py > app.log 2>&1 &
                '''
            }
        }
    }
}

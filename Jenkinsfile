pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<your-username>/three-tier-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd backend
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo "Run your tests here"'
            }
        }

        stage('Deploy App') {
            steps {
                sh '''
                echo "Starting Flask App..."
                pkill -f app.py || true
                nohup python3 backend/app.py &
                '''
            }
        }
    }
}

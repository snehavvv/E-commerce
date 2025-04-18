pipeline {
    agent any

    environment {
        VENV_DIR = "venv" // Virtual environment directory
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository
                git branch: 'main', url: 'https://github.com/snehavvv/E-commerce.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                // Set up Python virtual environment
                sh '''
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh '''
                source ${VENV_DIR}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests
                sh '''
                source ${VENV_DIR}/bin/activate
                pytest tests/
                '''
            }
        }

        stage('Build and Deploy') {
            steps {
                // Run the Flask application
                sh '''
                source ${VENV_DIR}/bin/activate
                python RestApi/main.py
                '''
            }
        }
    }

    post {
        always {
            // Archive test results or logs
            archiveArtifacts artifacts: '**/logs/*.log', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install bandit'
            }
        }
        stage('SAST Analysis') {
            steps {
                sh 'bandit -f xml -o bandit-output.xml -r . || true'
                recordIssues enabledForFailure: true, tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'bandit-output.xml'
        }
    }
}

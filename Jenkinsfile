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
                // Generate HTML report
                sh 'bandit -f html -o bandit-output.html -r . || true'
                
                // Publish HTML
                publishHTML([
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'bandit-output.html',
                    reportName: 'Bandit Security Report'
                ])
            }
        }
    }
}

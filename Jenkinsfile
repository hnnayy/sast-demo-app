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
                // Generate laporan Bandit dalam bentuk HTML
                sh 'bandit -f html -o bandit-report.html -r . || true'

                // Tampilkan hasil HTML di dashboard Jenkins
                publishHTML([
                    reportName: 'Bandit Report',
                    reportDir: '.',
                    reportFiles: 'bandit-report.html',
                    allowMissing: true,
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ])
            }
        }
    }
}

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
                // Gunakan try-catch untuk menjalankan bandit
                script {
                    try {
                        sh 'bandit -f xml -o bandit-output.xml -r .'
                    } catch (Exception e) {
                        echo "Bandit found security issues, but we'll continue the pipeline"
                    }
                }
                
                // Gunakan warnings-ng plugin dengan konfigurasi yang benar
                recordIssues enabledForFailure: true, 
                            aggregatingResults: true, 
                            tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
    post {
        always {
            // Arsipkan hasil bandit untuk referensi
            archiveArtifacts artifacts: 'bandit-output.xml', allowEmptyArchive: true
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from Git
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/abhijitganeshshinde/Flask_Sample.git']]])
            }
        }
        
        stage('Build') {
            steps {
                sh '/usr/bin/python3 --version' // Use the correct path to Python executable
                sh '/usr/bin/python3 -m pip --version' // Use the correct path to Python executable
                sh '/usr/bin/python3 -m pip install -r requirements.txt' // Use the correct path to Python executable
            }
        }
        
        stage('Test') {
            steps {
                sh '/usr/bin/pytest --version'
                sh '/var/lib/jenkins/.local/bin/pytest'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo Deploying to staging environment...'
            }
        }
    }
    
    post {
        success {
            emailext (
                subject: "Pipeline Success",
                body: "Your pipeline was successful.",
                to: "ashinde1997@gmail.com"
            )
        }
        failure {
            emailext (
                subject: "Pipeline Failure",
                body: "Your pipeline has failed.",
                to: "ashinde1997@gmail.com"
            )
        }
    }
}

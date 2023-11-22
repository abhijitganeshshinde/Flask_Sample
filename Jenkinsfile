pipeline {
    agent any
    
    tools {
        tool 'Python3'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from Git
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/abhijitganeshshinde/Flask_Sample.git']]])
            }
        }
        
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest'
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

pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                
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

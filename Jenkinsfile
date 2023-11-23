pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/abhijitganeshshinde/Flask_Sample.git']]])
            }
        }
        
        stage('Build') {
            steps {
                sh '/usr/bin/python3 --version'
                sh '/usr/bin/python3 -m pip --version'
                sh '/usr/bin/python3 -m pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh '/usr/bin/pytest-3 --version'
                sh '/usr/bin/pytest-3'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo Deploying to staging environment...'
                sh 'cp -r * /var/www/html'
                sh 'sudo chown -R www-data:www-data /var/www/html'
                sh 'sudo chmod -R 755 /var/www/html'
                sh 'echo Deployment to /var/www/html complete.'
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

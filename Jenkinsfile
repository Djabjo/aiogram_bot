pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'bot-memorizer'
        DOCKER_CONTAINER = 'bot-memorizer'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Djabjo/aiogram_bot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t c .'  
            }
        }

        stage('Stop and Remove Old Container') {
            steps {
                sh 'docker stop ${DOCKER_CONTAINER} || true'
                sh 'docker rm ${DOCKER_CONTAINER} || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -it --name ${DOCKER_CONTAINER} -v /Database:/Database ${DOCKER_IMAGE}:v1.0.0'
            }
        }
    }
}
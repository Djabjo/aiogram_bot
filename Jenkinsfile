pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'bot-memorizer'
        DOCKER_CONTAINER = 'bot-memorizer:v1.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Djabjo/aiogram_bot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
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
                sh 'ocker run -it --name bot-memorizer -v /Database:/Database bot-memorizer'
            }
        }
    }
}
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
                sh 'docker build -t bot-memorizer .'  
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
                sh 'docker run -d --name ${DOCKER_CONTAINER} -v /Database:/Database ${DOCKER_IMAGE}'
            }
        }
    }
}
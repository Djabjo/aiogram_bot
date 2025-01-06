#билдим образ 
docker build -t bot-memorizer:v1.0.0 .

#запускаем контейнер
docker run -it --name bot-memorizer -v /Database:/Database bot-memorizer:v1.0.0

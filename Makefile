#билдим образ 
docker build -t c .

#запускаем контейнер
docker run -it --name bot-memorizer -v /Database:/Database bot-memorizer:v1.0.0

#остановка контейнера 
docker stop bot-memorizer 

#запуск после остановки
docker start bot-memorizer

#вызов теминала контейнера 
docker exec -it bot-memorizer /bin/bash

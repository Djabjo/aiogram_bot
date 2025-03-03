#билдим образ 
docker build -t bot-memorizer .

#запускаем контейнер
docker run -d --name bot-memorizer -v /Database:/Database bot-memorizer

#остановка контейнера 
docker stop bot-memorizer 

#запуск после остановки
docker start bot-memorizer

#вызов теминала контейнера 
docker exec -it bot-memorizer /bin/bash

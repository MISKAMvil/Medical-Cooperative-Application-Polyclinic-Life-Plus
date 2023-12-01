FROM ubuntu:20.04 

ENV TZ=Europe/Moscow 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone 
# Обновляем систему
RUN apt-get update -y && apt upgrade -y
# Устанавливаем необходимые пакеты
RUN apt-get install -y python3-pip build-essential
RUN apt-get install -y python3-dev default-libmysqlclient-dev
RUN apt-get install -y pkg-config
RUN apt-get install -y gunicorn
# Создаем дикректорию для проекта
RUN mkdir /project
# Копируем все файлы из текущей директории в папку с проектом
COPY . /project
# Устанавливаем папку проекта в качестве рабочей директории 
WORKDIR /project
# Устанавливаем зависимости для проекта
RUN pip3 install -r requirements.txt
# Устанавливаем папку с wsgi приложением в качестве рабочей директории
WORKDIR /project/app
# Задаем команду для запуска
#CMD /usr/bin/gunicorn -b 0.0.0.0:8000 -w 4 app:app
CMD flask run -p 8000 -h 0.0.0.0
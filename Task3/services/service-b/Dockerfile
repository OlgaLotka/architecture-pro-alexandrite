# Используем базовый образ Python
FROM python:3.13.7-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev mariadb-dev libffi-dev openblas-dev libgfortran lapack-dev build-base openssl-dev

RUN apk add --no-cache hdf5-dev
RUN pip install  -r requirements.txt


#CMD ["python", "service-b.py"]

# Определяем команду для запуска приложения
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
CMD ["python", "service-b.py"]
#CMD ["gunicorn ", "main:app", "--bind", "0.0.0.0:8081" ]
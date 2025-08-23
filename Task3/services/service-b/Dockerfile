# Используем базовый образ Python
FROM python:3.12.0a7-slim-buster 

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости

RUN pip install  -r requirements.txt --no-cache-dir 


#CMD ["python", "service-b.py"]

# Определяем команду для запуска приложения
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
CMD ["python", "service-b.py"]
#CMD ["gunicorn ", "main:app", "--bind", "0.0.0.0:8081" ]
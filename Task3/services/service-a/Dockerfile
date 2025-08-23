# Используем базовый образ Python
FROM python:3.13.7-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY . /app

# Устанавливаем зависимости
# Install h5py with no-binary flag

RUN pip install pkgconfig
RUN pip install  -r requirements.txt --no-cache-dir


#CMD ["python", "service-a.py"]

# Определяем команду для запуска приложения
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8084"] 
CMD ["python", "service-a.py"]
#CMD ["gunicorn ", "main:app", "--bind", "0.0.0.0:8084" ] 
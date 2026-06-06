# Берем легкий образ с Python
FROM python:3.12-slim

# Указываем рабочую папку внутри контейнера
WORKDIR /app

# Копируем файл с библиотеками и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь наш код в контейнер
COPY . .

# Команда, которая запустится при старте контейнера
CMD ["python", "db.py"]
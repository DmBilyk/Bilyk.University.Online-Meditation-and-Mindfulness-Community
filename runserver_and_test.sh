#!/bin/bash

# Запустити сервер D
python manage.py runserver &

# Зачекати 5 секунд
sleep 5

# Запустити тести
python manage.py test

# Завершити процес сервера
kill $(lsof -t -i:8000)

Прописываем команды в командную строку в сл. порядке:

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

После чего, можем запускать сервер:
python manage.py runserver
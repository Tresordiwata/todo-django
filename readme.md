Pour executer le projet
    > python manage.py runserver

Initier la migration
    > python manage.py makemigrations
    > python manage.py migrate

Pour creer les endpoints
    - Il faut creer une fichier urls.py dans l'application



<!-- Creation variable d'environnement -->
python -m venv env

pip freeze > requirements.txt

<!-- Migration -->
>python manage.py makemigrations
>python manage.py migrate

<!-- Creation super user -->
python manage.py createsuperuser
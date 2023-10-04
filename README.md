
clone this repo

create a dotenv file using an example from the repository

run command in virtual envoriment "pip install -r requirements.txt"

python manage.py migrate

python manage.py createsuperuser

python manage.py loaddata printer_fixtures.json

docker-compose up

python manage.py runserver & celery -A Main_app worker --loglevel=info

OR:

in two different terminals:

python manage.py runserver

celery -A Main_app worker --loglevel=info

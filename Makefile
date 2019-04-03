freeze:
		pip freeze | grep -v "pkg-resources" > requirements.txt

super:
		python manage.py createsuperuser

migrations:
		python manage.py makemigrations blog

migrate:
		python manage.py migrate
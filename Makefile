start:
	python3 manage.py runserver

lint:
	poetry run flake8 django_blog/



rundocker:
	cd ./docker && sudo docker-compose up -d

run-develop:
	python manage.py runserver 0.0.0.0:8000 --settings=config.settings.develop
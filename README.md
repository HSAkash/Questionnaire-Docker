# Questionnaire

The course teaches how to build a fully functioning REST API using:

- Python
- Django / Django-REST-Framework
- JWT Token Authentication
- Docker / Docker-Compose
- HTML / JS / CSS

##Django Rest APi
[Documentation](https://www.django-rest-framework.org/)

##Docker
[Read more](https://www.docker.com/)

Install docker
[Windows](https://docs.docker.com/desktop/windows/install/)
[Mac](https://docs.docker.com/desktop/mac/install/)
Linux:

```
sudo snap install docker
```

## Getting started

Build Docker:

```
sudo docker build .
```

Build Docker Compose:

```
sudo docker-compose build
```

Service Migration:

```
sudo docker-compose run app sh -c "python manage.py makemigrations user"
sudo docker-compose run app sh -c "python manage.py makemigrations post"
```

Or

```
sudo docker-compose run app python manage.py makemigrations user
sudo docker-compose run app python manage.py makemigrations post
```

To start project, run:

```
sudo docker-compose up
```

The API will then be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

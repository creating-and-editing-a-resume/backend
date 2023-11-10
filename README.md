# Backend for Resume Creation Service
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)
[![Django](https://img.shields.io/badge/django-4.2-green)](https://docs.djangoproject.com/en/4.2/)
[![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-v3.12-green)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/-Docker_Compose-384d54?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.0-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-green)](https://docs.gunicorn.org/en/stable/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)

## Description

## Features

## Technologies Used
* Python 3.11
* Django 4.2
* Django REST Framework 3.14
* PostgreSQL 13+
* Docker
* Docker Compose
* Nginx
* Gunicorn

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository using:
```
git clone https://github.com/creating-and-editing-a-resume/backend.git
```
2. Create a .env file in the root directory of the project.

3. Add the following environment variables to the .env file:
```
SECRET_KEY=django-insecure-@5(x_6kcbt8l=ft_j%+$*29c#&5sk&k1raa%s-1uox6fuc0ooe
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, 0.0.0.0, localhost
POSTGRES_DB=creating_and_editing_a_resume_db
POSTGRES_USER=creating_and_editing_a_resume_user
POSTGRES_PASSWORD=creating_and_editing_a_resume_password
DB_HOST=creating_and_editing_a_resume_db
DB_PORT=5432
```
4. Navigate to the project directory using:
```
cd backend
```

5. Start the Django development server using the following command:
```
docker-compose up -d --build
```

6. Next, execute the commands one by one:
```
docker-compose exec backend poetry run python manage.py makemigration
docker-compose exec backend poetry run python manage.py migrate
docker-compose exec backend poetry run python manage.py createsuperuser
docker-compose exec backend poetry run python manage.py collectstatic --no-input
```
7. Open your web browser and navigate to http://127.0.0.1 to view the application.

## Credits

## License

## Contributing
If you have any questions, suggestions, requests, or comments, please feel free to open [issues or pull requests](https://github.com/creating-and-editing-a-resume/backend/issues) in this repository.

FROM python:3.10-slim
WORKDIR /app
RUN pip3 install poetry
COPY pyproject.toml poetry.lock /app/
RUN poetry install
COPY . .
CMD ["poetry", "run", "gunicorn", "creating_and_editing_a_resume.wsgi:application", "--bind", "0:8000"]

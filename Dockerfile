FROM python:3.11-slim-bullseye

# Copy project files
WORKDIR /app

COPY Pipfile Pipfile.lock /app/
COPY src/ /app/src

# Install dependencies
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system

ENTRYPOINT ["python", "src/main.py"]
FROM python:3.11-alpine

ARG DJANGO_SECRET_KEY
ARG SENTRY_DSN
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY_GITLAB
ENV SENTRY_DSN=$SENTRY_DSN_GITLAB

WORKDIR .

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python replace_config.py && \
    python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

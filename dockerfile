# Utilisez l'image Amazon Linux 2023 en tant que base
FROM amazonlinux:2023

# Installez les outils de développement et Python
RUN yum -y update && \
    yum -y groupinstall "Development Tools" && \
    yum -y install python3 python3-pip

# Configurez les variables d'environnement Django
ARG DJANGO_SECRET_KEY
ARG SENTRY_DSN
ARG DJANGO_STATUS
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV DJANGO_STATUS=$DJANGO_STATUS
ENV SENTRY_DSN=$SENTRY_DSN

# Installez les dépendances et copiez les fichiers de l'application
WORKDIR .
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Exécutez les migrations Django
RUN python3 replace_config.py && \
    python3 manage.py migrate

# Exposez le port 8000
EXPOSE 8000

# Lancez le serveur Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

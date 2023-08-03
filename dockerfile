# Utilisez l'image Amazon Linux 2023 en tant que base
FROM amazonlinux:2023

# Installez les outils de développement et Python
RUN yum -y update && \
    yum -y groupinstall "Development Tools" && \
    yum -y install python3

# Configurez les variables d'environnement Django
ARG DJANGO_SECRET_KEY
ARG SENTRY_DSN
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV SENTRY_DSN=$SENTRY_DSN

# Installez les dépendances et copiez les fichiers de l'application
WORKDIR .
COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
COPY . .

# Exécutez les migrations Django
RUN python3 replace_config.py && \
    python3 manage.py migrate

# Exposez le port 8000
EXPOSE 8000

# Lancez le serveur Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

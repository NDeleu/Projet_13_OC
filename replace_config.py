import os
import configparser
import sys


def replace_config():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python replace_config.py <DJANGO_SECRET_KEY> <SENTRY_DSN> <DJANGO_STATUS>")
        sys.exit(1)

    # Chemin vers le fichier config.ini
    config_file_path = 'config.ini'

    # Vérifier si config.ini existe
    if not os.path.exists(config_file_path):
        # Créer un nouveau fichier config.ini avec les valeurs par défaut
        with open(config_file_path, 'w') as configfile:
            config = configparser.ConfigParser()
            config['django'] = {'secret_key': 'default_secret_key'}
            config['config'] = {'status': 'production'}
            config['sentry'] = {'dsn': 'default_sentry_dsn'}
            config.write(configfile)

    # Get the command-line arguments
    django_secret_key = sys.argv[1]
    sentry_dsn = sys.argv[2]
    django_status = sys.argv[3]

    # Remplacer les valeurs dans le fichier config.ini
    config = configparser.ConfigParser(interpolation=None)
    config.read(config_file_path)

    if config['django']['secret_key'] == 'default_secret_key' \
            or config['sentry']['dsn'] == 'default_sentry_dsn' \
            or config['config']['status'] == 'development':
        # Les valeurs par défaut sont détectées, mettre à jour
        # le fichier config.ini
        config['django']['secret_key'] = django_secret_key
        config['config']['status'] = django_status
        config['sentry']['dsn'] = sentry_dsn

        # Enregistrer les modifications dans le fichier config.ini
        with open(config_file_path, 'w') as configfile:
            config.write(configfile)

    # Le fichier config.ini est prêt, continuer avec le reste du script


if __name__ == "__main__":
    replace_config()

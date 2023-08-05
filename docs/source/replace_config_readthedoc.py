import os
import configparser


def replace_config():
    # Chemin vers le fichier config.ini
    config_file_path = os.path.join(os.path.dirname(__file__),
                                    '../../config.ini')

    # Créer un nouveau fichier config.ini avec les valeurs
    # par défaut s'il n'existe pas
    if not os.path.exists(config_file_path):
        with open(config_file_path, 'w') as configfile:
            config = configparser.ConfigParser()
            config['django'] = {'secret_key': 'default_secret_key'}
            config['config'] = {'status': 'development'}
            config['sentry'] = {'dsn': 'default_sentry_dsn'}
            config.write(configfile)

    # Obtenir les valeurs des variables d'environnement
    django_secret_key = os.getenv('DJANGO_SECRET_KEY', 'default_secret_key')
    sentry_dsn = os.getenv('SENTRY_DSN', 'default_sentry_dsn')
    django_status = os.getenv('DJANGO_STATUS', 'development')

    # Remplacer les valeurs dans le fichier config.ini
    config = configparser.ConfigParser(interpolation=None)
    config.read(config_file_path)

    # Si les valeurs par défaut sont détectées,
    # mettre à jour le fichier config.ini
    if config['django']['secret_key'] == 'default_secret_key' \
            or config['sentry']['dsn'] == 'default_sentry_dsn' \
            or config['config']['status'] == 'development':
        config['django']['secret_key'] = django_secret_key
        config['sentry']['dsn'] = sentry_dsn
        config['config']['status'] = django_status

        # Enregistrer les modifications dans le fichier config.ini
        with open(config_file_path, 'w') as configfile:
            config.write(configfile)

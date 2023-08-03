import os
import configparser


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

# Charger les variables GitLab CI/CD
django_secret_key = os.environ.get('DJANGO_SECRET_KEY', 'default_secret_key')
django_status = os.environ.get('DJANGO_STATUS', 'development')
sentry_dsn = os.environ.get('SENTRY_DSN', 'default_sentry_dsn')

# Remplacer les valeurs dans le fichier config.ini
config = configparser.ConfigParser(interpolation=None)
config.read(config_file_path)

if config['django']['secret_key'] == 'default_secret_key' \
        or config['sentry']['dsn'] == 'default_sentry_dsn' \
        or config['config']['status'] == 'development':
    # Les valeurs par défaut sont détectées, mettre à jour
    # le fichier config.ini
    config['django']['secret_key'] = django_secret_key
    config['django']['config'] = django_status
    config['sentry']['dsn'] = sentry_dsn

    # Enregistrer les modifications dans le fichier config.ini
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

# Le fichier config.ini est prêt, continuer avec le reste du script

django_secret_key = config.get('django', 'secret_key', raw=True)
django_status = config.get('config', 'status', raw=True)
sentry_dsn = config.get('sentry', 'dsn', raw=True)

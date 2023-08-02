import os
import sys


def main():
    """
    Point d'entrée principal pour l'exécution des commandes Django
        depuis la ligne de commande.

    Cette fonction configure le module de paramètres Django
        et exécute les commandes spécifiées dans la ligne de commande.

    Returns:
        None

    Raises:
        ImportError: Si Django n'est pas installé ou
            n'est pas disponible sur le PYTHONPATH.

    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

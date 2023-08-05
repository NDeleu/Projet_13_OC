import os
import sys
import django

os.system("python replace_config.py")

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

project = 'Python OC Lettings FR'
copyright = '2023, Nicolas Deleu'
author = 'Nicolas Deleu'
release = '1.0.0'

# Activez l'extension autodoc
extensions = ['sphinx.ext.autodoc']

# Incluez les modules à documenter (lettings, profiles, oc_lettings_site)
autodoc_default_flags = [
    'members', 'undoc-members', 'private-members', 'show-inheritance'
]
autodoc_modules = {
    'lettings': 'lettings',
    'profiles': 'profiles',
    'oc_lettings_site': 'oc_lettings_site',
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site/settings'
django.setup()

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../oc_lettings_site/'))
sys.path.insert(0, os.path.abspath('../../oc_lettings_site/tests/'))
sys.path.insert(0, os.path.abspath('../../lettings/'))
sys.path.insert(0, os.path.abspath('../../lettings/tests/'))
sys.path.insert(0, os.path.abspath('../../profiles/'))
sys.path.insert(0, os.path.abspath('../../profiles/tests/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python OC Lettings FR'
copyright = '2023, Nicolas Deleu'
author = 'Nicolas Deleu'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
# http://www.sphinx-doc.org/en/master/config

import guzzle_sphinx_theme

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'WebCamp Zagreb Docs'
copyright = '2019, WebCamp Zagreb team & contributors'
author = 'WebCamp Zagreb team & contributors'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.githubpages',
    'guzzle_sphinx_theme',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = None

# -- Options for HTML output -------------------------------------------------

html_title = "WebCamp Zagreb Docs"

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'
html_theme_options = {}

html_static_path = ['_static']
html_sidebars = {
    '**': [
        'logo-text.html',
        'globaltoc.html',
        'searchbox.html',
    ],
}

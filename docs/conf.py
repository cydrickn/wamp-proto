# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import os
import sys
import json
import time
from sphinx.highlighting import lexers

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

try:
    from sphinxcontrib import spelling
except ImportError:
    spelling = None

# Check if we are building on readthedocs
RTD_BUILD = os.environ.get('READTHEDOCS', None) == 'True'

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '_ext'))


# -- Project information -----------------------------------------------------

project = 'Web Application Messaging Protocol'
author = 'Crossbar.io Technologies GmbH'
this_year = u'{0}'.format(time.strftime('%Y'))
if this_year != u'2012':
    copyright = u'2012-{0}, Crossbar.io Technologies GmbH'.format(this_year)
else:
    copyright = u'2012, Crossbar.io Technologies GmbH'

# The short X.Y version
version = 'version 2'
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Usage: .. thumbnail:: picture.png
    'sphinxcontrib.images',
]

# https://pythonhosted.org/sphinxcontrib-images/#how-to-configure
images_config = {
    'override_image_directive': False
}

# extensions not available on RTD
if spelling is not None:
    extensions.append('sphinxcontrib.spelling')
    spelling_lang = 'en_US'
    spelling_show_suggestions = False
    spelling_word_list_filename = 'spelling_wordlist.txt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_work', '_design']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# the following trickery is to make it build both locally and on RTD
#
# see: https://blog.deimos.fr/2014/10/02/sphinxdoc-and-readthedocs-theme-tricks-2/
#
if RTD_BUILD:
    html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/css/custom.css'
        ]
    }
else:
    if sphinx_rtd_theme:
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

        # add custom CSS on top of Sphinx RTD standard CSS
        # https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html
        def setup(app):
            # deprecated at 1.8.0. Please use app.add_css_file() instead.
            app.add_css_file('css/custom.css')
            app.add_js_file('js/custom.js')
    else:
        html_theme = 'default'

html_logo = '_static/img/wamp_logo_white.png'
full_logo = True

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'collapse_navigation': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
#pygments_style = 'monokai'
#pygments_style = 'native'
#pygments_style = 'pastie'
pygments_style = 'friendly'

# http://www.sphinx-doc.org/en/master/theming.html
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html#html-theme-options
html_theme_options = {
    'canonical_url': 'https://wamp-proto.org/',
    'display_version': False,
}

# -- Extension configuration -------------------------------------------------

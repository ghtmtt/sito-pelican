#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matteo Ghetta'
SITENAME = u'GeoPenguin'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# include extras (images, css, ...) in the final output folder
STATIC_PATHS = ['images']


# Bootstrap options

# dont show post categories on the top bar
DISPLAY_CATEGORIES_ON_MENU = False

# for ordering pages relative to the attribute metadata. ALL PAGES MUST HAVE IT!
PAGE_ORDER_BY = 'attribute'
PAGES_SORT_ATTRIBUTE = 'attribute'

# HIDE_SIDEBAR = True


# Theme
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = "united"


# Traslation environment with plugin and jinja
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ["../plugins"]
PLUGINS = ['i18n_subsites']

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'it': {
        'SITENAME': 'Il mio Sito',
    }
}

languages_lookup = {
    'en': 'English',
    'it': 'Italiano'
}


def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
}

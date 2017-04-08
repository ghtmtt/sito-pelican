#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matteo Ghetta'
SITENAME = u'GeoPenguin'
SITEURL = ''
# workaround to make languages work, see includes/nav.bar
SITEURLABS = SITEURL


PATH = 'content'

TIMEZONE = 'Europe/Rome'

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
# DISPLAY_BREADCRUMBS = True

# include extras (images, css, ...) in the final output folder
STATIC_PATHS = ['images']


# Bootstrap options

# dont show post categories on the top bar
DISPLAY_CATEGORIES_ON_MENU = False

# categories on the lateral sidebar
DISPLAY_CATEGORIES_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True


# for ordering pages relative to the attribute metadata. ALL PAGES MUST HAVE IT!
PAGE_ORDER_BY = 'attribute'
PAGES_SORT_ATTRIBUTE = 'attribute'


# markdown extension and values
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.toc': {'permalink': True},
        'markdown.extensions.attr_list': {},
    }
}


# Theme
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = "united"


# Traslation environment with plugin and jinja
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# plugins loading
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ['i18n_subsites', 'headerid', 'tipue_search']


# Settings for i18n plugin, folder, etc
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'it': {
        # 'MENUITEMS': [
        #     ('Blog', '/pages/about.html')
        # ],
        'THEME_STATIC_DIR': 'pelican-bootstrap3',
    },
    'en': {
        # 'MENUITEMS': [
        #     ('Blog', '/pages/courses.html')
        # ],
        # 'OUTPUT_PATH': 'output/en',
        'THEME_STATIC_DIR': 'pelican-bootstrap3',
    },
}


DELETE_OUTPUT_DIRECTORY = True

languages_lookup = {
    'en': 'English',
    'it': 'Italiano'
}


def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


def extract_trans(article, lang, url):
    for trans in article.translations:
        if trans.lang == lang:
            return trans.url
    return url


JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
    'extract_trans': extract_trans,
}


# google analytics code
GOOGLE_ANALYTICS = "UA-96942229-1"
DISQUS_SITENAME = "geopenguin"

# for the moment, hardcode index, category and tag pages for languages
# see includes/nav-bar
INDEX_EN = 'http://localhost:8000/en/'
INDEX_IT = 'http://localhost:8000/it/'
CATEGORY_EN = ''
CATEGORY_IT = ''
TAG_EN = ''
TAG_IT = ''


# needed for the searching bar. **ALL TEMPLATED MUST BE ADDED**
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'tags', 'search']


ARCHIVES_SAVE_AS = 'archives.html'

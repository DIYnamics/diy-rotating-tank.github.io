#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The DIYnamics Team'
SITENAME = 'DIYnamics'
SITEURL = ''
SITESUBTITLE = 'Affordable materials for geoscience teaching demonstrations'
SITEIMAGE = '/images/homepage_slideshow.gif'
DESCRIPTION = ('DIYnamics: affordable, accessible Earth science demonstration '
               'and teaching materials')
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

INDEX_SAVE_AS = 'blog.html'

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images', 'pdfs']

ICONS = [
    ['github', 'https://github.com/DIYnamics/diynamics.github.io'],
    ['twitter', 'https://twitter.com/DIYnamicsTeam'],
]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
LINKS = [
    ['about', '/pages/about.html'],
    ['resources', '/pages/resources.html'],
    ['events', '/pages/events.html'],
    ['blog', '/blog.html'],
    ['links', '/pages/links.html'],
    ['team', '/pages/people.html'],
    ['acknowledgments', '/pages/acknowledgments.html'],
]

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

PAGE_ORDER_BY = 'page-order'

THEME = 'themes/pelican-alchemy/alchemy'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.youtube',
           ]

DISQUS_SITENAME = "diynamics"
TWITTER_USERNAME = "DIYnamicsTeam"

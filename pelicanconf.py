#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christopher Bonnett'
SITENAME = u'MK47'
SITEURL = ''

PATH = 'content'
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
 
THEME = '/Users/Christopher_old/ice/github_code/pelican-themes/octopress'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# Social widget
#SOCIAL = ('https://twitter.com/cbonnett', '#')
TWITTER_USER = 'cbonnett'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

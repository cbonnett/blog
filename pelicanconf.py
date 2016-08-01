#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christopher Bonnett'
SITENAME = u'Adventures in Machine Learning'
SITESUBTITLE = u''
SITEURL = 'http://cbonnett.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs'] 
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
                    
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'               
 
THEME = '/Users/Christopher_old/ice/github_code/pelican-themes/octopress'

MENUITEMS = [('LinkedIn', 'https://www.linkedin.com/in/cbonnett')]
NEWEST_FIRST_ARCHIVES = False

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
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
DEFAULT_PAGINATION = 10
DISQUS_SITENAME = "mk49"
                                               
# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# -*- coding: utf-8 -*-
"""
Settings file for project
"""
import os
from webassets import Bundle

DEBUG = True

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

# Common site name and domain to use available in templates
SITE_NAME = 'Bagel Street'
SITE_DOMAIN = '192.168.0.103:8001'

# Sources directory where the assets will be searched
SOURCES_DIR = os.path.join(PROJECT_DIR, 'sources')
# Templates directory
TEMPLATES_DIR = os.path.join(SOURCES_DIR, 'templates')
# Directory where all stuff will be builded
PUBLISH_DIR = os.path.join(PROJECT_DIR, '_build/dev')
# Path where will be moved all the static files, usually this is a directory in
# the ``PUBLISH_DIR``
STATIC_DIR = os.path.join(PROJECT_DIR, PUBLISH_DIR, 'static')

# The static url to use in templates and with webassets
# This can be a full URL like http://, a relative path or an absolute path
STATIC_URL = 'static/'

# Extra or custom bundles
#BUNDLES = {
    #'modernizr_js': Bundle(
        #"js/modernizr.src.js",
        #filters='yui_js',
        #output='js/modernizr.min.js'
    #),
    #'app_css': Bundle(
        #'css/app.css',
        #filters='yui_css',
        #output='css/app.min.css'
    #),
    #'app_js': Bundle(
        #"js/app.js",
        #filters='yui_js',
        #output='js/app.min.js'
    #),
#}

# Extra or custom bundles
from project.assets import PUBLISHED_BUNDLES as BUNDLES


# Sources files or directory to synchronize within the static directory
FILES_TO_SYNC = (
    #(SOURCE, DESTINATION)
    #('css', 'css'),
)

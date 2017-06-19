#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/python_projects/")

from python_projects import app as application
application.secret_key = 'fdhsdfh4y42723jkjkh5klh234589234523h834580923'
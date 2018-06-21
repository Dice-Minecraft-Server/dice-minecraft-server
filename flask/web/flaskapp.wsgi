#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/b10509017/flask/web/")
from app import app as application
application.secret_key = 'qwertasdf'

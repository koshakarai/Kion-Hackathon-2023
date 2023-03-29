""" Docstring """
import json

import pyrebase
import firebase_admin
from firebase_admin import credentials, auth


credential = credentials.Certificate('key.json')

firebase = firebase_admin.initialize_app(cred)
pyrebase = pyrebase.initialize_app(json.load(open('firebase_config.json')))

def create_user():
    ...
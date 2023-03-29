import json
import os

SRC_DIR = os.path.dirname(os.path.dirname(__file__))
CREDS_PATH = os.path.join(SRC_DIR, "yc/creds.json")
creds = json.load(open(CREDS_PATH, "r"))

FOLDERID = creds['FOLDERID']
API_KEY = creds['API_KEY']


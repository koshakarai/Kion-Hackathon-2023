""" Configuration module """

import os

from starlette.config import Config


SRC_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(SRC_DIR, ".env")
# '/home/<user>/<...>/Kion/backend' | root of backend
# '/home/<user>/<...>/Kion/backend/.env' | env path


# Config will be read from environment variables and/or ".env" files.
config = Config(ENV_PATH)


# project info
PROJECT_NAME = config("PROJECT_NAME")
VERSION = config("VERSION")


# Debug | make sure disable in production!
DEBUG = config("DEBUG", cast=bool, default=False) 


# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings)
# CORS_ORIGIN_...


# Uvicorn settings
RELOAD = config("RELOAD", cast=bool, default=False)
...

if __name__ == '__main__':
    from pprint import pprint
    
    pprint(f'src dirictory: {SRC_DIR}')
    pprint(f'.env path: {ENV_PATH}')
    
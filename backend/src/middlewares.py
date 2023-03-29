""" Application meddlewares 

   nothing meddleware yet :(
"""

from starlette.middleware.base import BaseHTTPMiddleware 
from fastapi.middleware.cors import CORSMiddleware

def setup_middlewares(application):
    """ setup application middlewares 
        (use in asgi)
    """

    # test CORS
    allow_all = ['*']
    application.add_middleware(
            CORSMiddleware,
            allow_origins=allow_all,
            allow_credentials=True,
            allow_methods=allow_all,
            allow_headers=allow_all
    )
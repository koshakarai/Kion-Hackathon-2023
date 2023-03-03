""" Asynchronous Server Gateway Interface
    
    authors: Koshar Akay (koshakarai) 
             ... Egor (FaVaku)
             ... Saveliy (...)
"""

import asyncio

from fastapi import FastAPI

import config 
from middlewares import setup_middlewares
from main_router import setup_routes


app = FastAPI()

def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, 
        debug=settings.DEBUG, 
        version=settings.VERSION,
    )

    @application.on_event("startup")
    async def handle_startup_events():
        # await setup_middlewares(application) | Uncomment when middleware appears  
        await setup_routes(application)

    @application.on_event("shutdown")
    async def handle_shutdown_events():
        ...

    return application

app = get_application()
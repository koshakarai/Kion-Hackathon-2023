""" Asynchronous Server Gateway Interface
    
    authors: Koshar Akay (koshakarai) 
             Tsarkov Egor (FaVaku)
             Semenochev Saveliy (Save1iy2)
"""

import asyncio

from fastapi import FastAPI

import config 
from middlewares import setup_middlewares
from main_router import setup_routes

def get_application() -> FastAPI:
    application = FastAPI( 
        title=config.PROJECT_NAME,
        version=config.VERSION,
        debug=config.DEBUG, 
    )
    
    
    setup_middlewares(application)  
    
    @application.on_event("startup")
    async def handle_startup_events():
        await setup_routes(application)

    @application.on_event("shutdown")
    async def handle_shutdown_events():
        ...

    return application

app = get_application()
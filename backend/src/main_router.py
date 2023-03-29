""" Application main router """

async def setup_routes(application) -> None:
    """ import and include to assembly all application routers 
        (use in asgi)
    """

    # from api.v1 import router as v1_router | Example
    # from api.v2 import router as v2_router | 

    # include app routers
    # application.include_router(v1_router, prefix='v1', tags=['v1']) | Example
    # application.include_router(v2_router, prefix='v2', tags=['v2']) |

    from example.endpoints import router as examle_router
    from yc.endpoints import router as ycservices_router
    from ICG.endpoints import router as icg_router
    
    application.include_router(examle_router, tags=['temporary'])
    application.include_router(ycservices_router)
    application.include_router(icg_router)
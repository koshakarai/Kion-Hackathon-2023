#!/usr/bin/env python
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

    ...
""" Exemple app router 

    Api endpoints:
        /example/hello
"""

from fastapi import APIRouter


router = APIRouter(
    prefix = '/example',
    responses = {404: {"description": "Not found"}},
)

@router.get('/')
async def hello(): return {'msg': 'Hello True Tech Hack!'}

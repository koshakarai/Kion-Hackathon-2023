""" Text to speech

    Api endpoints:
        /yc/TTS
"""

from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse


from .schemas import TTSRequest
from .services import YCTTS, YCT

router = APIRouter(
    prefix = '/yc',
    responses = {404: {"description": "Not found"}},
)

@router.post('/TTS/')
async def TTS(req: TTSRequest): 

    Content = YCTTS(req)
    
    return Content

@router.post('/TRN/')
async def TTS(req: TTSRequest): 

    Content = YCT(req.text)
    
    return Content


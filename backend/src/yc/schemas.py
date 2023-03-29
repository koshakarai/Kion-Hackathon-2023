from pydantic import BaseModel, validator


class TTSRequest(BaseModel):
    text: str 
    voice: str = 'jane' # oksana
    emotion: str = 'evil'
    speed: str = '1.0'

    @validator('text', allow_reuse=True)
    def text_validation(cls, v):
        if not 0 < len(v) < 5000:
            raise ValueError('Test lenght must be in the range from 0 to 5000')
        return v
    
    @validator('voice', allow_reuse=True)
    def text_validation(cls, v):
        if v not in ['jane', 'oksana']:
            raise ValueError('No such voice exist')
        return v
    
    @validator('emotion', allow_reuse=True)
    def text_validation(cls, v):
        if v not in ['evil', 'neutral']:
            raise ValueError('No such emotion exist')
        return v
    
class TTSRequest(BaseModel):
    text: str 
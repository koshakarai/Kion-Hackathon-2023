import requests

from .creds import API_KEY, FOLDERID
from .schemas import TTSRequest

import json

def YCTTS(data: TTSRequest): 
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    
    headers = {'Authorization': 'Api-key ' + API_KEY}
    
    data = {
        'folderId': FOLDERID,
        'text': data.text,
        'lang': 'ru-RU',
        'voice': data.voice,
        'emotion': data.emotion,
        'speed': data.speed,

        'format': 'oggopus',
        'sampleRateHertz': 48000,
    }
    
    ret = []

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))
 
        for chunk in resp.iter_content(chunk_size=None):
            ret.append(chunk)
    print(ret)
    return str(ret[0])  

def YCT(text):
    target_language = 'ru'


    body = {
        "targetLanguageCode": target_language,
        "texts": text,
        "folderId": FOLDERID,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": 'Api-key ' + API_KEY
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
        json = body,
        headers = headers
    )
    print(response.text)
    return response.json()['translations'][0]["text"]
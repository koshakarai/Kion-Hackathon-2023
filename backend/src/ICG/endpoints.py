from fastapi import File, UploadFile, APIRouter
from PIL import Image as pil_image
from yc.services import YCT
import io

from .caption_generator import GIC

router = APIRouter(
    prefix = '/icg',
    responses = {404: {"description": "Not found"}},
)

@router.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()

        imageStream = io.BytesIO(contents)
        imageFile = pil_image.open(imageStream)
        res = GIC(imageFile)
    except Exception as e:
        raise e
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"Грустная собака"}#YCT(res)


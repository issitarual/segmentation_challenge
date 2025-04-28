from fastapi import APIRouter, UploadFile,HTTPException
from app.pipelines.segmentation import segmentation_pipeline
import numpy as np
from PIL import Image
import cv2

router = APIRouter()

@router.post("/segment/")
async def segment_image(input_image: UploadFile):
    if input_image is None:
        raise HTTPException(status_code=400, detail="Nenhuma imagem enviada.")

    contents = await input_image.read()

    if not contents:
        raise HTTPException(status_code=400, detail="Arquivo de imagem vazio.")

    nparr = np.frombuffer(contents, np.uint8)

    image_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # BGR padrão

    wall_mask, window_mask, segmented_img = segmentation_pipeline(image_np)

    return {
        "wall_mask": wall_mask.tolist(),
        "window_mask": window_mask.tolist(),
        "segmented_img": segmented_img.tolist(),
    }
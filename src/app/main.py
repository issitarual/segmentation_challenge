from fastapi import FastAPI, APIRouter, UploadFile, File, HTTPException

from app.api.routes_segmentation import router as segmentation_router

app = FastAPI()

app.include_router(segmentation_router, prefix="/segmentation", tags=["Segmentation"])

@app.get("/")
async def root():
    return {"message": "Lumina Lab API is running"}

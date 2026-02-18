from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.services.similarity_service import SimilarityService

app = FastAPI()

service = SimilarityService()

UPLOAD_DIR = "storage/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "Assignment Similarity Detection API running"}


@app.post("/upload")
async def upload_assignment(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    service.add_assignment(file_path, file.filename)

    return {"message": f"{file.filename} uploaded and processed successfully"}


@app.post("/check-similarity")
async def check_similarity(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = service.check_similarity(file_path)

    return {"results": results}

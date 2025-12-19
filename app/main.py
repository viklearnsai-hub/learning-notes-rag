from fastapi import FastAPI,UploadFile,Response
from app.injestion.uploadfile import UploadFileService
from typing import Tuple
from app.models.uploadresponse import UploadResponse
app = FastAPI(title="Learning notes rag assistant")
service = UploadFileService()

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.post("/upload")
def upload_file(file:UploadFile) -> Tuple[UploadResponse,int]:
  return service.upload_file(file)
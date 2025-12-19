from fastapi import FastAPI,UploadFile,File
from app.injestion.uploadfile import UploadFileService

app = FastAPI(title="Learning notes rag assistant")
service = UploadFileService()

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.post("/upload")
def upload_file(file:UploadFile):
     service.uploadFile(file)
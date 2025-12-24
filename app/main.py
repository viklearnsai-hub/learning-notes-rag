from fastapi import FastAPI,UploadFile,status
from app.injestion.uploadfile import UploadFileService
from app.models.uploadresponse import UploadResponse
app = FastAPI(title="Learning notes rag assistant")
service = UploadFileService()

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.post("/upload",status_code=status.HTTP_201_CREATED)
async def upload_file(file:UploadFile) -> UploadResponse :
  return await service.upload_file(file)
from fastapi import FastAPI,UploadFile,Response,status
from app.injestion.uploadfile import UploadFileService

app = FastAPI(title="Learning notes rag assistant")
service = UploadFileService()

@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.post("/upload")
def upload_file(file:UploadFile) -> Response:
    success =  service.upload_file(file)
    if(success):
        return Response("File uploaded Successfully",status_code=status.HTTP_200_OK)
    else:
         return Response("Error Occured whiel uploading service",status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
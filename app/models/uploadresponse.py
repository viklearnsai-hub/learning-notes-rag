from pydantic import BaseModel

class UploadResponse(BaseModel):
    msg:str
    successful:bool
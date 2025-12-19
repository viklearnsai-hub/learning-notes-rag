from fastapi import UploadFile,status
from app.library.helpers.validation import validate_file_type
from app.models.uploadresponse import UploadResponse
from typing import Tuple
class UploadFileService:

    def upload_file(self,uploaded_file:UploadFile) -> Tuple[UploadResponse,int]:
        if (validate_file_type(uploaded_file)):
            res = UploadResponse(msg="Upload Successful",successful=True)
            return res,status.HTTP_200_OK
        else:
            res = UploadResponse(msg="Invalid filetype",successful=False)
            return res,status.HTTP_400_BAD_REQUEST



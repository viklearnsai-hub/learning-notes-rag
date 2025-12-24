from fastapi import UploadFile,status,HTTPException
from app.library.helpers.validation import validate_file_type
from app.library.helpers.file_helper import read_file_and_normalize
from app.models.uploadresponse import UploadResponse
class UploadFileService:

    async def upload_file(self,uploaded_file:UploadFile) -> UploadResponse:
        if (validate_file_type(uploaded_file)):
            content = await read_file_and_normalize(uploaded_file)
            print("Normalized Content",content)
            res = UploadResponse(msg="Upload Successful",successful=True)
            return res
        else:
            res = UploadResponse(msg="Invalid filetype",successful=False)
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)



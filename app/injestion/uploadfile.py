from fastapi import UploadFile,Response,status
from app.library.helpers.validation import validate_file_type
from app.models.uploadresponse import UploadResponse
class UploadFileService:

    def upload_file(self,uploaded_file:UploadFile) -> Response:
        if (validate_file_type(uploaded_file)):
            res = UploadResponse(msg="Upload Successful",successful=True)
            return Response(res,status_code=status.HTTP_200_OK)
        else:
            res = UploadResponse(msg="Invalid filetype",successful=True)
            return Response(res,status_code=status.HTTP_400_BAD_REQUEST)



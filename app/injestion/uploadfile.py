from fastapi import UploadFile
from app.library.helpers.validation import validate_file_type
class UploadFileService:

    def upload_file(self,uploaded_file:UploadFile) -> bool:
        if (validate_file_type(uploaded_file)):
            return True


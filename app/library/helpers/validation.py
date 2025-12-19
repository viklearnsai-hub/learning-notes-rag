
from app.library.helpers.constants import ACCPECTED_FILE_CONTENT_TYPE
from fastapi import UploadFile


def validate_file_type(uploaded_file:UploadFile) -> bool:
   guessed_file_content_type = uploaded_file.content_type
   return guessed_file_content_type != None and ACCPECTED_FILE_CONTENT_TYPE.__contains__(guessed_file_content_type)


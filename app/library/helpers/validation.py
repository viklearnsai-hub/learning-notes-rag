
from constants import ACCPECTED_FILE_EXTENSIONS,MAX_FILE_SIZE
from fastapi import UploadFile
import filetype

def validate_file_type(uploaded_file:UploadFile) -> bool:
   guessed_file_ext = filetype.guess_extension(uploaded_file.file)
   return guessed_file_ext != None and ACCPECTED_FILE_EXTENSIONS.__contains__(guessed_file_ext)

def is_within_size_limit(fileSize:int) -> bool:
   return filetype <= MAX_FILE_SIZE

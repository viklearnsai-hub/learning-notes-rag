from fastapi import UploadFile
import unicodedata
async def  read_file_and_normalize(uploaded_file:UploadFile) -> str:
   file_in_bytes =  await uploaded_file.read()
   content_str = file_in_bytes.decode(encoding="utf-8",errors="strict")
   content_str = content_str.strip()
   normalized_str = unicodedata.normalize('NFC',content_str)
   return normalized_str

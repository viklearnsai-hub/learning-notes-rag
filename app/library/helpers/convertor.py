from fastapi import UploadFile
async def convert_from_file_to_bytes(file:UploadFile) -> bytes:
    return await file.read()

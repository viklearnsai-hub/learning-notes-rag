from fastapi import UploadFile

class UploadFileService:

    def uploadFile(self,uploadedFile:UploadFile):
        if(uploadedFile == "" or uploadedFile == None):
            return "File not present"
        extn  = uploadedFile.filename.split(".")[1]

        if(extn == "md" or extn == "txt"):
                print(uploadedFile.file.read())
                uploadedFile.close()
        else:
            return "Invalid format"



import unicodedata
import re
async def  read_file_and_normalize(content_bytes:bytes) -> str:
   content_str = content_bytes.decode(encoding="utf-8",errors="strict")
   return _normalize_text(content_str)

def _normalize_text(content_str:str)->str:
   normalized_str = unicodedata.normalize('NFC',content_str)
   normalized_str = normalized_str.strip()
   normalized_str = normalized_str.replace('\r\n','\n').replace('\r','\n')
   normalized_str = normalized_str.replace('\n\n','\n')
   normalized_str = normalized_str.replace('\t',' ')
   normalized_str = re.sub(r"\n {3,}","\n\n",normalized_str)
   normalized_str = re.sub(r" {2,}", " ", normalized_str)
   normalized_str = re.sub(r"(?m)^[ ]+", "", normalized_str)
   return normalized_str
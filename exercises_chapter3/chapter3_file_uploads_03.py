from fastapi import FastAPI, UploadFile, File
from typing import List

app = FastAPI()


@app.post("/files")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return [
        {
            "file_name": file.filename,
            "content-type": file.content_type
        } for file in files
    ]

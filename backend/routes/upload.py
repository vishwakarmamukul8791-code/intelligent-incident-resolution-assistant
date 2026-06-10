from fastapi import APIRouter, UploadFile, File
from fastapi import HTTPException
import os

router = APIRouter()

@router.post("/upload")

async def upload_file(file: UploadFile = File(...)):
    allowed_extensions = [".pdf", ".csv", ".txt"]

    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )
    name, extension = os.path.splitext(file.filename)

    file_path = f"data/raw/{file.filename}"

    counter = 1

    while os.path.exists(file_path):
        file_path = f"data/raw/{name}({counter}){extension}"
        counter += 1
        # file_path = f"data/raw/{file.filename}"


    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return {
        "message": "File uploaded successfully",
        "filename": os.path.basename(file_path)
    }
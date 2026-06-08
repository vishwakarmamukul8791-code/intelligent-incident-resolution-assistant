from fastapi import APIRouter,UploadFile,File

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):

    return {"message": "File upload successfully",
            "filename": file.filename
            }
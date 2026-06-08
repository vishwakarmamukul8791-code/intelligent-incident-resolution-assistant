from fastapi import APIRouter

router = APIRouter()

@router.get("/upload")
def upload_info():
    return {"message": "Upload endpoint working"}
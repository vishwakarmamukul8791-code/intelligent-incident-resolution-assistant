# from fastapi import APIRouter

# router = APIRouter()
# @router.get("/process-document")
# def process_document():
#     return {
#         "message" : "process document endpoint working"

#     }

# @router.get(
#     "/process-document",
#     summary="Read and Process Uploaded Document"
# )
# def process_document():
#      return {
#          "message" : "process document endpoint working"

#      }

from fastapi import APIRouter, HTTPException
from backend.services.embedding_service import generate_embeddings
import os

router = APIRouter()
def create_chunks(text, chunk_size=100):
    
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])

    return chunks



@router.post("/process-document")
def process_document(filename: str):

    file_path = f"data/raw/{filename}"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # return {
    #     "filename": filename,
    #     "content": content
    # }
    chunks = create_chunks(content)
    embeddings = generate_embeddings(chunks)

    return {
    "filename": filename,
    "total_chunks": len(chunks),
    "embedding_dimension": len(embeddings[0])
}
from fastapi import APIRouter
from backend.services.vector_store import (
    load_metadata
)

router = APIRouter()


@router.get("/document/{filename}")
def get_document(filename: str):

    metadata = load_metadata()

    chunks = []

    for record in metadata:

        if record["document_name"] == filename:
            chunks.append(record)

    return {
        "document_name": filename,
        "total_chunks": len(chunks),
        "chunks": chunks
    }
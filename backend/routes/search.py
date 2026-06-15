from fastapi import APIRouter
from backend.services.retrieval_service import search_similar_chunks

router = APIRouter()

@router.get("/search")
def search(query: str):

    results = search_similar_chunks(query)

    return {
        "query": query,
        "results": results
    }

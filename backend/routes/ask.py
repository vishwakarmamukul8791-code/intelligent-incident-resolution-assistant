from backend.services.retrieval_service import (search_similar_chunks,get_context)  
from backend.services.llm_service import (generate_answer)  
from fastapi import APIRouter

router = APIRouter()


@router.get("/ask")
def ask_question(query: str):

    results = search_similar_chunks(
        query
    )

    context = get_context(
        results
    )

    answer = generate_answer(
        query,
        context
    )

    return {
        "question": query,
        "answer": answer
    }